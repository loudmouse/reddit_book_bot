import praw
from db import DB
import re
from book_service import BookService
import time
from uuid import uuid4
from formatter_factory import FormatterFactory

class Bot:
    def __init__(self):
        self.reddit = praw.Reddit()
        self.book_service = BookService()
        self.db = DB()

        self.db.create_tables()

    def listen_to_subreddit(self, name):
        for comment in self.reddit.subreddit(name).stream.comments():
            comment_invocations = self.db.count_comment_invocations(comment.id)
            if comment_invocations > 0:
              continue
            submission = comment.submission
            formatted_reddit_comment = ""
            for m in re.finditer('\{\{([^}]+)\}\}|\{([^}]+)\}', comment.body):
                group = m.group()
                cleaned = self.__clean_group(group)

                book, author = self.__extract_book_and_author(cleaned)

                book_info = self.book_service.get_book_info(book, author)

                if book_info is None:
                    continue

                book = (book_info["works_key"], book_info["title"], book_info["open_library_url"], int(time.time()))
                invocation = (str(uuid4()), book_info["works_key"], comment.id, submission.id, "", comment.permalink, int(time.time()))

                self.db.save_book(book)
                self.db.save_invocation(invocation)

                book_suggested_count = self.db.count_book_requests(book_info["works_key"])

                formatter = FormatterFactory.for_subreddit(
                    subreddit_name=comment.subreddit.display_name,
                    book_info=book_info,
                    cleaned=cleaned,
                    book_suggested_count=book_suggested_count)

                formatted_reddit_comment += formatter.format_link() + formatter.get_section_separator()
                formatted_reddit_comment += formatter.format_header() + formatter.get_section_separator()
                formatted_reddit_comment += formatter.format_description() + formatter.get_section_separator()
                
                formatted_reddit_comment += formatter.format_book_footer() + formatter.get_section_separator()

            if len(formatted_reddit_comment) > 0:
                post = (submission.id, submission.title, submission.url)
                self.db.save_post(post)

                formatted_reddit_comment += "***" + formatter.get_section_separator()

                invocations = self.db.count_invocations()
                formatted_reddit_comment += self.__make_footer(invocations)
                comment.reply(formatted_reddit_comment)

    def __clean_group(self, group):
        return group.replace("{", "").replace("}", "").replace("*", "")

    def __extract_book_and_author(self, match):
        book, *author = match.lower().rsplit("by", 1)
        book = book.strip()
        author = author[0].strip() if author else None

        return (book, author)

    def __make_footer(self, suggestions):
        s = "s" if suggestions > 1 else ""
        return "^(%s book%s suggested | )[^(Source Code)](https://github.com/loudmouse/reddit_book_bot)" % (
            suggestions, s)