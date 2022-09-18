
<<<<<<< HEAD

# Todo(1): 생성자로 생성된 숫자들 리스트 생성
nature_numbers = set(range(1, 10000))
generate_numbers = set()

for i in range(1, 10001):
    for j in str(i):    #123
        i += int(j)    #j == "1", "2", "3"
    generate_numbers.add(i)

# Todo(2): 생성된 숫자들을 1~10000까지의 자연수 집합에서 제외
self_numbers = sorted(nature_numbers-generate_numbers)
for i in self_numbers:
    print(i)







#
# # Todo(1): 생성자로 생성된 숫자들 리스트 생성
# # n = 10, 10+ 1 + 0 = 11,  11 + 1 + 1 = 14, ....
# nature_number = set(range(1, 10000))
# generated_number = set()
#
# for i in range(1, 10001):
#     for j in str(i):    # i == 123
#         i += int(j)     # j = "1", "2", "3"
#     generated_number.add(i)
#
#
# # Todo(2): 생성된 숫자들을 1~10000까지의 자연수 집합에서 제외
# self_num = sorted(nature_number - generated_number)
# for i in self_num:
#     print(i)
=======
# d(n), (d(d(n))) ...


nature_number = set(range(1, 10001))
generate = set()


for i in nature_number:
    for j in str(i):
        i += int(j)
    generate.add(i)

self_num = sorted(nature_number - generate)
for output in self_num:
    print(output)
>>>>>>> ea6abfcd7ab5b401e3ad218d2f92b7af438d2843
