import struct

V = "aeiou"
C = "bdfgjkmnprstvz"

def vorud_chunk(x):
    assert(x >= 0 and x < len(V)**2 * len(C)**3)
    x, c5 = divmod(x, len(C))
    x, v4 = divmod(x, len(V))
    x, c3 = divmod(x, len(C))
    x, v2 = divmod(x, len(V))
    x, c1 = divmod(x, len(C))
    return C[c1] + V[v2] + C[c3] + V[v4] + C[c5]

def find_v(v): ret = V.find(v); assert(ret >= 0); return ret

def find_c(c): ret = C.find(c); assert(ret >= 0); return ret

def durov_chunk(s):
    assert(len(s) == 5)
    x, n = 0, 1
    x += find_c(s[4]) * n; n *= len(C)
    x += find_v(s[3]) * n; n *= len(V)
    x += find_c(s[2]) * n; n *= len(C)
    x += find_v(s[1]) * n; n *= len(V)
    x += find_c(s[0]) * n
    return x

def is_valid_chunk(s):
    return len(s) == 5 and C.find(s[0]) >= 0 and V.find(s[1]) >= 0 \
        and C.find(s[2]) >= 0 and V.find(s[3]) >= 0 and C.find(s[4]) >= 0

def vorud(b):
    """Encode bytes-like data to a Vorud string."""
    ret = []
    while True:
        if len(b) == 0: return "-".join(ret)
        if len(b) == 1:
            # Stream ends after 1 byte, do special encoding in the chunk.
            ret.append(vorud_chunk(2**16 + b[0]))
        else:
            ret.append(vorud_chunk(b[0] * 256 + b[1]))
        b = b[2:]


def durov(s):
    """Decode a Vorud string into bytes."""
    ret = []
    stream_ended = False
    while True:
        if len(s) == 0: return bytes(ret)
        if stream_ended: raise TypeError("Vorud data after stream end marker")
        chunk = s[:5].lower()
        if not is_valid_chunk(chunk):
            raise TypeError("Invalid Vorud chunk: '%s'" % chunk)
        val = durov_chunk(chunk)
        if val < 2**16:
            # Regular two-byte chunk.
            ret.append(val // 256)
            ret.append(val % 256)
        elif val < 2**16 + 256:
            # Single byte at data end.
            stream_ended = True
            ret.append(val - 2**16)
        else:
            raise TypeError("Unused Vorud encoding: '%x'" % val)
        s = s[6:]

def vorud_32(i):
    """Standard big-endian encoding for 32-bit integers"""
    b = struct.pack(">I", i)
    return vorud(b)

def durov_32(s):
    """Standard big-endian decoding for 32-bit integers"""
    return struct.unpack(">I", durov(s))[0]

if __name__ == '__main__':
    for i in range(2**16):
        assert(durov_32(vorud_32(i)) == i)
