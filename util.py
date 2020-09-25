def str2bits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def bits2str(bits):
    bitgroups = [bits[i:i+8] for i in range(0,len(bits),8)]
    int_list = []
    for bit in bitgroups:
        int_list.append(0)
        for i, val in enumerate(bit[::-1]):
            int_list[-1] += (2**(i))*bool(val)
    str_out = ''.join([chr(i) for i in int_list])
    return str_out

def bits2int(bits):
    out_int = 0
    for i, val in enumerate(bits[::-1]):
        out_int += (2**(i))*bool(val)
    return out_int