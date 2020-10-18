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
        ans = set()
        
        def rec(url):
            if url in ans:
                return
            
            ans.add(url)
            host_name = 'http://' + url[7:].split('/')[0]
            
            all_urls = htmlParser.getUrls(url)
            for u in all_urls:
                if u in ans or not u.startswith(host_name):
                    continue
                rec(u)
            return
        
        rec(startUrl)
        return list(ans)
