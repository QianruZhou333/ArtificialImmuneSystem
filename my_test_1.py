import pcap
import dpkt
import socket

if __name__ == '__main__':
    a = pcap.pcap('en0')
    for time,data in a:
	eth = dpkt.ethernet.Ethernet(data)
        print('{:02X}'.format(eth.type))
	print('%s' % eth.data.__class__.__name__.lower())
	print('%s' % eth.data.data.dport)
	print('\n')
