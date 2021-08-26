lista=[]
file=open("device.txt","r")
for i in file:
    i= i.strip ()
    lista.append(i)
    print(i)
file.close()
print(lista)