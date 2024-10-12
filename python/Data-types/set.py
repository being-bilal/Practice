# set : mutable - unordered - not support duplication
set_1 = {1, 2, 3, 4, 5}
print(f"original set : {set_1}")
# mutable objects like list cannot be used in a set
# set.add(value) is used to add a single value in a set
set_1.add(6)
print(f"tuple.add(6) : {set_1}")
# set.update([value]) is used to add multiple value to a set
set_1.update([7, 8])
print(f"set.udate([7,8]) : {set_1}")
# set.discard(value) is used to discard a single value in a set
set_1.discard(8)
print(f"set.discard(8) : {set_1}")
# set.remove(value) is used to remove a  value in a set
set_1.remove(6)
print(f"set.remove(6) : {set_1}")
# difference between discard() is that it leaves a set unchanged if the element is not present
# the remove() function will raise an error 
# set_2 = set.copy() is used ro copy a set
set_2 = set_1.copy()
print(f"set.copy() : {set_2}")
# set.pop() removes a random value from a set
set_1.pop()
print(f"set.pop() : {set_1}", end="\n\n")

# operations 
a = {0, 1, 3, 5, 7}
b = {0, 2, 4, 6, 8}
print(f"a : {a}")
print(f"b : {b}", end="\n\n")

# union : return all the values from set 'a' and 'b'.
# union can also be done by '|' like: (a|b)
union = a.union(b)
union = a|b
print(f"a.union(b), a|b : {union}")

# intersection : returns only the values which are in both set 'a' and 'b'.
# intersection can also be done by '&' like : (a & b)
intersection = a.intersection(b)
intersection = (a & b)
print(f"a.intersection(b), (a & b) : {intersection}")

# difference : returns all the values which are in set 'a' and not in set 'b'.
# difference can also be done by '-' like : (a-b)
difference = a.difference(b)
difference = (a-b)
print(f"a.difference(b), (a-b) : {difference}")

# Symmetric_Difference : returns the values which are in 'a' and 'b' but not in both
# Symmetric_Difference can also be done by '^' like : (a^b)
Symmetric_Difference = a.symmetric_difference(b)
Symmetric_Difference = (a^b)
print(f"a.Symmetric Difference(b), (a^b) : {Symmetric_Difference}", end="\n\n")

# update 
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
print(f"A : {A}")
print(f"B : {B}", end="\n\n")
# a.update(b) can the set 'a' with values of both set_1 and set_2
A.update(B)
print(f"A.update(B) : {A}")
# a.difference_update(b) change the set 'a' to the difference of set 'a' and 'b'
A.difference_update(B)
print(f"A.difference_update(B) : {A}")
# a.intersection_udate(b) changes the set 'a' to the intersection of set 'a' and 'b'
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
A.intersection_update(B)
print(f"A.intersection_update(B) : {A}")
# a.symmetric_difference_update(b)changes the set 'a' to the symmetric_difference of set'a' and 'b'
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
A.symmetric_difference_update(B)
print(f"A.symmetric_difference_update(B) : {A}", end="\n\n")

y = {1, 2, 4}
z = {1, 2, 4, 6, 8}
# a.isdisjoint(b) : set a is said to be disjoint if there is no common value between set 'a' 'b'.
x = y.isdisjoint(z)
print(f"y.isdisjoint(z) : {x}")
# a.issubset(b) : 'a' is said to be the subset of 'b' if all the values of 'a' is present in 'b'
x = y.issubset(z)
print(f"y.issubset(z): {x}")