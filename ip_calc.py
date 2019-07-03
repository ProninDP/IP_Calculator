#IP_adress = input('введите IP-сети: ')
#from sys import argv
#IP_adress = argv[1:]

IP_adress = '192.168.100.10/24'
IP_adress = IP_adress.split('/', -1)
mask = IP_adress[1]
print(IP_adress)
ip = list(IP_adress[0].split('.'))
ip0 = int(ip[0])
ip1 = int(ip[1])
ip2 = int(ip[2])
ip3 = int(ip[3])
ip_template = '''
    ...: IP address:
    ...: {0:<8} {1:<8} {2:<8} {3:<8}
    ...: {0:08b} {1:08b} {2:08b} {3:08b}'''
print(ip_template.format(ip0,ip1,ip2,ip3))
IP_mask = ['0','0','0','0']
for i in range(int(mask)+1):
  if i <= 8:
    a = 2**(8-i)
    IP_mask[0] = 255 - a + 1
  elif i >= 9:
    if i <= 16:
      b = 2**(16-i)
      IP_mask[1] = 255 - b + 1
    elif i >= 17:
      if i <= 24:
        c = 2**(24-i)
        IP_mask[2] = 255 - c + 1
      elif i >= 25:
        d = 2**(32-i)
        IP_mask[3] = 255 - d + 1
#wildcard:
w0 = 255 - int(IP_mask[0])
w1 = 255 - int(IP_mask[1])
w2 = 255 - int(IP_mask[2])
w3 = 255 - int(IP_mask[3])
#IP mask:
m0 = int(IP_mask[0])
m1 = int(IP_mask[1])
m2 = int(IP_mask[2])
m3 = int(IP_mask[3])
#network IP address:
n0 = ip0 & m0
n1 = ip1 & m1
n2 = ip2 & m2
n3 = ip3 & m3
#broadcast:
b0 = ip0 | w0
b1 = ip1 | w1
b2 = ip2 | w2
b3 = ip3 | w3

network_template = '''
    ...: network IP address:
    ...: {0:<8} {1:<8} {2:<8} {3:<8}
    ...: {0:08b} {1:08b} {2:08b} {3:08b}'''
print(network_template.format(n0,n1,n2,n3))
mask_template = '''
    ...: IP mask: /{4}
    ...: {0:<8} {1:<8} {2:<8} {3:<8}
    ...: {0:08b} {1:08b} {2:08b} {3:08b}'''
print(mask_template.format(m0,m1,m2,m3,mask))
wildcard_template = '''
    ...: wildcard:
    ...: {0:<8} {1:<8} {2:<8} {3:<8}
    ...: {0:08b} {1:08b} {2:08b} {3:08b}'''
print(wildcard_template.format(w0,w1,w2,w3))
broadcast_template = '''
    ...: broadcast:
    ...: {0:<8} {1:<8} {2:<8} {3:<8}
    ...: {0:08b} {1:08b} {2:08b} {3:08b}'''
print(broadcast_template.format(b0,b1,b2,b3))

hosts = 2**(32-int(mask))-2
hosts_template = '''
    ...: hosts:{0}
    ...: min_IP:
    ...: {1:<8} {2:<8} {3:<8} {4:<8}
    ...: {1:08b} {2:08b} {3:08b} {4:08b}
    ...: max_IP:
    ...: {5:<8} {6:<8} {7:<8} {8:<8}
    ...: {5:08b} {6:08b} {7:08b} {8:08b}'''
print(hosts_template.format(hosts,n0,n1,n2,n3+1,b0,b1,b2,b3-1))