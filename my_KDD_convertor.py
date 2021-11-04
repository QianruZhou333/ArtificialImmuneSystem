# Author: Qianru Zhou
# Email: zhouqr333@126.com
# Magic, do not touch!!

import csv

def to_binary(num, bitsNum):
        """ Convert a interger to a binary string
	Args:
		num: the interger to be converted to binary
		bitsNum: the number of bits of the binary string
	Returns:
		the binary string
        """
	return format(num, '0>'+bitsNum+'b')


def csv_to_binary(csvDir, binaryDir):
	""" Convert the strings in csv file to binary strings
	and write to file
	Args:
		csvDir: the absolute directory of the csv file
		binaryDir: the absolute directory of the binary file
	"""
	toFile = open(binaryDir, 'a')
	with open(csvDir) as f:
		f_csv = csv.DictReader(f)
		for row in f_csv:
		    toFile.write(format(int(row['protocol']),'0>8b') \
		    + format(int(row['dport']),'0>16b') \
		    + format(int(row['checksum']),'0>16b') \
		    + format(int(row['length']),'0>16b') \
		    + format(int(row['offset']),'0>15b') \
		    + '\n')
	toFile.close()

if __name__ == '__main__':
    csv_to_binary('/Users/silvia/Documents/code/my/my_pcap/nonself/ipsweep.csv', \
    		  '/Users/silvia/Documents/code/my/my_pcap/nonself/ipsweep_binary')
    csv_to_binary('/Users/silvia/Documents/code/my/my_pcap/nonself/back.csv', \
    		  '/Users/silvia/Documents/code/my/my_pcap/nonself/back_binary')
    csv_to_binary('/Users/silvia/Documents/code/my/my_pcap/nonself/loadmodule.csv', \
    		  '/Users/silvia/Documents/code/my/my_pcap/nonself/loadmodule_binary')
    csv_to_binary('/Users/silvia/Documents/code/my/my_pcap/nonself/buffer_overflow.csv', \
    		  '/Users/silvia/Documents/code/my/my_pcap/nonself/buffer_overflow_binary')
    csv_to_binary('/Users/silvia/Documents/code/my/my_pcap/nonself/neptune.csv', \
    		  '/Users/silvia/Documents/code/my/my_pcap/nonself/neptune_binary')
    csv_to_binary('/Users/silvia/Documents/code/my/my_pcap/nonself/guesspassword.csv', \
    		  '/Users/silvia/Documents/code/my/my_pcap/nonself/guesspassword_binary')

    csv_to_binary('/Users/silvia/Documents/code/my/my_pcap/self/self_text.csv', \
    		  '/Users/silvia/Documents/code/my/my_pcap/self/self_binary')

