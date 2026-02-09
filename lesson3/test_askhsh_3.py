#def x input nums -> list

def test_askhsh1 ():
    z=[]
    q_num = int(input("posous arithmous theleis?:"))
    for i in range (q_num):
        num = float(input("vale arithmo"))
        z.append(num)
    print(z[0])
    print(z[-1])
    z.insert(0, 100)
    print(len(z))
    z.pop(1)
    if 100 in z:
        z.remove(100)
    print(z)

test_askhsh1()