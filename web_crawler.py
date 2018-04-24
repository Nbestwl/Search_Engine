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
	return: return frontier and a visited url repo
"""
def url_scraping(url, frontier, visited_repo, limit):
	# request will time out after 1 second if its not responding
	page = requests.get(url, timeout=1)
	soup = BeautifulSoup(page.text, "lxml")

	# recursively enqueue the link
	for link in soup.find_all('a'):
		url = link.get('href')
		# make sure the link is valid
		if url.startswith("http") if url else False and not frontier.full():
			frontier.put(url)

	# keeps crawling when the frontier is not empty
	while not frontier.empty():
		# dequeue the frontier
		next_url = frontier.get()
		if len(visited_repo) < limit:
			# make sure the item is not duplicated
			if next_url not in visited_repo:
				#  mark the dequeued item as visited
				visited_repo.append(next_url)
		else:
			# return when the repo reaches the limit
			return frontier, visited_repo
		# continue scraping urls if the frontier hasn't reach the limit
		if frontier.qsize() <= limit:
			# recursively call the scraping method
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
	print "frontier:", frontier.qsize()
	print "visitted", visited_repo


def main():
	root_url = 'http://www.leiwangcoding.com'
	spider(root_url, 100)


if __name__ == '__main__':
	main()
