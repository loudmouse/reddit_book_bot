from default_formatter import DefaultFormatter

class FormatterFactory:
    @staticmethod
    def for_subreddit(subreddit_name, book_info, cleaned, book_suggested_count):
        return DefaultFormatter(
                book_info=book_info,
                cleaned=cleaned,
                book_suggested_count=book_suggested_count)