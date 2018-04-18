# this is the linked list class for sotring posting lists
# structure:
# 1.doc_num : document ID
# 2.term_freq : term frequency in that document
# 3.next : acts as a pointer points to the next node


"""
	pre: NONE
	post: class for Node
	return: NONE
"""
class Node(object):
	def __init__(self, num, frequency, n = None):
		self.doc_num = num
		self.term_freq = frequency
		self.m_next = n

	def get_next(self):
		return self.m_next

	def set_next(self, n):
		self.m_next = n

	def get_doc(self):
		return self.doc_num

	def set_doc(self, num):
		self.doc_num = num

	def get_freq(self):
		return self.term_freq

	def set_freq(self, frequency):
		self.term_freq = frequency


"""
	pre: NONE
	post: class for Linkedlist
	return: NONE
"""
class LinkedList(object):
	def __init__(self, r = None):
		self.root = r
		self.cur = self.root
		self.size = 0

	def get_size(self):
		return self.size

	def add(self, doc_num, term_freq):
		if self.root == None:
			new_node = Node(doc_num, term_freq, None)
			self.root = new_node
			self.cur = new_node
		else:
			new_node = Node(doc_num, term_freq, None)
			self.cur.set_next(new_node)
			self.cur = new_node
		self.size += 1

	def remove(self, doc_num):
		cur_node = self.root
		prev_node = None
		while cur_node:
			if cur_node.get_doc() == doc_num:
				if prev_node:
					prev_node.set_next(cur_node.get_next())
				else:
					self.root = cur_node
				self.size -= 1
				return True
			else:
				prev_node = cur_node
				cur_node = cur_node.get_next()
		return False

	def find(self, index):
		cur_node = self.root
		while cur_node:
			if cur_node.get_doc() == index:
				return cur_node.get_freq()
			else:
				cur_node = cur_node.get_next()
		return False

	def printList(self):
		message = ''
		start = self.root
		while start:
			if start.get_next() == None:
				message += 'Doc#: {} term_freq: {}'.format(start.get_doc(), start.get_freq())
			else:
				message += 'Doc#: {} term_freq: {} -> '.format(start.get_doc(), start.get_freq())
			start = start.get_next()
		print message

