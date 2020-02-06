from ISO8583.ISO8583 import ISO8583
from ISO8583.ISOErrors import *

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



try:
    message = iso.getNetworkISO()
    print('Sending ... %s' % message)
    ans = message
    ans = "02003020058020C012040000000000000010000015690051001100325236700000009571D2307226198551153030303038202020303030303520202020202020202020043CA9C4CD634BF301505F2A0201445F340100820218008407A0000000041010950580200480009A031809069C01009F02060000000010009F090200029F10120110A00001220000000000000000000000FF9F1A0201449F1E08324B3237383131349F26088D6E9312DC6A29B89F2701809F3303E0F8C89F34034203009F3501229F360200359F3704F24634FC9F41030015699F5301529F03060000000000000006303031353639004C60000000110210303801000E80020000000000000000100000156912080809060011303031353639202020202020383939393034303030303030382020200012910AEBCD0881B2BDDA540012"
    print("\nInput ASCII |%s|" % ans)
    isoAns = ISO8583()
    isoAns.setNetworkISO(ans)
    v1 = isoAns.getBitsAndValues()
    print(v1)

    for v in v1:
        print('Bit %s of type %s with value = %s' % (v['bit'], v['type'], v['value']))

    print(isoAns.getMTI())
    if isoAns.getMTI() == '0810':
        print("\tThat's great !!! The server understand my message !!!")
    else:
        print("The server dosen't understand my message!")

except InvalidIso8583 as ii:
    print(ii)

sys.exit(1)
