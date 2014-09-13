V = "aeiou"
C = "bdfgjkmnprstvz"

def vorud_chunk(a):
    assert(a >= 0 and a < 2**16)
    a, c5 = divmod(a, len(C))
    a, v4 = divmod(a, len(V))
    a, c3 = divmod(a, len(C))
    a, v2 = divmod(a, len(V))
    a, c1 = divmod(a, len(C))
    return C[c1] + V[v2] + C[c3] + V[v4] + C[c5]

def find_v(v): ret = V.find(v); assert(ret >= 0); return ret

def find_c(c): ret = C.find(c); assert(ret >= 0); return ret

def durov_chunk(s):
    assert(len(s) == 5)
    ret, n = 0, 1
    ret += find_c(s[4]) * n; n *= len(C)
    ret += find_v(s[3]) * n; n *= len(V)
    ret += find_c(s[2]) * n; n *= len(C)
    ret += find_v(s[1]) * n; n *= len(V)
    ret += find_c(s[0]) * n

    return ret

def vorud(a):
    assert(a > 0)
    if a < 2**16:
        return vorud_chunk(a)
    else:
        return "%s-%s" % (vorud(a // 2**16), vorud_chunk(a % 2**16))

def durov(s):
    if len(s) < 6:
        assert(len(s) == 5)
        return durov_chunk(s)
    return durov_chunk(s[-5:]) + 2**16 * durov(s[:-6])
