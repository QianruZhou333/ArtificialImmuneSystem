# author: Qianru Zhou (zhouqr333@126.com)

import pcap
import dpkt
from dpkt.compat import compat_ord
import datetime
import socket


def mac_addr(address):
	""" Convert a MAC address to a readable/printable string

	Args: 
		address: a MAC address in HEX form
	Returns:
		str: Printable/readable MAC address
	"""
	print(':'.join('%02x' % compat_ord(b) for b in address))
	return ':'.join('%s' % format(compat_ord(b), '0>8b') for b in address)


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
	#a.setfilter('tcp')
	for time,data in a:
	    print('timestamp is: ', str(datetime.datetime.utcfromtimestamp(time)))

	    # get the MAC address (src/dst), ethernet type
	    eth = dpkt.ethernet.Ethernet(data)
	    print('ethernet frame in HEX: ', eth.src, eth.dst, eth.type)
	    print('ethernet frame: ', mac_addr(eth.src), mac_addr(eth.dst), eth.type)

	    # Make sure the Ethernet data contains an IP packet
	    if not isinstance(eth.data, dpkt.ip.IP):
		print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)
		continue

	    ip = eth.data # pull out src, dst, length, fragment info, TTL, and Protocol

	    do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
	    more_fragment = bool(ip.off & dpkt.ip.IP_MF)
	    fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

	    # print out the info
	    print('IP: %s : %s -> %s : %s  (len=%d ttl=%d checksum=%d tos=%d DF=%d MF=%d offset=%d) \n' % \
	    	( inet_to_str(ip.src), ip.data.sport, inet_to_str(ip.dst), ip.data.dport, ip.len, ip.ttl, ip.sum, ip.tos, do_not_fragment, more_fragment, fragment_offset))



