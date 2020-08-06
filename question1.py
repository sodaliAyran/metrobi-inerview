# Since the list can contain anything ranging from strings, intergers to other list we can't trust the elements to be hashable so we can not use dictionaries and sets therefore we have to resort to a quadratic time solution

a = [[1, 2], 2, [2], [3], [1, 2], [5],"ilke", "elvan" , "ilke", [3]]

duplicates = [x for n, x in enumerate(a) if x in a[:n]]
print(duplicates)	
