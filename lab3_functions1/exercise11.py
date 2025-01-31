#Write a Python function that checks whether a word or phrase is palindrome or not. 
def polindrom(word):
    new=word[::-1]
    if new==word:
        return "Polindrom"
    else:
        return "Not polindrom"
word=input("enter the word to check:")
print(polindrom(word))
