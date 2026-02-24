#def , print avg mathhmatvn + print mathhmata >=8

def askhsh1():
    grades = { #list(grades.keys()) -> ["Python","Finance","Statistics"], list(grades.values()) -> [8, 7, 9]
        "Python": 8,
        "Finance": 7,
        "Statistics": 9
    }

    vathmoi = list(grades.values())
    vathmoi_avg = sum(vathmoi) / len(vathmoi)
    print("mesos oros:", vathmoi_avg)

    mathhmata = list(grades.keys())
    #grades["Python"] -> 8
    for i in mathhmata:
        if grades[i] >= 8:
            print (i)



#na ektypvsv ton mathhth me ton megalytero vathmo
def askhsh2():
    students = {
        "Anna": 9,
        "Nikos": 6,
        "Maria": 1,
        "Giorgos": 7,
        "Eleni": 9
    }
    mathhtes = list(students.keys())
    vathmoi = list(students.values())

    local_max = -1
    for i in mathhtes:
        if students[i] >= local_max:
            local_max = students[i]

    for i in mathhtes:
        if students[i] == local_max:
            print (i)

    freq_ex = 0
    for i in mathhtes:
        if students[i] >= 8:
            freq_ex += 1
    print (freq_ex)

    freq_kalos = 0
    for i in mathhtes:
        if students[i] >= 5 and students[i] <= 7:
            freq_kalos += 1
    print (freq_kalos)

    freq_meh = 0
    for i in mathhtes:
        if students[i] < 5:
            freq_meh +=1
    print (freq_meh)

#3 listes

    list_ex = []
    list_kalos = []
    list_meh = []
    for i in mathhtes:
        if students[i] >= 8:
           list_ex.append(i)
        elif students[i] >= 5 and students[i] <= 7:
            list_kalos.append(i)
        elif students[i] < 5:
            list_meh.append(i)

    final_dict = {
        "excellent": list_ex,
        "kalos": list_kalos,
        "meh": list_meh
    }
    print(final_dict)

def askhsh3():
    students = {
        101: {"name": "Maria", "python": 8, "active": True},
        102: {"name": "Nikos", "python": 10, "active": False},
        103: {"name": "Eleni", "python": 9, "active": True}
    }
    initial_list = list(students.values())
    print(initial_list)
    for i in initial_list: #to i einai to dictionary
        if i["active"] == True:
            print(i["name"])

    # print onomata foithtvn poy einai aktive kai exoyn vathmo > 8
    print("/////////////")
    for i in initial_list:
        if i["active"] == True and i["python"] > 8:
            print(i["name"])




# grades["Python"] -> 8

askhsh3()
