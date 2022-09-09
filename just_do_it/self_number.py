
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