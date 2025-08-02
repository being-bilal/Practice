# HASHMAPS
# Hashmaps are data structures that store key-value pairs, allowing for fast retrieval of values based on their keys.
# Dictionaries are python implementation of hash maps, they are mutable and unordered collections of key-value pairs.

# Hash maps uses hash functions which converts a string key to an integer to compute an index, where the value is stored.
# index = h % table_size (h = Hash_function(key))

# In a hash map, a collision occurs when two different keys produce the same hash index.
# Hashmaps have an average time complexity of O(1) for lookups, insertions, and deletions.
dict_1 = {"Tony stark": "ironman", "bruce wayne": "batman"}
print(f"original dictionary  : {dict_1}")
# to add a item in a dictionary dict_name[key] = value
dict_1["clark kent"] = "Superman"
print(f"Adding Clark kent    : {dict_1}")
# to access a value in dictionary we use key
x = dict_1["Tony stark"]
print(f"accessing tony stark : {x}")
# to delete a item in a dictionary 'del' keyword is used
del dict_1["bruce wayne"]
print(f"deleting bruce wayne : {dict_1}")
# dictionary can be converted into a list or a tuple
print(f"dictionary to a list :  {list(dict_1)}")
print(f"dictionary to a tuple: {tuple(dict_1)}")
# .get is used to get the value of a key
x = dict_1.get("Tony stark")
print(f".get(Tony stark)     : {x}")
# .keys() returns all the keys
x = dict_1.keys()
print(f".keys()              : {x}")

# to loop through the dict use dict_name.items()
print("looping through the dictionary :: ")
for key, value in dict_1.items():
    print(f"{key} : {value}")

# dictionary comprehension
list_1 = ["name", "class", "section", "roll no."]
list_2 = ["bilal", 9, "A", 45]
dict_2 = {name: value for name in list_1 for value in list_2}
print(dict_2)
