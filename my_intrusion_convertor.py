# Author: Qianru Zhou
# Email: zhouqr333@126.com
# Magic, do not touch!!

import csv

def intrusionCSV_to_binary(csvDir, binaryDir):
	""" Convert the intrusion data in 'intrusion.csv' to binary strings
	Args:
		csvDir: the absolute directory of the csv file
		binaryDir: the absolute directory of the binary file
	"""
	toFile = open(binaryDir, 'a')
	with open(csvDir, 'r') as f:
		f_csv = csv.DictReader(f)
		for row in f_csv:
		    toFile.write(ip_addr(row['ip_src']) \
		    + ip_addr(row['ip_dst']) \
		    + format(int(row['dport']),'0>16b') \
		    + format(int(row['length']),'0>16b') \
		    + '\n')
	toFile.close()


def to_binary(num, bitsNum):
	""" Convert a interger to a binary string
	Args: 
		num: the interger to be converted to binary
		bitsNum: the number of bits of the binary string
	Returns:
		the binary string
	"""
	return format(num, '0>'+bitsNum+'b')


def ip_addr(address):
	""" Convert a IP address to a binary string
	Args:
		address: a IP address string, e.g., 1.2.3.4
	Returns
		bstr: a binary string
	"""
	ip = address.split('.')
	bstr = ''
	for i in ip:
	    bstr += str(format(int(i),'0>8b'))
	return bstr


if __name__ == '__main__':
	intrusionCSV_to_binary('/Users/silvia/Documents/code/my/my_pcap/log/intrusion.csv', \
			       '/Users/silvia/Documents/code/my/my_pcap/log/intrusion_bin')
