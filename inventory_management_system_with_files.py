
"""Inventory Management System with Files"""

file1 = open("InvFile1.txt" , 'w')

file1.close()

"""## Products Details
1 Product ID

2 Name of Product

3 Price of Product

4 Quantity

###DATA
#####1,5 STAR,5,100
#####2,SILK,10,102
#####3,KIT KAT,22,30
#####4,MUNCH,33,10
"""

file1 = open("InvFile1.txt" , 'r')

products = file1.read().split('\n')

file1.close()

print(products)

for product in products:
       print(product)

# Taking User Input
ui_username = input("Enter your Name: ")
ui_phone    = input("Enter your Phone No: ")
ui_mail     = input("Enter your Mail: ")
ui_Id = input("Enter Id :")
ui_Qt = input("Enter Quantity :")
updated_product = []
for product in products:
    product_details = product.split(',')
  ##  [O] it is the row which represent id of the product
    if(product_details[0] == ui_Id):
        if(int(ui_Qt) <= int(product_details[3])):
           print("Product Name : ",product_details[1])
           print("Product Price : ",product_details[2])
           print("Product Quantity : ",ui_Qt)
           print("Total Amount : ", int(ui_Qt) * int(product_details[2]))
           product_details[3] = str(int(product_details[3])-int(ui_Qt))
           # Generating Sales in Sales.txt
           fd = open("Sales.txt",'a')
           sales_detail = ui_username +","+ ui_phone +","+ ui_mail +","+product_details[1] +","+ ui_Id +","+ ui_Qt +","+ str(int(ui_Qt) * int(product_details[2]))+"\n"
           fd.write(sales_detail)
           fd.close()
        else:
            print("Sorry , We are not having enought quantity")
            print("We have only  : " , product_details[3])
            print("Would you like to purchase it?")

            ch = input("Press Y/N: ")

            if (ch == 'Y' or ch == 'y'):
                print("-----------------------------")
                print("Product Name     : ", product_details[1])
                print("Price            : ", product_details[2])
                print("Quantity         : ", product_details[3])
                print("-----------------------------")
                print("Billing Amount   : ", int(product_details[3]) * int(product_details[2]))
                print("-----------------------------")

                # Updating Inventory list
                product_details[3] = '0'
            else:
                print("Thanks")

    # Updating my Inventory List
    updated_product.append(product_details)

list1 =[]

for i in updated_product:
      pro = i[0]+","+i[1]+","+i[2]+","+i[3]+"\n"
      list1.append(pro)

list1[-1] = list1[-1][:-1]

file1 = open("InvFile1.txt" , 'w')
for i in list1:
      file1.write(i)
file1.close()
print("-------------------")
print("Inventory Updated")

file1 = open("InvFile1.txt" , 'r')

products = file1.read().split('\n')

file1.close()
for product in products:
       print(product)
