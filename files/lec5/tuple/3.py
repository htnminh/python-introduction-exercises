def tup2num(tup):
    try:
        s = ''
        for ele in tup:
            s += str(ele)
        return int(s)
    except:
        return tup
def main():
    tup = (1, 23, 567)
    print(tup2num(tup))
