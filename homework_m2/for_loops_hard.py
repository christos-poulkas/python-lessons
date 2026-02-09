# askhsh1
def askhsh1():
    z_num = [9, 16, 25, 36]
    z_squareroot = [x ** 0.5 for x in z_num]

    print(z_squareroot)


# askhsh2

def askhsh2():
    sentence = input("grapse protash:")
    freq = {}
    for c in sentence:
        if c.isalpha():
            c = c.lower()
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
    print(freq)

askhsh2()