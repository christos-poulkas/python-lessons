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


#######selida 7, dialeksh 3 LATHOS H POP######

#askhsh2: zhtav apo ton xrhsh n mathhmata vathmologia > dvse mathhma kai vathmologia

def test_askhsh2 ():
    archeio = {}
    q_math = int(input("posa mathhmata?:"))
    for i in range (q_math):
        titlos = input("vale mathhma:")
        vathmos = int(input("vale vathmo:"))
        archeio[titlos] = vathmos
    print(archeio)
    vathmoi_list=archeio.values()
    print(vathmoi_list)
    new_list = list(vathmoi_list)
    print(new_list)

    local_max = 8
    for i in new_list:
        if i > local_max:
            print("kalos mathhths")
            return 0
    print("kakos mathhths")
#ean kapoios apo tous vathmous >8, na kanv print kalos h kakos



test_askhsh2()