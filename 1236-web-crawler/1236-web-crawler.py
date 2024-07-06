# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from urllib.parse import urlparse

def hostname(url):
    return urlparse(url).netloc

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        q = {startUrl}
        seen = {startUrl}

        while q:
            neighbors = {
                url for url in htmlParser.getUrls(q.pop())
                if hostname(url) == hostname(startUrl)
                and url not in seen
            }
            q |= neighbors
            seen |= neighbors
        
        return seen
