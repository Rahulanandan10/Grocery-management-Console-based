import mysql.connector;
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rahul@2004",
    database="grocery")
mycursor=mydb.cursor()

class purchase:
    def __init__(self):
        cart=[]
        price=0
        print("\nSelect products to purchase\n")
        while(True):
            x=[]
            qry="select * from products"
            mycursor.execute(qry)
            r=mycursor.fetchall()
            print(r)
            ch=input("Enter product id to buy and 'q' to end purchase:")
            if (ch=='q'):
                break
            else:
                qry="select Pdt_name from products where Pdt_ID=%s"
                x.append(int(ch))
                mycursor.execute(qry,x)
                r=mycursor.fetchone()
                if (r==[]):
                    print("Product not found")
                    break
                else:
                    cart.append(r[0])
                    print(cart)


            
pur=purchase()        
        
