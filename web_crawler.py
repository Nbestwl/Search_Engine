'''
(1) a multi-threaded spider that fetches and parses webpages
(2) the URL frontier which stores to-be-crawled URLs
(3) the URL repository that stores crawled URLs.
'''
import requests
from bs4 import BeautifulSoup
from Queue import Queue
from pre_processing import progressbar


"""
	pre: a url
	post: extract the urls at the page
	return: return all urls
"""
def url_scraping(url):
	page = requests.get('http://www.leiwangcoding.com', timeout=5)
	soup = BeautifulSoup(page.text, "lxml")
	return soup.find_all('a')


"""
	pre: a root url which the crawling starts from, the limit of the frontier
	post: crawl all pages from the frontier
	return: NONE
"""
def spider(root_url, limit):
	# set the frontier with a limit
	frontier = Queue(maxsize=limit)
	# recursively enqueue the link
	for link in url_scraping(root_url):
		# make sure the link is valid
		url = link.get('href')
		if url.startswith("http") and not frontier.full():
			frontier.put(url)

	while not frontier.empty():
		print frontier.get()


def main():
	root_url = 'http://www.leiwangcoding.com'
	spider(root_url, 5)


if __name__ == '__main__':
	main()
