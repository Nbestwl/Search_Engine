# -*- coding: utf-8 -*-

'''
(1) a multi-threaded spider that fetches and parses webpages
(2) the URL frontier which stores to-be-crawled URLs
(3) the URL repository that stores crawled URLs.
'''
import os
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
	# catch the exception if any url is not responding
	except Exception as e:
		# print e.message
		return

	# recursively enqueue the link
	for link in soup.find_all('a'):
		temp = link.get('href')
		# make sure the link is valid
		if (temp.startswith("http") if temp else False) and not (temp.endswith("pdf") if temp else False):
			frontier.put(temp)

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
				progressbar(len(visited_repo), limit, prefix = 'Progress:', length = 50)
		else:
			# return when the repo reaches the limit
			return frontier, visited_repo
		# continue scraping urls if the frontier hasn't reach the limit
		if frontier.qsize() <= limit:
			# recursively call the scraping method
			url_scraping(next_url, frontier, visited_repo, limit)


"""
	pre: a path to a directory
	post: remove all files within that dir
	return: NONE
"""
def init_dir(mydir):
	filelist = [ f for f in os.listdir(mydir) ]
	for f in filelist:
		os.remove(os.path.join(mydir, f))


"""
	pre: a list of urls
	post: writing the html content into a file
	return: None
"""
def file_writer(urls, mydir):
	for url in urls:
		try:
			page = requests.get(url, timeout=1)
			content = page.text

			basename = "Doc"
			index = urls.index(url)
			suffix = ".".join([str(index), 'html'])
			filename = "_".join([basename, suffix])
			with open(os.path.join(mydir, filename), "w") as file:
				file.write(content.encode('utf-8'))

		# catch the exception if any url is not responding
		except Exception as e:
			# print e.message
			continue


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
	print "\nvisited", visited_repo
	print "\nvisited size: ", len(visited_repo)

	# clear the directory before writing
	mydir = './temp/'
	init_dir(mydir)
	# writing all html files to the dir
	file_writer(visited_repo, mydir)


def main():
	root_url = 'http://www.leiwangcoding.com'
	spider(root_url, 50)

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
