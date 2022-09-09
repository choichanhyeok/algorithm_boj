


except_crotia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
alphabets = input()

for except_word in except_crotia:
    alphabets = alphabets.replace(except_word, "*")
print(alphabets)
print(len(alphabets))