#def x input nums -> list

def test_askhsh1 ():
    z=[]
    q_num = int(input("posous arithmous theleis?:"))
    for i in range (q_num):
        num = float(input("vale arithmo"))
        z.append(num)
    # z = [1,2,3,4]
    print(z[0]) #->1
    print(z[-1]) #->4
    z.insert(0, 100) #-> [100,1,2,3,4]
    print(len(z)) # -> 5
    z.pop(1) #-> [100,2,3,4]
    if 100 in z:
        z.remove(100) #-> [2,3,4]
    print(z)

test_askhsh1()