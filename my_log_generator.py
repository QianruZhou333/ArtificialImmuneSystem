# Author: Qianru Zhou
# Email: zhouqr333@126.com
# Magic, do not touch!!

import pcap
import dpkt
from dpkt.compat import compat_ord
import datetime
import socket
import random
import string
from my_intrusion_convertor import ip_addr


def write_to_log(data):
	""" Write to file
	"""
	with open('/Users/silvia/Documents/code/my/my_pcap/log/log_train', 'a') as f:
		f.write(data + '\n')


def reduce_duplicate_log():
	""" delete the duplicate strings in the log for efficiency 
	"""
	patterns = []
	with open('/Users/silvia/Documents/code/my/my_pcap/log', 'r') as f:
		for line in f.readlines():
			if line not in patterns:
			    patterns.append(line+'\n')

	with open('/Users/silvia/Documents/code/my/my_pcap/uniLog', 'w+') as out:
		for pattern in patterns:
		    out.write(pattern)


def to_binary(num, bitsNum):
	""" Convert a interger to a binary string
	Args: 
		num: the interger to be converted to binary
		bitsNum: the number of bits of the binary string
	Returns:
		the binary string
	"""
	return format(num, '0>'+bitsNum+'b')


def binary_str_generator():
	""" Generate a 168 bits binary string randomly
	"""
	# generate a 24 letters long string
	temp = ''.join(random.sample(string.ascii_letters + string.digits, 24 ))
	# convert it to binary, 1 letter = 7 bits
	return ''.join(format(ord(x), '0>7b') for x in temp)


def mac_addr(address):
	""" Convert a MAC address to a readable/printable string
	Args: 
		address: a MAC address in HEX form
	Returns:
		str: Printable/readable MAC address
	"""
#	print(':'.join('%02x' % compat_ord(b) for b in address))
	return ''.join('%s' % format(compat_ord(b), '0>8b') for b in address)


def inet_to_str(inet):
	""" Convert inet object to a string

	Args: 
		inet: inet network address
	Returns:
		str: Printable/readable IP address
	"""
	# first try ipv4 then ipv6
	try:
		return socket.inet_ntop(socket.AF_INET, inet)
	except ValueError:
		return socket.inet_ntop(socket.AF_INET6, inet)


def udp_iterator(pc):
	""" 
	pc is an pcap.pcap object which listens to the network, and returns an object when a packet goes by.
	"""
	for time,pkt in pc:
		eth = dpkt.ethernet.Ethernet(pkt)
		if eth.type == dpkt.ethernet.ETH_TYPE_IP:
		    ip = eth.data
		    # if the IP protocol is UDP, process it further
		    if ip.p == dpkt.ip.IP_PROTO_UDP :
			udp = ip.data
			yield( ip.src, udp.sport, ip.dst, udp.dport, udp.data )


if __name__ == '__main__':
	a = pcap.pcap('en0')
	a.setfilter('tcp')
	for time,data in a:
#	    print('timestamp is: ', str(datetime.datetime.utcfromtimestamp(time)))

	    # get the MAC address (src/dst), ethernet type
	    eth = dpkt.ethernet.Ethernet(data)
#	    print('ethernet frame in HEX: ', eth.src, eth.dst, eth.type)
#	    print('ethernet frame: ', mac_addr(eth.src), mac_addr(eth.dst), eth.type)

	    # Make sure the Ethernet data contains an IP packet
	    if not isinstance(eth.data, dpkt.ip.IP):
#		print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)
		continue

	    ip = eth.data # pull out src, dst, length, fragment info, TTL, and Protocol

	    do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
	    more_fragment = bool(ip.off & dpkt.ip.IP_MF)
	    fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

	    # print out the info
	    #print('IP: %s : %s -> %s : %d  (len=%d ttl=%d checksum=%d tos=%d DF=%d MF=%d offset=%d) \n' % \
	    #	( inet_to_str(ip.src),to_binary(ip.data.sport, '16'), inet_to_str(ip.dst), ip.data.dport, ip.len, ip.ttl,  
	    #   ip.sum, ip.tos, do_not_fragment, more_fragment, fragment_offset))

	    if not isinstance(ip.data, dpkt.icmp.ICMP): 
#	    	print('the binary string for all: %s ' % (mac_addr(eth.src) + to_binary(ip.data.sport, '16')
#	    	+ mac_addr(eth.dst) + to_binary(ip.data.dport, '16') + to_binary(ip.tos, '8') + to_binary(ip.sum, '16') 
#		+ to_binary(ip.len, '16')))

	    	write_to_log(ip_addr(inet_to_str(ip.src)) + to_binary(ip.data.sport, '16')
	    	+ ip_addr(inet_to_str(ip.dst)) + to_binary(ip.data.dport, '16') + to_binary(ip.tos, '8') + to_binary(ip.sum, '16') 
		+ to_binary(ip.len, '16'))
	    else:
		tempPort = '0000000000000000'
#	    	print('the binary string for all: %s ' % (mac_addr(eth.src) + tempPort + mac_addr(eth.dst) 
#		+ tempPort + to_binary(ip.tos, '8') + to_binary(ip.sum, '16') 
#		+ to_binary(ip.len, '16')))

	    	write_to_log(ip_addr(inet_to_str(ip.src)) + tempPort + ip_addr(inet_to_str(ip.dst)) + tempPort 
		+ to_binary(ip.tos, '8') + to_binary(ip.sum, '16') 
		+ to_binary(ip.len, '16'))

