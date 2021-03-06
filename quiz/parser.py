import sys
from html.parser import HTMLParser

from cs50 import get_string


class Stack:

    def __init__(self):
        """Implement stack with a list."""
        self.list = []

    def peek(self):
        """Return item on top of stack without removing."""
        peekitem = self.list[0] # shows the first item of the list
        return peekitem

    def pop(self):
        """Remove and return item on top of stack."""
        remove = self.list.pop(0) # removes the first item
        popitem = self.list[0] # shows the first item of the list
        return popitem

    def push(self, item):
        """Add item to top of stack."""
        self.list.insert(0, item) # insert item to the first place of the list
        pass

    def size(self):
        """Return number of items in stack."""
        return len(self.list)


class MyHTMLParser(HTMLParser):

    def __init__(self):
        """Initialize parser."""
        super().__init__()
        self.stack = Stack()

    def handle_starttag(self, tag, attrs):
        """Handle the start of a tag."""
        starttag = self.stack.push(tag) # put new tag to the front of the list
        pass  # TODO

    def handle_endtag(self, tag):
        """Handle the end tag of an element."""
        endtag = self.stack.list.append(tag) # append the list by adding new tags to the end of the list
        pass  # TODO

    def feed(self, data):
        """
        Feed some text to the parser.
        Return True if all end tags match start tags.
        """
        try:
            super().feed(data)
        except:
            return False
        else:
            return self.stack.size() == 0


def main():

    # Get HTML
    html = get_string("HTML: ")

    # Parse HTML
    parser = MyHTMLParser()
    if parser.feed(html):
        print("matched")
    else:
        print("mismatched")


if __name__ == "__main__":
    main()
