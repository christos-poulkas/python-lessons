#python-exercises_gr_if_else (1).pdf

##step 1
x = int(input("insert int num:"))
if x < 0:
    print("num is negative")
elif x == 0:
    print("num is zero")
else:
    print("num is positive")

##step 2
z=[]

q_num=int(input("How many numbers do you want?:"))

for i in range(q_num):
    num=float(input("insert a number:"))
    z.append(num)

local_max=z[0]

for i in z[1:]:
    if i > local_max:
        local_max=i

print ("the biggest number is ",local_max)

##step 3
num100 = int(input("insert num from 0 to 100:"))
if num100 < 25:
    print("Ανεπαρκώς")
elif num100 >= 25 and num100 <= 50:
    print("Καλά")
elif num100 >= 50 and num100 <= 75:
    print("Πολύ Καλά")
elif num100 >= 75:
    print("Άριστα")
else:
    print("Μη έγκυρη τιμή. Εισέγαγε αριθμό μεταξύ του 0-100")

##step 4
age = int(input("insert age:"))
if age < 18:
    print("Ανήλικος")
else:
    print("Ενήλικας")

##step 5

x5 = int(input("insert a number:"))
if x5%3==0 and x5%5==0:
    print(x5, "is perfectly divisible by 3 and 5")
else:
    print(x5, "is NOT perfectly divisible by 3 and 5")

##step 6
year=int(input("insert year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print(year, "is perfectly divisible by 4 and 5")
else:
    print(year, "is NOT perfectly divisible by 4 and 5")

##step 7
correct_password=("python123")
password=input("input password: ")

if password==correct_password:
    print("Access Granted.")
else:
    print("Access Denied.")

##step 8
z8 = []

print("--Insert three numbers below--")
for i in range(3):
    num = float(input("Insert a number:"))
    z8.append(num)

local_max8 = z8[0]

for i in z8[1:]:
    if i > z8[0]:
        local_max8 = i

print("The biggest among the three numbers is:", local_max8)

#Αρχείο: python_exercises_gr_if_else(1).pdf
#Ολοκληρώθηκε η διαφάνεια ασκήσεων


