#3c
word=input("enter word")
vowels=['a','e','i','o','u']
list=[]
for x in word:
 if(x in vowels and x not in list):
     list.append(x)
     print("vowel present in the given word is:",list)
#3d
a=input("enter word")
for i in range(len(a)):
    print("ascii value is ",a[i],"is",ord(a[i]))