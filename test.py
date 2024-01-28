
data = {"k1":1,"k2":2}

with open("file.txt","wb") as f:
    f.write(data)

d2={}

with open("file.txt","rb") as f:
    d2 = f.read()