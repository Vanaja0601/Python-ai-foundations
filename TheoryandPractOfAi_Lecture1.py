#Task 1 lecture1
#used bubble sort to sort the list,n-1-i to prevent the comparision of sorted elements and n-1 for i because by the time of i as n-1 there would be no ddorting as ot is already sorted by that time 
#after n-1 passes all elements are sorted so last pass would be redundant..
num=[]
for i in range(4):
    num.append(int(input("Enter a num")))
print(f'num before sorting {num}')
n=len(num)
for i in range (n-1):
    for j in range(n-i-1):
        if(num[j]>num[j+1]):
            num[j],num[j+1]=num[j+1],num[j]
print(num)
tuple1=tuple(num)
print(tuple1)

##pROOF Of correct ness
##we need to prove that there is a termination(base case) and the recursive logic is correct-for loops u will show a loop variant in the starting which is true before and after condition 
