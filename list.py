list_1=[1,2,3,4]
print(list_1)
list_2=[2,8,9,1,6]
print(list_2)
list_3=list_1+list_2
print(list_3)
even=[]
odd=[]
for i in list_3:
    if i %2==0:
        even.append(i)
        even.sort(reverse=True)
    else:
        odd.append(i)
        odd.sort(reverse=True)
print(even+odd)
