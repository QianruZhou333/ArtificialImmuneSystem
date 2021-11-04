# Author: Qianru Zhou
# Email: zhouqr333@126.com
# Magic, do not touch!!

""" generate immature detector, a file with random 96 bits binary strings
"""

from random import randint

def reduce_duplicate(inputPath, outputPath):
	""" delete the duplicate strings in the log for efficiency 
	"""
	patterns = []
	with open(inputPath, 'r') as f:
		for line in f.readlines():
			if line not in patterns:
			    patterns.append(line)

	with open(outputPath, 'w+') as out:
		for pattern in patterns:
		    out.write(pattern)

	# another way to do that
	#tmp = open('/Users/silvia/Documents/code/my/my_pcap/log').readlines()
    	#set(tmp)
    	#with open('/Users/silvia/Documents/code/my/my_pcap/uniLog', 'w+') as f:
    		#for item in tmp:
	    	#f.write(item)


def create_antibody():
	""" generate 96 bits long binary strings randomly
	"""
	s = list(''.zfill(96))
	for i in range(0,96):
	    s[i]=str(randint(0,9)%2)

	return ''.join(s)


if __name__ == '__main__':
#	with open('/Users/silvia/Documents/code/my/my_pcap/log/raw_immature_detector', 'w+') as f:
#		for _ in range(5000000):
#			f.write(create_antibody()+'\n')

	reduce_duplicate('/Users/silvia/Documents/code/my/my_pcap/log/raw_immature_detector', \
	'/Users/silvia/Documents/code/my/my_pcap/log/immature_detector')
