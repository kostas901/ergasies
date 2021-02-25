import random
x = int(input('ΕΙΣΑΓΕΤΕ ΤΟΝ ΟΡΟ ΑΚΟΛΟΥΘΙΑΣ FIBONACCI ΠΟΥ ΘΕΛΕΤΕ:'))


def Fibo(x):
    n1, n2 = 0, 1
    count = 0
    if x <= 0:
        print("ΠΑΡΑΚΑΛΩ ΕΙΣΑΓΕΤΕ ΘΕΤΙΚΟ ΑΚΕΡΑΙΟ")
    elif x == 1:

        return x-1

    else:
        while count < x-1:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return n1

c = Fibo(x)

print('Η ΤΙΜΗ ΤΟΥ ΟΡΟΥ ΠΟΥ ΕΠΙΛΕΞΑΤΕ ΕΙΝΑΙ:', c)
w = 0
if x == 2 or x == 1 or x == 3:
    print('ΤΟ', c, 'ΔΕΝ ΕΙΝΑΙ ΠΡΩΤΟΣ')
else:
    for i in range(0, 20):

        a = random.randint(1, c-1)

        if (a ** (c-1) - 1) % c == 0:
            w += 1
    if w == 20:
        print(c, 'ΕΙΝΑΙ ΠΡΩΤΟΣ')
    else:
        print(c, 'ΔΕΝ ΕΙΝΑΙ ΠΡΩΤΟΣ')