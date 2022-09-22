all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):

    dict_all_students = {student: 0 for student in all_students}

    for student in present_students:
        dict_all_students.pop(student)

    print(dict_all_students)
    return


print(get_absent_student(all_students, present_students))