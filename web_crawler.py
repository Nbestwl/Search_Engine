'''
(1) a multi-threaded spider that fetches and parses webpages
(2) the URL frontier which stores to-be-crawled URLs
(3) the URL repository that stores crawled URLs.
'''
from collections import deque
import requests
from lxml import html
from pre_processing import progressbar

class Spider:
	def __init__(self, capacity):
		# set the limitation of the spider capacity
		self.capacity = capacity
		self.frontier = deque()
		self.url_repo = []

	def get_frontier_size(self):
		return len(self.frontier)

	def get_repo_size(self):
		return len(self.url_repo)

	def get_repo(self):
		return self.url_repo

	def enqueue(self, item):
		self.frontier.appendleft(item)

	def dequeue(self):
		item = self.frontier.pop()
		return item

	def crawl(self, root_url, iteration=0):
		iteration += 1

		page = requests.get(root_url)
		webpage = html.fromstring(page.content)
		urls = webpage.xpath('//a/@href')

		# enqueue url to the left of the queue
		for url in urls:
			if not url.startswith("http"):
				url = root_url + url
			if url not in self.get_repo():
				self.enqueue(url)

		# if queue is not empty, recursively crawling the the domain
		if self.get_frontier_size() != 0:
			if self.get_repo_size() <= self.capacity:
				# print 'frontier: ', self.get_frontier_size()
				next_url = self.dequeue()
				# print next_url
				self.url_repo.append(next_url)

				progressbar(iteration, self.capacity, prefix = 'Progress:', length = 50)
				self.crawl(next_url, iteration)
			else:
				# print "frontier reaches the limit, size: ", self.get_frontier_size()
				return
		else:
			print "done"
			return


def main():
	root_url = 'http://www.leiwangcoding.com/'

	spider = Spider(1000)
	spider.crawl(root_url)
	print spider.get_repo_size()
	print spider.get_repo()

if __name__ == '__main__':
	main()
