# author: Qianru Zhou (zhouqr333@126.com)

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


def train_antibody(immatureDir, nonselfDir, matureDir, threshold):
	""" match the immature antibodies with non-self sets, if match,
	add it as mature antibody.
	Args:
		immatureDir: the absolute directory of the immature antibodies
		matureDir: the absolute directory of the mature antibodies
		nonselfDir: the absolute directory of the non-self binary strings
		threshold: the threshold of the match
	"""
	immatureSet = open(immatureDir, 'r+')
	nonselves = open(nonselfDir, 'r')
	matureSet = open(matureDir, 'a')

	for immature in immatureSet:
		isMatch = False
		for nonself in nonselves:
		    if get_longest_match(int(nonself,2), int(immature,2)) >= threshold:
		    	isMatch = True
		    print(isMatch)
		    break
		if isMatch:
		    matureSet.write(immature)
		    print('written to mature set!')

	matureSet.close()
	nonselves.close()
	immatureSet.close()


if __name__ == '__main__':
    train_antibody('/Users/silvia/Documents/code/my/my_pcap/log/raw_immature_detector',\
    '/Users/silvia/Documents/code/my/my_pcap/log/intrusion_bin',\
    '/Users/silvia/Documents/code/my/my_pcap/log/mature_antibody',\
    10)
