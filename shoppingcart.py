import sqlite3

db= sqlite3.connect("shoppingcart.db")
db.execute("Create table IF NOT EXISTS Shopping(Item text, Quantity integer, Total)")
cur=db.cursor()
class Shoppingcart():
    def __init__(self):
        self.items=dict()
        self.total=0
        self.totalexpenditure=True
        self.cost=True

    def add_item(self):
        self.item_name=input("Enter Item: ")
        self.cost=int(input("Enter cost of item: "))
        self.item_quantity=int(input("Enter Quantity: "))
        self.items[self.item_name]=self.item_quantity
        self.total=self.cost*self.item_quantity
        db.execute("INSERT into Shopping VALUES(?,?,?)", (shp_c.item_name,shp_c.item_quantity,shp_c.total))

    def remove_item(self):
        raw_input=input("To Remove item Enter Del to Decrease Quantity Enter Update: ")
        if(raw_input=='Del'):
            self.item_name=input("Enter Item: ")
            db.execute("DELETE FROM Shopping where Item=(?)",(shp_c.item_name,))
        elif(raw_input=='Update'):
            self.item_name=input("Enter Item name: ")           
            self.item_quantity=int(input("Enter Quatity of Item: "))
            self.cost=int(input("Enter cost of item: "))
            db.execute("Update Shopping set Quantity=(?) Where Item=(?)",(shp_c.item_quantity,shp_c.item_name,))
            self.total=self.cost*self.item_quantity
            db.execute("Update Shopping set Total=(?) WHERE Item=(?)",(shp_c.cost*shp_c.item_quantity,shp_c.item_name,))
        else:
            exit
    
    def sumoflist(self):
        sumofitems=0
        empt=list()
        cur.execute("Select Total from Shopping")

        for i in cur:
            sumofitems=sum(i)+sumofitems
        print(sumofitems)

shp_c=Shoppingcart()
while True:
    x=input("To start Shopping Enter Add to add item and Remove to remove item and Cash to cash in: ")
    if x=='Add':
        shp_c.add_item()
        cur= db.cur()
        cur.execute("SELECT * FROM Shopping")
        for i in cur:
            print(i)

    elif x=='Remove':
        shp_c.remove_item()
        cur= db.cur()
        cur.execute("SELECT * FROM Shopping")
        for i in cur:
            print(i)

    elif x=='Cash':
        shp_c.sumoflist()
    
    else:
        break

cur.close()
db.commit()
db.close()





            