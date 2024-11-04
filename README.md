# Lesson 07: Remove duplicate element

This code snippet demonstrates the use of the `difference_update` method in Python sets. It shows how the method modifies the set `one` by removing elements that are also present in the set `two`. The explanation clarifies why the output is `{1}` instead of `{1, 4}` by detailing the steps of the `difference_update` operation.

one = {1, 2, 3}
two = {2, 3, 4}
one.difference_update(two)
print(one) # Why does it print {1} and not {1, 4}?

The [`difference_update`] method in Python modifies the set on which it's called ([`one`] in this case) by removing all elements found in the set passed as an argument ([`two`] in this case). Therefore, after [`one.difference_update(two)`] is executed, [`one`] will only contain elements that are not in [`two`].

Here's a step-by-step explanation of what happens:

1. [`one`] initially contains `{1, 2, 3}`.
2. [`two`] contains `{2, 3, 4}`.
3. [`one.difference_update(two)`] removes all elements from [`one`] that are also in [`two`]. Both `2` and `3` are in [`two`], so they are removed from [`one`].
4. After this operation, [`one`] contains only `{1}`, because `1` is the only element in [`one`] that is not in [`two`].

The reason it prints `{1}` and not `{1, 4}` is that [`difference_update`] does not add elements from [`two`] to [`one`]; it only removes the common elements from [`one`]. The set [`two`] is not modified, and its elements are not added to [`one`].

## Explanation of the code:

**Section 1: Dictionaries**

The code starts with an introduction to dictionaries, which are used to store data in key-value pairs.

* The first dictionary `band` is created with two key-value pairs: `"vocals": "Plant"` and `"guitar": "Page"`.
* The second dictionary `band2` is created using the `dict()` constructor function with the same key-value pairs.
* The code prints the contents of both dictionaries, their types, and their lengths.

**Section 2: Accessing items in a dictionary**

The next section demonstrates how to access specific items in a dictionary:

* The code uses the square bracket notation (`band["vocals"]`) to access the value associated with the key `"vocals"`.
* It also shows how to use the `get()` method to retrieve a value from a dictionary, even if the key is not present.
* The code prints the results of these operations.

**Section 3: Listing all keys and values in a dictionary**

The next section demonstrates how to list all keys and values in a dictionary:

* The code uses the `.keys()`, `.values()`, and `.items()` methods to retrieve lists of keys, values, and key-value pairs, respectively.
* It prints the results of these operations.

**Section 4: Verifying key existence**

The next section demonstrates how to verify whether a specific key exists in a dictionary:

* The code uses the `in` operator to check if the key `"guitar"` is present in the dictionary `band`.
* It also shows how to use this operator with a tuple of values, which is used to create a set.

**Section 5: Changing values**

The next section demonstrates how to change values in a dictionary:

* The code updates the value associated with the key `"vocals"` to `"Coverdale"`.
* It also uses the `update()` method to add new key-value pairs to the dictionary.
* The code prints the updated dictionary.

**Section 6: Removing items**

The next section demonstrates how to remove specific items from a dictionary:

* The code uses the `.pop()` method to remove an item with the specified key `"bass"`.
* It also shows how to use this method without specifying a key, which removes and returns any item that can be found in the dictionary.

**Section 7: Nested dictionaries**

The next section demonstrates how to create nested dictionaries:

* The code creates two inner dictionaries `member1` and `member2`, each with two key-value pairs.
* It then combines these inner dictionaries into a main dictionary `band`.
* The code prints the contents of the `band` dictionary.

**Section 8: Sets**

The final section demonstrates how to create and manipulate sets:

* The code creates a set `nums` containing five unique values.
* It shows how to add new elements to the set using the `.add()` method.
* It also demonstrates how to use the `.union()` method to combine two sets into one.

**Section 9: Duplicate removal**

The next section demonstrates how to remove duplicate elements from a set:

* The code uses the `difference_update()` method to modify the set `one` by removing elements that are also present in the set `two`.
* It explains why the output is `{1}` instead of `{1, 4}`, which involves clarifying the steps of the `difference_update()` operation.

**Section 10: Additional explanations**

The final section provides additional explanations for specific parts of the code, including:

* How to create a copy of a dictionary using the `.copy()` method.
* How to use the `.union()` and `.symmetric_difference_update()` methods with sets.
* An explanation for why the output is `{1}` instead of `{1, 4}`, which involves clarifying the steps of the `difference_update()` operation.
