SR = []

def MEGAALGORITM3000(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def ULTRAALGORITM9000(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def GLADIATOR(x, y):
    for i in range(len(SR)):
        rs = []
        for j in range(len(SR[i])):
            rs.append(y[SR[i][j]])
        l = 0
        for k in range(len(rs)):
            if rs[k] == 1:
                l += 1
        if l % 2 == 0:
            l = 0
        else:
            l = 1
        x.append(l)

s = input("Введите строку: ")

res = MEGAALGORITM3000(s)
#res = ''.join(format(ord(i), 'b') for i in s)
b = [c for c in res]
for i in range(len(b)):
    b[i] = int(b[i])

print(s)
print("Строка в двоичном коде: " + str(res))

m = [0, 0, 0]
p = []

n = int(input("Введите кол-во сумматоров: "))
#if n != 1 or n != 2 or n != 3:
 #   print("Вас засекла проверка на дурака")
  #  exit()
#else:
 #   n = int(n)
n1 = n

if n == 1:
    d = []
    for i in range(n):
        a = input("Введите регистры для первого суммматора")
        a.split(" ")
        d = a.split(" ")
        d = list(d)
    for i in range(len(d)):
        d[i] = int(d[i])
    print(d)

    for i in range(len(res)):
        m.insert(0, res[i])
        h = int(m[d[0] - 1])
        h_ = int(m[d[1] - 1])
        l = (h + h_) % 2
        p.append(l)
    print(p)



if n == 2:
    d = []
    a = input("Введите регистры для первого сумматора")
    a.split(" ")
    d = a.split(" ")
    d = list(d)
    for i in range(len(d)):
        d[i] = int(d[i])
    print(d)
    a_ = input("Введите регистры для второго сумматора")
    a_.split(" ")
    d_ = a_.split(" ")
    d_ = list(d_)
    for i in range(len(d)):
        d_[i] = int(d_[i])
    print(d_)
    for i in range(len(res)):
        m.insert(0, res[i])
        h = int(m[d[0] - 1])
        h_ = int(m[d[1] - 1])
        l = (h + h_) % 2
        p.append(l)
        r = int(m[d_[0] - 1])
        r_ = int(m[d_[1] - 1])
        f = (r + r_) % 2
        p.append(f)
    print(p)


if n == 3:
    d = []
    a = input("Введите регистры для первого сумматора")
    a.split(" ")
    d = a.split(" ")
    d = list(d)
    for i in range(len(d)):
        d[i] = int(d[i])
    print(d)
    a1 = input("Введите регистры для второго сумматора")
    a1.split(" ")
    d1 = a1.split(" ")
    d1 = list(d1)
    for i in range(len(d)):
        d1[i] = int(d1[i])
    print(d1)
    a2 = input("Введите регистры для третьего сумматора")
    a2.split(" ")
    d2 = a2.split(" ")
    d2 = list(d2)
    for i in range(len(d)):
        d2[i] = int(d2[i])
    print(d2)
    for i in range(len(res)):
        m.insert(0, res[i])
        h = int(m[d[0] - 1])
        h_ = int(m[d[1] - 1])
        l = (h + h_) % 2
        p.append(l)
        r = int(m[d1[0] - 1])
        r_ = int(m[d1[1] - 1])
        f = (r + r_) % 2
        p.append(f)
        r1 = int(m[d2[0] - 1])
        r2 = int(m[d2[1] - 1])
        f1 = (r1 + r2) % 2
        p.append(f1)
    print(p)

P = ""
for i in range(len(p)):
    P += str(p[i])

INFSL = []
n2 = int(n)
while len(P) != 0:
    ck = ""
    for i in range(n):
        ck += P[0]
        P = P.replace(P[0], "", 1)

    reg1 = []
    for i in range(len(m)):
        reg1.append(m[i])
    reg1.insert(0, 0)
    del reg1[-1]

    rez1 = []
    GLADIATOR(rez1, reg1)

    REZ1 = ""
    for i in range(len(rez1)):
        REZ1 += str(rez1[i])


    reg2 = []
    for i in range(len(m)):
        reg2.append(m[i])
    reg2.insert(0, 1)
    del reg2[-1]

    rez2 = []
    GLADIATOR(rez2, reg2)

    REZ2 = ""
    for i in range(len(rez2)):
        REZ2 += str(rez2[i])

    if REZ1 == ck and REZ2 != ck:
        INFSL.append(0)
        reg = []
        for i in range(len(reg1)):
            reg.append(reg1[i])

    elif REZ1 != ck and REZ2 == ck:
        INFSL.append(1)
        reg = []
        for i in range(len(reg2)):
            reg.append(reg2[i])

    elif len(P) == 0:
        INFSL.append(0)

IS = ""
for i in range(len(res)):
    IS += str(res[i])
IS = IS[:-n1]
print("Декодированная строка в двоичном коде: ", IS)
print(ULTRAALGORITM9000(res))