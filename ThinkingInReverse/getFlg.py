flag = []
lst  = list('rv')

flag.append(lst[0])
flag.append(str(int(3)))
flag.append(lst[1])
flag.append('_1s_')
flag.append(chr(102))
flag.append(str(int(0)))
flag.append(chr(110))
flag = ''.join(flag)
flag = flag[::-1]

print(flag)