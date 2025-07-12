s1 = "Race"
s2 = "Care"

s1 = sorted(s1.lower())
s2 = sorted(s2.lower())

print("s1 after sorting: ", s1)
print("String2 after sorting: ", s2)


if s1 == s2:
    print('Strings are anagram')
else:
    print('Strings are not anagram')