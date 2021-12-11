from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int

def test(messages):
    """ decoder for RPM messages """
    print(messages)
    d = messages[0].data # only operate on a single message
    print(d)
    d = d[2:] # chop off mode and PID bytes
    print(d)
    v = bytes_to_int(d) / 4.0  # helper function for converting byte arrays to ints
    print(v)
    return (v) # construct a Pint Quantity

c = OBDCommand("Test",           # name
               "Engine Test",    # description
               b"0100",          # command
               30,               # number of return bytes to expect
               test,             # decoding function
               #ECU.ENGINE, \     # (optional) ECU filter
               True)


import obd

o = obd.OBD()

# use the `force` parameter when querying
resp = o.query(c, force=True)

print(resp.value)