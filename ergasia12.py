f = open("two.txt", "r")
a1 = f.read()
len(a1)
f.close()
with open("two.txt", "r") as f:

    ch = []
    list = []
    for i in range(0, len(a1)):
        ch.append(f.read(1))
        a = ord(ch[i])
        b = 128 - a
        list.append(b.to_bytes((b.bit_length() + 7) // 8, 'big').decode())
    list.reverse()
    print(''.join(list))


f.close()