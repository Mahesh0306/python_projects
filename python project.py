from datetime import datetime
mylist = '''
Apples          Rs 20/kg
Bananas         RS 30/kg
Strawberries    Rs 40/kg
Avocados        RS 15/kg
Bell Peppers    Rs 10/kg
Carrots         Rs 30/kg
Broccoli        Rs 13/kg
Garlic          Rs 15/kg
Lemons          Rs 90/kg
Onion           Rs 50/kg
Parsley         Rs 30/kg
Cilantro        Rs 33/kg
Basil           Rs 22/kg
Potatoes        Rs 31/kg
Spinach         Rs 12/kg
Tomatoes        Rs 10/kg
'''
items_list=[]
price_list=[]
quantity_list=[]
pricelist=[]
price=0
total_price=0
final_price=0
name=input("Enter the name:")
items={"Apples":20,"Bananas":30,"Strawberries":40,"Avocados":15,"Bell Peppers":10,
       "Carrots":30,"Broccoli":13,"Garlic":15,"Lemons":90,"Onion":50,"Parsley":30,
       "Cilantro":33,"Basil":22,"Potatoes":31,"Spinach":12,"Tomatoes":10}
option=int(input("Press the 1 to see the list of items:"))
if option==1:
    print(mylist)
for i in range(len(items)):
    inp1=int(input("press 1 to buy items or 2 to exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter the quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            total_price+=price
            items_list.append(item)
            quantity_list.append(quantity)
            price_list.append(price)
            gst = (total_price*5)/100
            finalamount=gst+total_price
        else:
            print("Sorry the items are not available")
    else:
        print("you are entered the wrong number")
    inp=input("Can i enter the bill yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(28*"=","star super market",28*"=")
            print(33*" ","Gachibowli",33*" ")
            print("Name:",name,30*' ',datetime.now())
            print(75*'-')
            print("sno",8*' ',"items",8*' ','quantity',8*' ','price')
            print(75*'-')
            for i in range(len(pricelist)):
                print(i,5*' ',3*' ',items_list[i],10*' ',quantity_list[i],15*' ',price_list[i])
            print(75*' ')
            print(50*'','Totalamount','Rs',total_price)
            print(75*'-')
            print(75*'',"gst",'Rs',gst)
            print(75*'-')
            print(75*'',"finalamount",'Rs',finalamount)
            print(75*'-')
            print(28*'',*'',"Thanks for visiting",28*'')
            print(75*'')