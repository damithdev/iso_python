from ISO8583.ISO8583 import ISO8583
from ISO8583.ISOErrors import *

import socket
import sys
import time

serverIP = "192.168.0.103"
serverPort = 8583



# def testTransactionunkn():
#     iso = ISO8583(debug=True)
#     iso.setMTI('0200')
#     iso.setBit(3, '000000')
#     iso.setBit(4, '000000001000')
#     iso.setBit(11, '001569')
#     iso.setBit(22, '0051')
#     iso.setBit(24, '0011')
#     iso.setBit(25, '00')
#     iso.setBit(35, '5236700000009571D230722619855115')
#     iso.setBit(41, '00008   ')
#     iso.setBit(42, '00005          ')
#     iso.setBit(52, '043CA9C4CD634BF3')
#     iso.setBit(55, '05F2A0201445F340100820218008407A0000000041010950580200480009A031809069C01009F02060000000010009F090200029F10120110A00001220000000000000000000000FF9F1A0201449F1E08324B3237383131349F26088D6E9312DC6A29B89F2701809F3303E0F8C89F34034203009F3501229F360200359F3704F24634FC9F41030015699F5301529F03060000000000000006303031353639')
#     iso.setBit(62, '004C60000000110210303801000E80020000000000000000100000156912080809060011303031353639202020202020383939393034303030303030382020200012910AEBCD0881B2BDDA540012')
#     # iso.setBit(61, '01')
#     # iso.setBit(62, '998877')
#     # iso.setBit(63, '0022001031303120202031202020000833313030414243')
#
#     message = iso.getNetworkISO()
#
#
#     return message

def sampleTransaction():
    iso = ISO8583(debug=True)
    iso.setMTI('0220')
    iso.setBit(3, '020000')
    iso.setBit(4, '000000001500')
    iso.setBit(11, '006499')
    iso.setBit(22, '0022')
    iso.setBit(24, '0003')
    iso.setBit(25, '00')
    iso.setBit(35, '371449635398431D891289017666F')
    iso.setBit(41, '70000000',True)
    iso.setBit(42, '012345678900000',True)
    iso.setBit(54, '000000000500',True)
    iso.setBit(61, '01      ',True)
    iso.setBit(62, '998877',True)
    iso.setBit(63, '101   1   |3100ABCD',True)

    message = iso.getNetworkISO()


    return message

def testTransaction():
    iso = ISO8583(debug=True)
    iso.setMTI('0220')
    iso.setBit(3, '99000x')
    iso.setBit(24, '0003')
    iso.setBit(41, '70000000',True)

    message = iso.getNetworkISO()


    return message

def exitFunction():
    return "0"


def sendMessege(message):
    s = None
    for res in socket.getaddrinfo(serverIP, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            print("Create Socket")
            s = socket.socket(af, socktype, proto)
        except socket.error as msg:
            print("Socket Error:" + msg)

            s = None
            continue
        try:
            print("Connect Socket")

            s.connect(sa)
        except socket.error as msg:
            print("Socket Error:" + msg)

            s.close()
            s = None
            continue
        break

    if s is None:
        print('Could not connect :(')
        return

    try:
        # message = iso.getNetworkISO()
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
            print("The server doesn't understand my message!")

    except InvalidIso8583 as ii:
        print(ii)

    s.close()

def getHeader():
    # HDLC poll address
    field1 = "00"

    # LC control byte
    field2 = "F0"

    # TPDU Id
    field3 = "60"

    # Destination address
    field4 = "0011"

    # Originator address
    field5 = "0000"

    header_val = field1+field2+field3+field4+field5
    return header_val

def getHeader2():
    # HDLC poll address
    field1 = "30"

    # LC control byte
    field2 = "00"

    # TPDU Id
    field3 = "60"

    # Destination address
    field4 = "0003"

    # Originator address
    field5 = "8100"

    header_val = field1+field2+field3+field4+field5
    return header_val

while True:
    switcher = {
        0: exitFunction,
        1: sampleTransaction,
        2: testTransaction,

    }
    print("===========================================================================\n")
    print("Select a message type to send \n")
    print("0.Exit")
    print("1.Sample Message")
    print("2.Test Message 2\n")

    try:
        arg = input()
        print("Selection:"+arg)
        func = switcher.get(int(arg), lambda: "INVALID_SELECTION")

        if func() == "0":
            break

        if func() == "INVALID_SELECTION":
            print(func())
            continue



        iso_msg = func()
        header = getHeader()
        print(header+iso_msg)
        # sendMessege(header+iso_msg)
    except Exception as e:
        print("Something Went Wrong")
        print('Exception: '+str(e))

# litMsg = iso.getNetworkISO(bigEndian=False)
# print(message)

print("Good Bye!")
sys.exit(1)

# iso = ISO8583(debug=True)
# iso.setMTI('0200')
# iso.setBit(2, '6526000060004')
# iso.setBit(3, '210000')
# iso.setBit(4, '000001000000')
# iso.setBit(7, '0913001205')
# iso.setBit(11, '211085')
# iso.setBit(12, '180913')
# iso.setBit(17, '20180913001205')
# iso.setBit(32, '00000581816')
# iso.setBit(37, '211085180913')
# iso.setBit(41, 'CDMDEH01')
# iso.setBit(49, '144')
# iso.setBit(102, '6526000060004')
# iso.setBit(103, '0010281329001')
# message = iso.getNetworkISO()
