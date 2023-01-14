
#to open and write in file:
file_name=input("Enter file name:")
L=["AI is good \n","I am SB\n"]
f=open(file_name,'w')
f.write("Hello LnB\n")
f.writelines(L)
f.close()

#to read file:
f=open("SB.txt",'r')
data=f.read()
print(data)
f.seek(0)   #(1 point=1 letter/space)
data1=f.readline()
print(data1)
f.close()


#To move files:
import shutil
source="SB.xls"
destination="F:\Learning\Data Science LNB\Python LNB Recorded\Practice\Files"
output=shutil.move(source,destination)
print(output)
