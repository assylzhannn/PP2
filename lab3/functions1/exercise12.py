#Define a functino histogram() that takes a list of integers and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:
def histogarm(lst):
    for i in lst:
        print("*"*i)

lst=list(map(int, input().split()))
histogarm(lst)