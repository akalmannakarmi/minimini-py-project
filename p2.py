# Wap to perform the following:
# 1) Input a text from user and store each word with its count in a file
# 2) Search a word and display its count
# 3) Print the most used word
# 4) Insead of reading from console read text from a file

dataPath = "data"
data = {}

def read():
    with open(dataPath,"r") as f:
        lines = f.readlines()
    for line in lines:
        word,count=line.split(":")
        data[word]=int(count)

def add():
    text = input("Enter text:")
    words = text.split(" ")
    for word in words:
        if word not in data:
            data[word]=0
        data[word]+=1
    
    d = ""
    for word,count in data.items():
        d+=f"{word}:{count}\n"

    with open(dataPath,"w") as f:
        f.writelines(d)

def search():
    word = input("Word:")
    if not data:
        read()
    if word in data:
        print(f"{word}:{data[word]}")
    else:
        print(f"{word}:0")

def display():
    if not data:
        read()
    key = max(data, key=lambda k: data[k])
    print(f"Most used:{key}:{data[key]}")

def addFile():
    filePath = input("Enter file:")

    text=""
    with open(filePath,"r") as f:
        text = f.read()
    
    words = text.split(" ")
    for word in words:
        if word not in data:
            data[word]=0
        data[word]+=1
    
    d = ""
    for word,count in data.items():
        d+=f"{word}:{count}\n"

    with open(dataPath,"w") as f:
        f.writelines(d)

prompt="""
Options:
######################
1) Add Text
2) Search Word
3) Most Used Word
4) Add Text from file
5) Quit
######################
What do u what to do(1-5)?
"""
def run():
    while True:
        q = input(prompt)
        if q=="1":
            add()
        elif q=="2":
            search()
        elif q=="3":
            display()
        elif q=="4":
            addFile()
        elif q=="5":
            break
        else:
            print("You can only enter 1-5")


if __name__ == "__main__":
    run()