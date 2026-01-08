import itertools

elements = ['a', 'b', 'c']

# All permutations of the list:
permutations = list(itertools.permutations(elements))
print("Permutations of ['a', 'b', 'c']:", permutations)

# All combinations of 2 elemments:
combinations = list(itertools.combinations(elements, 2))
print("Combinations of 2 from ['a', 'b', 'c']:",combinations)
