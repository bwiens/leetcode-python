# Benjamin Wiens
# Web Crawler (https://leetcode.com/problems/web-crawler/)

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

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname, result, grab = '', [], False
        # get hostname
        for index, char in enumerate(startUrl):
            if grab:
                if char == '/':
                    break
                hostname += char
            if char == '/' and startUrl[index-1] == '/':
                grab = True
        hostname = 'http://' + hostname
        result.append(startUrl)
		# process stack
        stack = [startUrl]
        while stack:
            q = stack.pop()
            urls = htmlParser.getUrls(q)
            for url in urls:
                if url.find(hostname) != -1:
                    if url not in result:
                        result.append(url)
                        stack.append(url)
        return result
