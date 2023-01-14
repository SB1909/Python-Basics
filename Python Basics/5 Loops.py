'''
n1=[6,5,3,2,8]
for i in n1:
    print(i,"SB")
'''
'''
for i in range(0,5):
    print(i)
'''
'''
data="Hello SB"
for i in data:
    print(i)
'''
'''
office={"name":"SB","contact":8698}
for i in office:
    print(i)
    print(office[i])
'''
'''
#nested loop
for i in range(1,5):
    for j in range(i):  #if i=3 then after printing i=3,j loop will happen 3 times but printing same value i=3
        print(i,'*',end=' ')
    print()
'''
'''
#controllers
for letter in 'lnbcore':
    if letter=='b':
        pass #continue
    print("Hey cureent letter is:",letter)
else:
    print("I am completed")
'''
i=0
a="Hello"
while i<len(a):
    if a[i]=='e':
        i=i+1
    break
print("current letter is:",a[i])
i+=1

