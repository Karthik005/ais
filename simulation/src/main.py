# -*- coding: utf-8 -*-
# @Author: chandan
# @Date:   2016-04-14 17:11:37
# @Last Modified by:   Chandan Yeshwanth
# @Last Modified time: 2016-04-25 13:20:22

import sim

def main():
	params = sim.SimParams(4, 1000, 10, 10000, "trainsmall.txt")
	results = sim.run_sim(params)

	results.display()

if __name__ == '__main__':
	main()