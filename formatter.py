class Formatter:
    def __init__(self, book_info, cleaned, book_suggested_count):
        self.book_info = book_info
        self.cleaned = cleaned
        self.book_suggested_count = book_suggested_count
    
    def format_link(self):
        pass

    def format_header(self):
        pass

    def format_description(self):
        pass

    def format_book_footer(self):
        pass

    def supports_long_version(self):
        return True
    
    def get_section_separator(self):
        return '\n\n'