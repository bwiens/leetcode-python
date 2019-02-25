#!/usr/bin/python
#Benjamin Wiens
input = "Ben"
input2 = [2,0,1,8]
#O(N!) runtime

#for string permutations
def permutations(input_string):
    if not len(input_string):
        return []
    if len(input_string) == 1:
        return input_string

    result = []
    char = input_string[0]
    perms = permutations(input_string[1:])
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] +char+ perm[i:])
    return result

#for integer permutations

def permutations2(string):
    if not len(string):
        return []
    if len(string) == 1:
        return [string]
    result = []
    char = string[0]
    perms = permutations2(string[1:])
    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + [char] + perm[i:])
    return result

print(permutations(input))
print(permutations2(input2))

#with itertools
import itertools
def iterperm(string):
	permutations = itertools.permutations(string)
	for p in permutations:
		print(p)

def itercomb(string):
	combinations = itertools.combinations(string,2)
	for c in combinations:
		print(c)

print("itertools permutations:")
iterperm(input)
print("itertools combinations:")
itercomb(input)
#in combinations, order does not matter 3, 2, 1 is the same as 1, 2, 3 so only returns 3, 2, 1 
#permutations('ABCD', 2)		AB AC AD BA BC BD CA CB CD DA DB DC
#combinations('ABCD', 2)		AB AC AD BC BD CD
