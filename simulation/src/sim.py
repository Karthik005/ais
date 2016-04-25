# -*- coding: utf-8 -*-
# @Author: Chandan Yeshwanth
# @Date:   2016-04-17 20:28:53
# @Last Modified by:   Chandan Yeshwanth
# @Last Modified time: 2016-04-25 15:53:23

from model import PPModel, NonPPModel
import network

class SimParams(object):
	"""AIS Simulation Parameters"""
	def __init__(self, num_parties=4, 
					num_detectors=1000,
					activ_thresh=10, 
					num_iters=10000,
					fname="train.txt",
					rcontbits_r=5):

		super(SimParams, self).__init__()

		# number of parties
		self.num_parties = num_parties
		# total number of detectors
		self.num_detectors = num_detectors
		# detector activation threshold
		self.activ_thresh = activ_thresh
		# total simulation time
		self.num_iters = num_iters
		# file containing network data
		self.data_file = fname
		# length of encoding of connection and detector
		self.encoding_length = None
		# "r" value in r-contiguous bits
		self.rcontbits_r = rcontbits_r

class SimResults(object):
	"""docstring for SimResults"""
	def __init__(self, params):
		self.simparams = params

		self.false_pos = 0
		self.false_neg = 0
		self.true_pos = 0
		self.true_neg = 0

	def display(self):
		print "sim results"

def run_sim(params):
	data, labels = network.read_KDD_data(params.data_file)
	connections = network.encode_data(data)
	# set encoding length
	params.encoding_length = len(connections.iloc[0])

	ais, ppais = NonPPModel(params), PPModel(params)
	result = SimResults(params)

	# get network connections data

	print "Encoding Length: ", params.encoding_length

	# select some self connections
	self_connections = data[labels["label"] == "normal"]
	# tolerize on these


	# iterate over time
		# kill detectors with probability
		# expose ais to connection
		# update results

	return result

def main():
	pass

if __name__ == '__main__':
	main()