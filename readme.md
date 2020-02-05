# ISO Messege Script

This is a simple ISO Message tester.



### Running

This app requires Python v3+ to run.
See [Download python](https://www.python.org/downloads/)

Change directory to the project root folder

```sh
$ cd path/to/project/root
$ python ISOTest.py
```



### Development

Want to customize the code? Great!

Open your ISOTest.py and change the following code lines according to your need.

```sh
# Turn debug logs on off from here
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
```

To change the ISO Type bit array to BigEndian or Not:
```sh
# BigEndian
iso.getNetworkISO(True)

# Not BigEndian
iso.getNetworkISO()

```

(optional) To customize the ISO Messege validation and preferences:
Open ISO8583.py file and customize the _BITS_VALUE_TYPE entries

ex:
```sh
_BITS_VALUE_TYPE[2] = ['2', 'Primary account number (PAN)', 'LL', 19, 'n']

```

