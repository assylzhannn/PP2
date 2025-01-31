"""Write a Python function that takes a list and returns a new list with unique elements of the first list.
 Note: don't use collection set"""
def unique(lst):
    new_list=[]
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list
lst=list(map(str, input().split()))
print(unique(lst))