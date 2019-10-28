from locator.quote_locators import QuoteLocator

class QuoteParser:

    def __init__(self,parnet):
        self.parnet = parnet

    def __repr__(self):
        return f"Quote {self.content} by {self.author}"

    @property
    def content(self):
        locator = QuoteLocator.CONTENT
        return self.parnet.select_one(locator)

    @property
    def author(self):
        locator = QuoteLocator.AUTHOR
        return self.parnet.select_one(locator)

    @property
    def tags(self):
        locator = QuoteLocator.TAGS
        return [e.string for e in self.parnet.select(locator)]
