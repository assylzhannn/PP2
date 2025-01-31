"""Write a function that accepts string from user and print all permutations of that string."""
def permutations(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in permutations(xs):
                l.append([x]+p)
        return l
word = list('abs')
for p in permutations(word):
    print(p)
