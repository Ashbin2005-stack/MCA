list1=[1,2,4,3,8]
list2=[1,2,3,4,5]

print("the fist list is ", list1)
print("the second list is ", list2)

sum1=0
sum2=0
for x in range(0,len(list1)):
    sum1=sum1+list1[x]
print("sum of all elements in given list1: ",sum1)
for x in range(0,len(list2)):
    sum2=sum2+list2[x]
print("sum of all elements in given list2: ",sum2)
if sum1==sum2:
    print("List sum to same value")
else:
    print("List are of different sum")