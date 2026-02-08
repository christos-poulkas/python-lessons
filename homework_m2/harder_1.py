# askhseis 2 diafaneias: python_exercises_gr_harder (1).pdf
# askhsh1

def askhsh1():
    print("Άσκηση 1: Ορίζει τις μεταβλητές a = 15 και b = 4 και εκτυπώνει το υπόλοιπο της διαίρεσής τους (a % b).")
    a = 15
    b = 4

    x = a % b
    print(x)
    return 0


def askhsh2():
    print("Άσκηση 2: Ορίζει τη μεταβλητή x = 3 και εκτυπώνει την τιμή της πέμπτης δύναμής της (x**5).")
    x = 3
    x_power = x ** 5
    print(x_power)
    return 0


def askhsh3():
    print("Άσκηση 3: Ζητά από τον χρήστη έναν αριθμό και εκτυπώνει αν είναι άρτιος ή περιττός.")
    x = int(input("dvse arithmo:"))
    if x % 2 == 0:
        print("o arithos:", x, "einai artios")
    else:
        print("o arithos:", x, "perittos")


def askhsh4():
    print("Άσκηση 4: Ζητά από τον χρήστη δύο αριθμούς και εκτυπώνει ποιος είναι ο μεγαλύτερος.")
    z = []
    for i in range(3):
        num = float(input("dvse arithmo:"))
        z.append(num)
        local_max = z[0]

    for n in z[1:]:
        if n > local_max:
            local_max = n

    print(local_max)


def askhsh5():
    print("Άσκηση 5: Χρησιμοποιεί βρόχο for για να εκτυπώσει τους αριθμούς από το 1 έως το 10.")
    for i in range(1, 11):
        print(i)


def askhsh6():
    print("Άσκηση 6: Χρησιμοποιεί βρόχο while για να εκτυπώσει τους πολλαπλασιασμούς του 5 μέχρι το 50.")
    x = 5
    i = 1
    y = 0
    while y < 50:
        y = x * i
        i += 1
        print(y)


def askhsh7():
    print("Άσκηση 7: Ορίζει λίστα [2, 4, 6, 8, 10] και εκτυπώνει το άθροισμα των στοιχείων της.")
    z = [2, 4, 6, 8, 10]
    print(sum(z))


def askhsh8():
    print(
        "Άσκηση 8: Δημιουργεί συνάρτηση που δέχεται ακέραιο και επιστρέφει το τετράγωνό του, εκτυπώνοντας το αποτέλεσμα για την τιμή 7.")
    akeraios = int(input("dvse akeraio:"))
    print("to tetragvno tou", akeraios, "einai to:", akeraios ** 2)

##########################################################
#DISPATCHER
dispatch_archive = {
    1: askhsh1,
    2: askhsh2,
    3: askhsh3,
    4: askhsh4,
    5: askhsh5,
    6: askhsh6,
    8: askhsh8
}

askhsh = int(input("Ποιά άσκηση θέλεις να καλέσεις (ΒΑΛΕ ΜΟΝΟ ΑΡΙΘΜΟ): "))

if askhsh in dispatch_archive:
    dispatch_archive[askhsh]()
else:
    print("Δεν υπάρχει τέτοια άσκηση")
##########################################################
















