# WAP to perfor the following:
# 1) Add Record to a file
# 2) Search Record in a file
# 3) Delete a Record in a file
# 4) Display all Records in a table

def add():
    fname = input("Which file?")
    count = int(input("how many records?"))
    lines = ""
    for _ in range(count):
        name = input("Enter Name:")
        address = input("Enter Address:")
        dob = input("Enter DOB:")
        salary = input("Enter Salary:")
        lines +=f"{name}:{address}:{dob}:{salary}\n"
    with open(fname,"a") as f:
        f.writelines(lines)

def search():
    flag = False
    fname = input("Which file?")
    name = input("Name to search:")
    with open(fname,"r") as f:
        lines = f.readlines()
    for line in lines:
        record = line.split(":")
        if name == record[0]:
            flag = True
            print(f"Name:{record[0]}\nAddress:{record[1]}\nDOB:{record[2]}\nSalary:{record[3]}")
    if not flag:
        print("Not found")

def delete():
    flag = False
    fname = input("Which file?")
    name = input("Name of record to delete:")
    with open(fname,"r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].startswith(name):
            flag=True
            lines.pop(i)
            break
    if not flag:
        print("Not found")
    else:
        with open(fname,"w") as f:
            f.writelines(lines)
        print("Deleted")


def display():
    fname = input("Which file?")
    with open(fname,"r") as f:
        lines = f.readlines()
    print("-----------------------------------------------------")
    print("|Name        |Address     |DOB         |Salary      |")
    print("-----------------------------------------------------")
    for line in lines:
        record = line.split(":")
        print(f"|{record[0]:<12}|{record[1]:<12}|{record[2]:<12}|{record[3].strip():<12}|")
    print("-----------------------------------------------------")

prompt="""
Options:
###################
1) Add record
2) Search record
3) Delete record
4) Display records
5) Quit
###################
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
            delete()
        elif q=="4":
            display()
        elif q=="5":
            break
        else:
            print("You can only enter 1-5")


if __name__ == "__main__":
    run()