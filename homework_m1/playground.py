n = int(input("how many numbers: "))
z = []

for i in range(n):
    num = float(input("insert a number: "))
    z.append(num)

current_max = z[0]

for value in z[1:]:
    if value > current_max:
        current_max = value

print("max:", current_max)