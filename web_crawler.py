'''
(1) a multi-threaded spider that fetches and parses webpages
(2) the URL frontier which stores to-be-crawled URLs
(3) the URL repository that stores crawled URLs.
'''
import requests
from bs4 import BeautifulSoup
from Queue import Queue
from multiprocessing.pool import ThreadPool
from pre_processing import progressbar


"""
	pre: a url
	post: extract the urls at the page
	return: return frontier and a visited url repo
"""
def url_scraping(url, frontier, visited_repo, limit):
	# request will time out after 1 second if its not responding
	try:
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
					# indicate the crawling progress
					# progressbar(len(visited_repo), limit, prefix = 'Progress:', length = 50)
			else:
				# return when the repo reaches the limit
				return frontier, visited_repo
			# continue scraping urls if the frontier hasn't reach the limit
			if frontier.qsize() <= limit:
				# recursively call the scraping method
				url_scraping(next_url, frontier, visited_repo, limit)
	# catch the exception if any url is not responding
	except Exception as e:
		print e.message
    	return


"""
	pre: a root url which the crawling starts from, the limit of the frontier
	post: crawl all pages from the frontier
	return: NONE
"""
def spider(root_url, limit):
	# initialize the frontier and url repo
	frontier = Queue(maxsize=0)
	visited_repo = []

	frontier, visited_repo = url_scraping(root_url, frontier, visited_repo, limit)
	print "\nfrontier:", frontier.qsize()
	print "\nvisitted", visited_repo
	print "\nvisitted size: ", len(visited_repo)


def main():
	root_url = 'http://www.ku.edu'
	spider(root_url, 1000)

	# creating threads
	# t1 = Thread(target=spider, args=(root_url, 10))
	# t2 = Thread(target=spider, args=(root_url, 10))
	# t3 = Thread(target=spider, args=(root_url, 10))
	# t4 = Thread(target=spider, args=(root_url, 10))

	# # starting threads
	# t1.start()
	# t2.start()
	# t3.start()
	# t4.start()

	# # wait until all threads finish
	# t1.join()
	# t2.join()
	# t3.join()
	# t4.join()


if __name__ == '__main__':
	main()
