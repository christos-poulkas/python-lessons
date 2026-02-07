#def x num (0-10) mean avg
#enothta 2

def vathmologia_mean():
    q_nums=int(input("how many numbers:"))
    z=[]
    for i in range(q_nums):
       x=float(input("insert number:"))
       if x >= 0 and x <= 10:
        z.append(x)
       else:
           print("error: num is not between 0 and 10")
           y=(float(input("insert number:")))
           z.append(y)
    mean_avg=sum(z)/len(z)
    print(mean_avg)
    return mean_avg


#askhsh 2: def input age, income if age >=18and <=65 and income >1500 and print

def hlikia_eisodhma():
    hlikia=int(input("insert hlikia:"))
    eisodhma=float(input("insert eisodhma:"))
    if hlikia >= 18 and hlikia <= 65 and eisodhma >1500:
        print("dikaiousai daneio")
    else:
        print("error")

#askhsh 3: user input int, check for odd and mult of 3 and print

def odd_and_mult_check():
    int_num=int(input("insert number:"))
    if int_num % 2 != 0 and int_num % 3 == 0:
        print("Ο αριθμός είναι περιττός και πολλαπλάσιο του 3!")
    else:
        print("Ο αριθμός ΔΕΝ πληροί τα κριτήρια.")


#askhsh 4:
def askhsh4():
    nums=input("dvse arithmous me komma")
    z=nums.split(",")
    z_premium=[]
    for i in z:
        z_premium.append(int(i))

#askhsh 5:
def askhsh5():
    kefalaio=float(input("insert kefalaio:"))
    epitokio=float(input("insert epitokio se dekadikh morfh:"))
    eth_daneiou=int(input("insert eth_daneiou:"))
    periodos_x=int(input("insert periodos_x:"))
    orio_asfalisis=float(input("insert orio_asfalisis:"))

    if epitokio == 0:
        print("kefalaio paramenei stathero:", kefalaio)
    else:
        for i in range(1, eth_daneiou+1):
            if i <= periodos_x:
                print("entos periodou xaritos:", kefalaio)
            else:
                kefalaio=kefalaio+(kefalaio*epitokio)
                print(f"to ananevmeno kefalaio isodynamei:, {kefalaio:.2f}, EUR")
                if kefalaio > orio_asfalisis:
                    print("To orio kseperasthke")
                    return 0

#askhsh 6:
def askhsh6():
    x = int(input("insert x:"))
    z=[]
    for i in range(1, x+1):
       z.append(i)
    print(sum(z))
