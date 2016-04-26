# -*- coding: utf-8 -*-
# @Author: Chandan Yeshwanth
# @Date:   2016-04-17 20:28:57
# @Last Modified by:   Chandan Yeshwanth
# @Last Modified time: 2016-04-26 10:25:20

import pandas as pd
import random

def r_cont_bits(s1, s2, r):
	""" r-contiguous bits - s1 and s2 match if they have r contiguous bits in 
	common """
	for start in range(0, len(s1) - r + 1):
		end = start + r 

		if s1[start:end] == s2[start:end]:
			return True

	return False

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
	# print r_cont_bits("abc", "abd", 3) 
	# print r_cont_bits("sdnfding", "adnfdeng", 5) 
	print r_cont_bits("b" * 100 + "aa", "b" * 100 + "aa", 2) 

if __name__ == '__main__':
	main()
