#Lists
#Lists -> epitrepetai na exoun oti data type thes esy px [1,2,"Kosmas",true,'c']. Mporeis na tis kaneis modify
#         kai episis epitrepontai dyplotypa [1,1,"Kosmas","Kosmas"]

prices =  [12, 23, 45]

print(prices)
print(prices[0])
print(prices[1])
print(prices[2])

print(prices[-1])
print(prices[-2])
print(prices[-3])

print("--------------------")
#append -> prosthetei mia thesi sto telos
prices.append("Kosmas")
print(prices)
#Insert -> eisago se mia thesi mia alli timi kai metatipizontai oi yparxontes

prices.insert(2,"Nikos")
print(prices)

#remove -> diagrafei ena sygkekrimeno stoixeio pou tha tou po (oxi thesi)
prices.insert(1,12)
print(prices)
prices.remove(12) #afairei to proto 12
#prices.remove(100)

print(prices)

#pop -> afairei to stoixeio se mia akrivos thesi

prices.pop(3)

print(prices)

#San na kaneis replace, change value :
prices[1] = 60

print(prices)

# Mikos listas

print(len(prices))

# Kathe string mporei na ginei lista:

leksi = "Christos"
lista = list(leksi)

print(lista)

# Lista episis kai to range

numbers = list(range(5))

print(numbers)

#Tuples (Pleiades)

#Tuples -> epitrepetai na exoun oti data type thes esy px [1,2,"Kosmas",true,'c'].Den Mporeis na tis kaneis modify!!!!
#         kai episis epitrepontai dyplotypa [1,1,"Kosmas","Kosmas"]

mytuple = (2,4.0,"Kosmass",'k')

print(mytuple)

# Arithimisi to idio

print(mytuple[0])
print(mytuple[-1])

#mytuple[1] = "Kosmas" !!!!Not possible because tuples cannot be modified

#Oi tuples den exoun entoles giati den ginontai modify (oxi delete, no replace, no insert)
#Ean thes na allaksis kati tin kaneis lista!!! kai meta ksana tuple

dummy_list = list(mytuple)
dummy_list[2] = "Kosmas"

modified_mytuple = tuple(dummy_list)

print(modified_mytuple)

#Dictionaries
#Einai san ta kanonika leksika -> kleidi - timi
lista = ["Nikos",23,True,"Male",34]
#Metafrazeis ti simainei i kathe timi
student_dict = {
    "name": "Nikos",
    "age": 23,
    "is_good_student": True,
    "sex": "Male",
    "vathmologia_Biologia": 34
}
print(student_dict)

#Theloume na prosthesoume tis 3 vathomologies stis kvantikes mixanikes 1,2,3

student_dict["vathmos_kvanto_3_teleautaies"] = [7,10,9]

print(student_dict)

student_dict["diagogi_glossa&mathimatika"] = ("artia","Metria") #Tuple epeidi den allazei pote

print(student_dict)

#Afairesi enos kleidiou mazi me tin timi

del student_dict["sex"]

print(student_dict)

#Pop afairei opos kai i del pano alla sou epistrefei kai tin timi pou afairese
onoma = student_dict.pop("name")
print(onoma)

#Allagi timis
student_dict["age"] = 18

print(student_dict)

print(student_dict["age"])

print("vathmologia_Biologia" in student_dict)
print(34 in student_dict.values())