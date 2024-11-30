import mysql.connector;
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rahul@2004",
    database="grocery")
mycursor=mydb.cursor()

class product:
    
    def addpdt(self,l):
        qry="insert into products (Pdt_Name,Price,Stock) values(%s,%s,%s)"
        mycursor.execute(qry,l)
        print("Product added")
        mydb.commit()
    def dltpdt(self,x):
        qry="delete from products where Pdt_id=%s"
        mycursor.execute(qry,x)
        print("Product deleted")
        mydb.commit()
    def viewpdt(self):
        qry="select * from products"
        mycursor.execute(qry)
        r=mycursor.fetchall()
        return r
    def updpdt(self,l):
        qry="update products set Stock=%s where Pdt_id=%s"
        mycursor.execute(qry,l)
        print("Stock updated")
        mydb.commit()
    def __init__(self):
        while(True):
            ch=int(input("\n1.To add a product\n2.To delete a product\n3.To display products\n4.To edit stock\n5.Exit\n"))
            if (ch==1):
                x=[]
                x.append(input("Enter product name:"))
                x.append(float(input("Enter price:")))
                x.append(int(input("Enter stock:")))
                self.addpdt(x)
            elif (ch==2):
                x=[]
                pid=int(input("Enter product id:"))
                x.append(pid)
                self.dltpdt(x)
            elif (ch==3):
                x=self.viewpdt()
                print(x)
            elif (ch==4):
                x=[]
                pid=int(input("Enter product id:"))
                stk=int(input("Enter stock:"))
                x.append(stk)
                x.append(pid)
                self.updpdt(x)
            elif (ch==5):
                break
        
        
    
