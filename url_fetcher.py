import requests
from lxml import html
from multiprocessing import Pool


class UrlFetcher:

    def __init__(self, size_of_pool=4):

        self.size_of_pool = size_of_pool

    def get_content(self, url):
        
        try:
            response = requests.get(url)

        except requests.ConnectionError:
            dict_of_results = {'status_code': -1, 'err': requests.ConnectionError, 'url': url}
        except requests.Timeout:
            dict_of_results = {'status_code': -1, 'err': requests.Timeout, 'url': url}
        except requests.TooManyRedirects:
            dict_of_results = {'status_code': -1, 'err': requests.TooManyRedirects, 'url': url}
        else:
            content = response.text
            dict_of_results = {'status_code': response, 'url': url, 'content': content}
       
        return dict_of_results

    def get_pages(self, urls):
        
        pool = Pool(self.size_of_pool)
        results = pool.map(self.get_content, urls)

        pool.close()
        pool.join()
        return results


# if __name__ == "__main__":

#     example = [
#         'http://www.pythonsdfsf.org',
#         'http://www.python.org/about/',
#         'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
#         'http://www.python.org/doc/',
#         'http://www.python.org/download/',
#         'http://www.python.org/about/'
#     ]

#     content1 = UrlFetcher(4)
#     print(content1.get_pages(example))
