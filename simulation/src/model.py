# -*- coding: utf-8 -*-
# @Author: Chandan Yeshwanth
# @Date:   2016-04-17 20:28:57
# @Last Modified by:   Chandan Yeshwanth
# @Last Modified time: 2016-04-25 15:51:59

import pandas as pd
import random

class Node(object):
	"""Represents a single node with detectors"""
	def __init__(self, num_detectors, enc_len):
		# generate random binary strings 
		# with length = connection encoding length
		rand_nums = [random.randint(0, 2**enc_len - 1) 
						for i in range(num_detectors)]
		# build the format string 
		format_str = "{{0:0{length}b}}".format(length=enc_len)
		# format all numbers in binary and store in dataframe
		self.detectors = pd.Series(
							map(lambda num: format_str.format(num),		
							rand_nums)
						)
		self.match_count = pd.Series([0 for i in range(num_detectors)])

class PPModel(object):
	"""Model for privacy preserving AIS"""
	def __init__(self, params):
		self.node = Node(params.num_detectors, params.encoding_length)

	def tolerize(self, connections):
		pass

	def receive_connection(self):
		pass
		
class NonPPModel(object):
	"""Model for Regular AIS"""
	def __init__(self, params):
		detectors_per_party = params.num_detectors / params.num_parties
		self.nodes = [Node(detectors_per_party, params.encoding_length)
						for i in range(params.num_parties)]

	def tolerize(self, connections):
		pass

	def receive_connection(self):
		pass
		

def main():
	pass

if __name__ == '__main__':
	main()
