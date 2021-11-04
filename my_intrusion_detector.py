# Author: Qianru Zhou
# Email: zhouqr333@126.com
# Magic, do not touch!!

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


def detect_intrusion(matureDir, trafficDir, intrusionDir, threshold):
	""" match the mature antibodies with traffic, if match,
	report the intrusion.
	Args:
		matureDir: the absolute directory of the mature antibodies
		trafficDir: the absolute directory of the traffic
		threshold: the threshold of the match
	"""
	antibodies = open(matureDir, 'r+')
	trafficSet = open(trafficDir, 'r')
	intrusion = open(intrusionDir, 'a')

	for traffic in trafficSet:
		isSelf = True
		for antibody in antibodies:
		    if get_longest_match(int(antibody,2), int(traffic,2)) >= threshold:
		    	isSelf = False
		    print(isSelf)
		    break
		if not isSelf:
		    intrusion.write(traffic)
		    print('written to detect result!')

	intrusion.close()
	trafficSet.close()
	antibodies.close()


if __name__ == '__main__':
    detect_intrusion('/Users/silvia/Documents/code/my/my_pcap/log/mature_antibody_1',\
    '/Users/silvia/Documents/code/my/my_pcap/log/intrusion_2',\
    '/Users/silvia/Documents/code/my/my_pcap/log/detect_result',\
    10)
