import products;
import mysql.connector;
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rahul@2004",
    database="grocery")
mycursor=mydb.cursor()

ch=int(input(('''           Welcome to our store\n
         1.Login as customer
         2.Login as admin
         3.New account
Enter choice:''')))
l=[]
m=[]
if (ch==1):
    usname=input("Enter user name:")
    passwd=input("Enter password:")
    l.append(usname)
    qry="select * from login where username=%s"
    mycursor.execute(qry,l)
    r=mycursor.fetchall()
    if r==[]:
        print("No user found")
    else:
        q="select passwd from login where username=%s"
        mycursor.execute(q,l)
        p=mycursor.fetchone()
        if passwd in p:
            print("Successfull login as customer")
        else:
            print("Incorrect password")

elif (ch==2):
    usname=input("Enter user name:")
    passwd=input("Enter password:")
    l.append(usname)
    qry="select * from login where username=%s"
    mycursor.execute(qry,l)
    r=mycursor.fetchall()
    m=list(r[0])
    if r==[] or m[2]=="customer":
        print("No user found")
    else:
        q="select passwd from login where username=%s"
        mycursor.execute(q,l)
        p=mycursor.fetchone()
        if passwd in p:
            print("Successfull login as employer\n")
            pd=products.product()
        else:
            print("Incorrect password")

elif(ch==3):
    ch=int(input("\n1.Customer\n2.Employer\nEnter choice:"))
    if(ch==1):
        na=input("Enter your name:")
        ph=input("Enter mobile number:")
        add=input("Enter address:")
        l.append(na)
        l.append(ph)
        l.append(add)
        qry="insert into customer (name,phone_number,address) values (%s,%s,%s)"
        mycursor.execute(qry,l)
        print("Account created successfully\n")
        ps=input("Set password:")
        m.append(na)
        m.append(ps)
        m.append("customer")
        qr="insert into login (username,passwd,role) values (%s,%s,%s)"
        mycursor.execute(qr,m)
        print("Password set successful")
        mydb.commit()
else:
    print("Enter correct choice..")

    
    
