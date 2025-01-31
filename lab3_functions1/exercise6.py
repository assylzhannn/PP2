"""Write a function that accepts string from user, 
return a sentence with the words reversed. We are ready -> ready are We"""
def reversed(lst):
    lst.reverse()
    return lst

sentence = input("enter the sentence: ").split()
print(reversed(sentence))