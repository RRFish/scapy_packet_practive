from scapy.all import *

connreq = sniff(count=100)
print("connreq", connreq)