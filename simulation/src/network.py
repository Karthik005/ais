# -*- coding: utf-8 -*-
# @Author: Chandan Yeshwanth
# @Date:   2016-04-18 15:07:22
# @Last Modified by:   Chandan Yeshwanth
# @Last Modified time: 2016-04-24 22:43:33

import pandas as pd
import os

# folder containing data files
DATA_DIR = "../data/"

def read_KDD_data(filename):
	""" Read connection data and labels from CSV file into dataframe """
	path = os.path.join(DATA_DIR, filename)
	df = pd.read_csv(path, header=None)

	# get the values of the last column 
	last_col_values = df.iloc[:, -1].unique()

	data = df.iloc[:, :-1]
	labels = None

	if "normal" in last_col_values and "anomaly" in last_col_values:
		# this is the training dataset
		labels = df.iloc[:, -1]

	return data, labels

def encode_data(df):
	""" Convert numerical variables to binary and categorial to one-hot encoding """
	enc_data = pd.DataFrame()

	column_dfs = []

	for (col_name, values) in df.iteritems():
		unique_vals = values.unique()

		# drop attributes with constant value
		if len(unique_vals) <= 1:
			continue

		# if values are string or 0/1
		# then categorial attribute
		if (len(unique_vals) == 2 and 0 in unique_vals and 1 in unique_vals) \
			 or isinstance(unique_vals[0], basestring):
			print col_name, "CATEGORICAL"

			# convert cols to string and concat
			column_dfs.append(pd.get_dummies(values).applymap(
					lambda x: str(int(x))
				))
		# if column is int
		elif isinstance(unique_vals[0], int):
			# find the length of binary repr. of the max value
			max_bin_len = len("{0:b}".format(max(unique_vals)))
			format_str = "{{0:0{maxlen}b}}".format(maxlen=max_bin_len)
			# convert all ints to binary with this length
			column_dfs.append(values.apply(lambda num:format_str.format(num)))
		else:
			pass

	# concat all columns
	enc_data = pd.concat(column_dfs, axis=1).apply(
			lambda col: "".join(col),
							axis = 1
						)

	return enc_data

def main():
	data, labels = read_KDD_data("train.txt")

	enc_data = encode_data(data)

if __name__ == '__main__':
	main()