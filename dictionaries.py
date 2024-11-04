# Dictionaries are used to store data values in key:value pairs.
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
print("Dictionaries".upper().center(50, "="))
# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

print("")
print("Access items".upper().center(50, "="))
# Access items
print(band["vocals"])
print(band.get("guitar"))

print("")
print("List all keys".upper().center(50, "="))
# list all keys
print(band.keys())

print("")
print("List all values".upper().center(50, "="))
# list all values
print(band.values())

print("")
print("List of key/value pairs as tuple".upper().center(50, "="))
# list of key/value pairs as tuple
print(band.items())

print("")
print("Verify a key exists".upper().center(50, "="))
# Verify a key exists
print("guitar" in band)
print("triangle" in band)

print("")
print("Change values".upper().center(50, "="))
# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

print("")
print("Remove items".upper().center(50, "="))
# Remove items
print(band.pop("bass"))
print(band)

print("")
band['drums'] = 'Bonham'
print(band)

print("")
print(band.popitem()) # tuple
print(band)

# %%
print("")
print("Delete and clear".upper().center(50, "="))
# Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

print("")
band2.clear()
print(band2)
# %%
del band2
# %%
print("")
print("Copy dictionaries".upper().center(50, "="))
# Copy dictionaries
band2 = band # create a reference
print("Bad copy!")
print(band2)
print(band)
# %%
print("")
band2 = band.copy() # create a copy
print("Good copy!")
print(band)
print(band2)

# %%
print("")
print("or use the dict() constructor function".upper().center(50, "="))
# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)
# %%
print("")
print("Nested dictionaries".upper().center(50, "="))
# Nested dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
  'member1': member1,
  'member2': member2
}
print(band)
print(band["member1"]["name"])
# %%
print("")
print("Sets".upper().center(50, "="))
# Sets
# Sets are used to store multiple items in a single variable.
# Set items are unordered, unchangeable, and do not allow duplicate values.
nums = {1, 2, 3, 4, 5}
nums2 = set((1, 2, 3, 4, 5))
print(nums)
print(nums2)
print(type(nums))
print(len(nums)) # number of items in the set

# %%
print("")
print("No duplicate allowed".upper().center(50, "="))
# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)
# %%
print("")
print("True is dupe of 1, False is dupe of zero".upper().center(50, "="))
# True is dupe of 1, False is dupe of zero
nums = (1, True, 2, False, 3, 4, 0)
print(nums)
# %%
print("")
print("Check if a value is in a set".upper().center(50, "="))
# Check if a value is in a set
print(2 in nums)
print("But you can't refer to an element in the set with an index position or a key".center(50, "="))
# But you can't refer to an element in the set with an index position or a key


# %%
print("")
print("Add a new element to a set".upper().center(50, "="))
# Add a new element to a set
nums = {1, 2, 3, 4, 5}
nums.add(8)
print(nums)
# %%
print("")
print("Add elements from one set to another".upper().center(50, "="))
# Add elements from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)
# %%
print("")
print("You can use update with lists, tuples, and dictionaries, two".center(50, "="))
# You can use update with lists, tuples, and dictionaries, two
one = {1, 2, 3}
two = {2, 3, 4}
mynewset = one.union(two)
print(mynewset)
# %%
print("")
print("Keep only the duplicate".upper().center(50, "="))
# Keep only the duplicate
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)

# %%
print("")
print("Keep everything, except the duplicate".upper().center(50, "="))
# Keep everything, except the duplicate
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)

# %%
print("")
print("Remove duplicate element".upper().center(50, "="))
# Remove duplicate element
one = {1, 2, 3}
two = {2, 3, 4}
one.difference_update(two)
print(one) # Why does it print {1} and not {1, 4}?
# %%
print("")
print("Explain".upper().center(100, "="))
explanation = (
    "There seems to be a misunderstanding due to the absence of specific code. "
    "However, I can offer a general explanation regarding Python dictionaries and sets, "
    "which might clarify the situation.\n\n"
    "In Python, dictionaries store key:value pairs, while sets store unique, unordered items. "
    "If you expected an output of `{1, 4}` but got `{1}`, it suggests you're working with a set. "
    "This discrepancy could arise from how elements are added to the set. "
    "Ensure each element is added with the `.add()` method.\n\n"
    "For example:\n"
    "```python\n"
    "my_set = set()\n"
    "my_set.add(1)\n"
    "my_set.add(4)\n"
    "print(my_set)\n"
    "```\n"
    "This should yield `{1, 4}`. If it doesn't, the code to add `4` might be missing, "
    "not executed, or there could be a logical error preventing `4` from being added.\n\n"
    "Sharing the specific code snippet causing the unexpected output would help in providing a more targeted explanation."
)

print(explanation)
print("=".center(100, "="))
# %%
print("")
my_set = set()
my_set.add(1)
my_set.add(4)
print(my_set)

