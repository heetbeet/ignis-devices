import minimalmodbus
import util
import serial

minimalmodbus.BAUDRATE = 9600
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = False


def get_instruments(device_ids):
    definative_com = None
    instances = {}

    for i in device_ids:
        comrange = range(1,11)
        if definative_com is not None:
            comrange = [definative_com]

        for com in comrange:
            dev = None
            try:
                dev = minimalmodbus.Instrument(f"COM{com}", i)
                dev.read_registers(512,8)
                instances[i] = dev
                definative_com = i
            except (serial.serialutil.SerialException, minimalmodbus.NoResponseError, minimalmodbus.InvalidResponseError):
                del dev
                pass

    not_found = set(device_ids).difference(instances)
    if not_found:
        raise ConnectionError(f"Could not connect to Devices: {list(not_found)}")

    return instances


def write_to_inst(ins, bits):
    try:
        ins.write_register(320, util.bits2int(bits[::-1]))
        return True
    except OSError:
        return False


'''
class SIODevice:
    """
    This module reads values from a cheap Preciso scale through RS232. It opens a background thread to continuously
    reads values from the serial device, with the last value being accessible through the mass property. If the device
    reads 10 faulty values in a row the process crashes.
    """
    def __init__(self, device_ids):
        self.devices = get_instruments()
'''

if __name__ == "__main__":
    dev1 = get_instruments([1,2,3])[2]
    dev1.read_registers(512, 8)