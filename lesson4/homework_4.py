students = {
    101: {
        "name": "Maria",
        "lessons": {
            "python": 8,
            "math": 9,
            "databases": 7
        },
        "active": True,
        "year": 2
    },
    102: {
        "name": "Nikos",
        "lessons": {
            "python": 6,
            "math": 5,
            "databases": 6
        },
        "active": False,
        "year": 1
    },
    103: {
        "name": "Eleni",
        "lessons": {
            "python": 9,
            "math": 8,
            "databases": 9
        },
        "active": True,
        "year": 3
    },
    104: {
        "name": "Giorgos",
        "lessons": {
            "python": 7,
            "math": 6,
            "databases": 5
        },
        "active": True,
        "year": 2
    },
    105: {
        "name": "Anna",
        "lessons": {
            "python": 10,
            "math": 9,
            "databases": 8
        },
        "active": True,
        "year": 4
    },
    106: {
        "name": "Kostas",
        "lessons": {
            "python": 5,
            "math": 6,
            "databases": 4
        },
        "active": False,
        "year": 1
    }
}
names_lessons_grades_extract = {}

for student_id, data in students.items():
    name = data["name"]
    lessons = data["lessons"]

    names_lessons_grades_extract[name] = lessons #1. kanei vivliothiki tvn onomatvn kai mathhmatvn kai vatmhologivn

print("Λεξικό με τα μαθήματα και βαθμούς:", names_lessons_grades_extract)

mean_avg_dict = {}
for name, grades in names_lessons_grades_extract.items():
    mean = sum(grades.values())/len(grades)
    mean_avg_dict[name] = mean
print("Ακολουθεί λεξικό με τους μέσους όρους των μαθητών:", mean_avg_dict)



#1. ftiakse ena dictionary me onoma tou mathhth kai th vathmologia tou sta mathhmata (key: onoma kai value: vathmologia)
#2. ftiakse ena dictionary me onoma tou mathhth kai th mesh vathmologia tou se ola ta mathhamata