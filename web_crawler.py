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
def url_scraping(url, frontier, visited_repo, limit):
	page = requests.get(url, timeout=5)
	soup = BeautifulSoup(page.text, "lxml")

	# recursively enqueue the link
	for link in soup.find_all('a'):
		url = link.get('href')
		# make sure the link is valid
		if url.startswith("http") if url else False and not frontier.full():
			frontier.put(url)

	while not frontier.empty():
		next_url = frontier.get()
		# dequeue a url and mark it as visited
		if len(visited_repo) < limit:
			if next_url not in visited_repo:
				visited_repo.append(next_url)
		else:
			return frontier, visited_repo
		url_scraping(next_url, frontier, visited_repo, limit)


"""
	pre: a root url which the crawling starts from, the limit of the frontier
	post: crawl all pages from the frontier
	return: NONE
"""
def spider(root_url, limit):
	# set the frontier with a limit
	frontier = Queue(maxsize=0)
	visited_repo = []

	frontier, visited_repo = url_scraping(root_url, frontier, visited_repo, limit)
	print visited_repo


def main():
	root_url = 'http://www.leiwangcoding.com'
	spider(root_url, 10)


if __name__ == '__main__':
	main()
