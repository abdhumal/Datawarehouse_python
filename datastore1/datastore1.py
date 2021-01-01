import json
import time
import os

temp={}

x=input("Do you want to import main_database and perform operations on it yes/no: ")
if(x=="yes"):
    #Load main database
    print('Loading main_database in temp...')
    with open('master.json', 'r') as masteropen:
        data_load = json.load(masteropen)
    temp=data_load
    print('Loaded into main_database')
    print(temp)

m={}
d=temp
def read(k):
    if k in m.keys(): 
       return m[k]
    else: 
        return 0
x1=int(input("Enter 1 for create , 2 for read , 3 for delete , 4 to exit , 5 to show data: "))

if(x1==1):
    key=input("Enter key for input")
    if(read(key)):
         print("value is already present")
    else:
        value=int(input("Enter its corresponding value"))
        m[key]=value
elif(x1==2):
    key=input("Enter key to read")
    print(read(key))
elif(x1==3):
    key=input("Enter key")
    del m[key] 
    print("key deleted")
elif(x1==5):
    print (m)
else:
    sys.exit()
with open('temp.json','w') as fp:
    json.dump(m, fp)


print('Your database after operatons are : ')
print(m)

x=input("Is this first ever operation yes/no? ")
if(x=="yes"):
    with open('master.json','w') as fp:
        json.dump(m,fp)
    print("thank you")
    exit()


x=input("Do you want to save this is the master dataset yes/no :")
if(x=="yes"):
    data={}
    with open('master.json', 'r') as fp:
        data=json.load(fp)

    master=dict(data)
    master.update(m)
    with open('master.json', 'w') as fp:
        json.dump(master,fp)


with open('master.json', 'r') as fp:
     data1=json.load(fp)
print(data1)
print("All task done,Thanks")
