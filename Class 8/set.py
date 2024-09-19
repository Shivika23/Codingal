s = {1,2,3,3,3,4,5,5,6}
print(s)

s.add(7)
print(s)

s2 = {1,5,8,9}

print(s.difference(s2))
print(s.symmetric_difference(s2))

print(s2.difference(s))
print(s2.symmetric_difference(s))
