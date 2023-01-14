#if we know error:
'''
try:
    n1=int(input("Enter a number:"))
    n2=int(input("Enter a number:"))
    sum=n1+n2
    print(sum)
    res=n1/n2
    print(res)
except ValueError:
    print("Please enter 'int' type number...")
except ZeroDivisionError:
    print("Second number should not equal to zero")
'''

#if we don't know error:
'''
i=10
try:
    i=i+'a'
except Exception as e:
    print("Unexpected error...",type(e))
'''

#try with else:
'''
try:
    num=int(input("Enter a number:"))
    assert num%2==0         # check whether condition is satiesfied or not and return true/false
except:                       #for all errors
    print("Not an even number..")
else:
    result=1/num
    print(result)
'''

#try with finnaly:
try:
    data=int(input("Enter data:"))
    print("hello",data)
except:
    print("I am error...check the code..")
finally:
    print("I am always going to print..")   #finally always run



