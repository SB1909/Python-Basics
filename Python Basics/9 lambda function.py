'''
def result(n):
    return lambda a: a*n
x=result(int(input("Enter a Number:")))
print(x("Hello"))

#OR

x=lambda a: a*"Hello"
print(x(int(input("Enter a Number:"))))
'''

#filter function with lambda:
list_names=["Neha","Parvesh","Surya","Pavan","Rishu"]
list_5names=list(filter(lambda x:(len(x)==5),list_names))
print(list_5names)
