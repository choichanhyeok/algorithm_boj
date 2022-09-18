conversions = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

alphabets = input()


for c in conversions:
    alphabets = alphabets.replace(c, '*');
print(len(alphabets))
