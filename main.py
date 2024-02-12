from datetime import datetime

Name = input("Enter Your Name : ").capitalize()

List = ('Rice   Rs.50/Kg''\n'
        'Sugar  Rs.45/Kg\n'
        'Oil    Rs.120/kg\n'
        'Salt   Rs.20/Kg\n'
        'Halid  Rs.80/kg\n'
        'Chilli Rs.80/kg\n'
        'Egg    Rs.250/set\n'
        'Pickel Rs.110/kg\n'
        'Colget Rs.20/pk\n'
        'Atta   Rs.85/kg\n'
        'Meggi  Rs.50/pkt\n')
price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []

items = {'rice': 50, 'sugar': 45, 'oil': 120, 'salt': 20, 'halid': 80, 'chilli': 80, 'egg': 250,
         'pickel': 110,
         "colget": 20,
         "atta": 85,
         "meggi": 50}
while True:
    print("1.List of Items")
    print("2.Generate bill")
    print("3.Exit")

    chose = int(input("Enter your Chose : "))
    if chose ==1:
       print(List)
    for i in range(len(items)):
        inpt=input("Add to your Items (yes/no) : ")
        if inpt =='no':
            break
        if inpt == 'yes':
            item=input("Enter Your Items : ")
            qty=int(input("Enter Your Qty :"))
            if item in items.keys():
                price=qty*(items[item])
                pricelist.append((item,qty,items,price))
                totalprice+=price
                ilist.append(item)
                qlist.append(qty)
                plist.append(price)
                gst=(totalprice*2)/100
                finalprice=gst+totalprice
            else:
                print("Sorry This not Available")
        else:
            print("your wrong enterd")
    if chose ==2:
        inp=input("Can I Bill The Items (yes/no) : ")
        if inp=="yes":
            pass
            if finalprice !=0:
                print("====================== D Mart ===========================")
                print("Name :",Name,"\t\t\tDate :",datetime.now())
                print("----------------------------------------------------------")
                print("S.no",'\t\t\tItems','\t\t\tQyt',"\t\tPrice")
                for i in range(len(pricelist)):
                    print(i,"\t\t\t\t",ilist[i],"\t\t\t",qlist[i],"\t\t\t",plist[i])
                print(57*"-")
                print("Total Price :","\t\t\t\t\t\t\t\t",totalprice)
                print("SGST  :","\t\t\t\t\t\t\t\t\t",gst)
                print(57*"-")
                print("Final Amount :","\t\t\t\t\t\t\t\t",finalprice)
                print(57 * "-")
                print("\t\tTHANK YOU ",Name,"FOR YOUR SHOPPING :)")
                print(57*"=")











