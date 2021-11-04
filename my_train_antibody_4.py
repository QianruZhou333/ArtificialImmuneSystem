# Qianru Zhou (zhouqr333@126.com)

import re

def get_longest_match(num1, num2):
	""" Get the longest number of contiguous bits which the two strings have in common  
	"""
	# an all 1s binary string with 96 bits long, in order to get reverse
	all1s = 0b111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

	# get the and or results of num1 and num2
	s = format(num1^num2^all1s, '0>96b')
	# get all the substrings of contiguous 1s
	pattern = re.compile(r'1{1,}')
	results = pattern.findall(s)

	# get the longest contiguous 1s
	cnt = 0
	for r in results:
		if cnt < len(r):
		    cnt = len(r)
	#print('the longest contiguous bits is: %d' % cnt)
	return cnt


def train_antibody(immatureDir, matureDir, selfDir, threshold):
	""" match the immuature antibodies with self set, if match,
	discard the antibody.
	Args:
		immatureDir: the absolute directory of the immuature antibodies
		matureDir: the absolute directory of the muature antibodies
		selfDir: the absolute directory of the self set
		threshold: the threshold of the match
	"""
	antibodies = open(immatureDir, 'r+')
	matureAntibody = open(matureDir, 'w')

	for antibody in antibodies:
		isSelf = False
		selfset = open(selfDir, 'r')
		for self in selfset:
		    if get_longest_match(int(antibody,2), int(self,2)) >= threshold:
		    	isSelf = True
	#		print(antibody, int(antibody,2))
	#		print(self, int(self,2))
	#	        print(isSelf)
      		        break
		selfset.close()
		if not isSelf:
		    matureAntibody.write(antibody)
#		    print('written to mature antibody!')

	antibodies.close()
	matureAntibody.close()


if __name__ == '__main__':
    train_antibody('/Users/silvia/Documents/code/my/my_pcap/log/mature_antibody_4', \
    '/Users/silvia/Documents/code/my/my_pcap/log/mature_antibody_44',\
    '/Users/silvia/Documents/code/my/my_pcap/log/log_binary_4',
    10)
