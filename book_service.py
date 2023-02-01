import requests
from xml.etree import ElementTree

class BookService:
    def __init__(self):
        return

    def get_book_info(self, book_title, author=None):

        author_name = self.search_author_by_name(author)

        params = [('title', book_title), ('author', author_name)]
        response = requests.get("https://openlibrary.org/search.json", params=params)

        if response.status_code == 404:
            return None

        data = response.json()

        if not data["docs"]:
            return None

        open_library_key = data["docs"][0]["key"]
        open_library_url = "https://openlibrary.org"+open_library_key

        num_pages = data["docs"][0]["number_of_pages_median"]
        pub_year = data["docs"][0]["first_publish_year"]
        authors = data["docs"][0]["author_name"]
        title = data["docs"][0]["title"]

        description = self.get_book_description(open_library_key)

        return {
            "open_library_url": open_library_url,
            "num_pages": num_pages,
            "pub_year": pub_year,
            "authors": authors,
            "title": title,
            "works_key": open_library_key,
            "description": description,
        }


    def get_book_description(self, book_key):        
        if book_key is None:
            return None

        response = requests.get("https://openlibrary.org/%s.json"%(book_key))

        if response.status_code == 404:
          return None

        data = response.json()

        if 'description' not in data:
          return None

        try:
          description = data["description"]["value"]
        except TypeError:
          description =  data["description"]

        return description


    def search_author_by_name(self, name):
        if name is None:
            return None
        
        response = requests.get("https://openlibrary.org/search/authors.json?q="+name)

        if response.status_code == 404:
            return None

        data = response.json()

        author_name = data["docs"][0]["name"]

        if author_name is None:
            return None
            
        return author_name


