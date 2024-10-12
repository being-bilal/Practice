# tuple : immutable - ordered
tuple_1 = (1, 2, 3, 4, 2, 5, 2, )
print(f"original name  : {tuple_1}")
# tuple[index] is used to access a single item from the tuple.
print(f"tuple[2]       : {tuple_1[2]}")
# tuple.index[value] is used to get the index of a value.
x = tuple_1.index(3)
print(f"tuple.index    : {x}")
# tuple[:index] is used to get the value to the certain index.
print(f"tuple[:2]      : {tuple_1[:2]}")
# tuple[index :] is used to get the value from the certain index.
print(f"tuple[2:]      : {tuple_1[2 :]}")
# tuple[::num] is used to display the tuple with the jump of num.
print(f"tuple[::2]     : {tuple_1[::2]}")
# tuple.count(value) is used to get no. of repetition of a certain value.
print(f"tuple.count(2) : {tuple_1.count(2)}")
# converting tuple to list and set.
print(f"tuple to list  : {list(tuple_1)}")
print(f"tuple to set   : {set(tuple_1)}")