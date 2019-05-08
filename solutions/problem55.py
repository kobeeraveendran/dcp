import string
import random

class URLShortener:

    def __init__(self):
        self.mapping = {}
        self.chars = list(set(string.ascii_letters + '0123456789'))

    def shorten(self, url):
        shortened = ''
        
        for _ in range(6):
            shortened += random.choice(self.chars)

        self.mapping[shortened] = url

        return shortened

    def restore(self, short):

        return self.mapping[short]

url_shortener = URLShortener()
test1 = url_shortener.shorten('https://www.google.com')
print(test1)                        # expected out: some alphanumeric string of length 6
test1 = url_shortener.restore(test1)
print(test1)                            # expected out: https://www.google.com

# adding the same URL more than once
test1 = url_shortener.shorten('https://www.google.com')
print(test1)                        # expected out: some alphanumeric string of length 6 (different from above)
test1 = url_shortener.restore(test1)
print(test1)                            # expected out: https://www.google.com