from ISO8583.ISO8583 import ISO8583
from ISO8583.ISOErrors import *

import socket
import sys
import time

iso = ISO8583(debug=True);
iso.setMTI('0200')
iso.setBit(2, '6526000060004')
iso.setBit(3, '210000')
iso.setBit(4, '000001000000')
iso.setBit(7, '0913001205')
iso.setBit(11, '211085')
iso.setBit(12, '180913')
iso.setBit(17, '20180913001205')
iso.setBit(32, '00000581816')
iso.setBit(37, '211085180913')
iso.setBit(41, 'CDMDEH01')
iso.setBit(49, '144')
iso.setBit(102, '6526000060004')
iso.setBit(103, '0010281329001')
message = iso.getNetworkISO()
# litMsg = iso.getNetworkISO(bigEndian=False)
print(message)

serverIP = "192.168.0.103"
serverPort = 8583

s = None
for res in socket.getaddrinfo(serverIP, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print("Create Socket")
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        print("Socket Error:"+msg)

        s = None
        continue
    try:
        print("Connect Socket")

        s.connect(sa)
    except socket.error as msg:
        print("Socket Error:"+msg)

        s.close()
        s = None
        continue
    break

if s is None:
    print('Could not connect :(')
    sys.exit(1)

try:
    message = iso.getNetworkISO()
    s.send(message)
    print('Sending ... %s' % message)
    ans = s.recv(2048)
    print("\nInput ASCII |%s|" % ans)
    isoAns = ISO8583()
    isoAns.setNetworkISO(ans)
    v1 = isoAns.getBitsAndValues()
    for v in v1:
        print('Bit %s of type %s with value = %s' % (v['bit'], v['type'], v['value']))

    if isoAns.getMTI() == '0810':
        print("\tThat's great !!! The server understand my message !!!")
    else:
        print("The server dosen't understand my message!")

except InvalidIso8583 as ii:
    print(ii)

s.close()
sys.exit(1)
