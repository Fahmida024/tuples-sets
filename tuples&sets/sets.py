studentid={12,15,17,19,21,25}
print(studentid)
if 19 in studentid:
    print('yes')
if 45 in studentid:
    print('yes')
studentid.add(26)
print(studentid)
studentid.remove(12)
print(studentid)

class1={45,46,47,48,49,51,52}
class2={51,52,53,54,55,45,46}
print(class1.union(class2))
print(class1.intersection(class2))
print(class2.difference(class1))
print(class1.symmetric_difference(class2))

if class1==class2:
    print('Both sides are equel')
else:
    print('Both sides are not equel')
