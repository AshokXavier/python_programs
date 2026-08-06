customer_name = input("Enter Customer Name: ")
product_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price_per_product = float(input("Enter Price Per Product: "))
membership_type = input("Enter Membership Type: ")
wallet_balance = float(input("Enter Wallet Balance: "))

total_cost=price_per_product*quantity
print(f"Total Cost: {total_cost}")
gst=int(input("GST Amount: "))
final_amount=total_cost+gst
print(f"Final Bill Amount: {final_amount}")

delivery_charge=int(input("Enter Delivery Charge: "))
final_amount+=delivery_charge

print("Wallet Balance Sufficient: ",wallet_balance>=final_amount)

print("Free Delivery Eligible: ",final_amount>1000 and membership_type=="gold")

products=["Rice","Sugar","Oil","Milk","Bread"]
print("Product Available: ",product_name in products)

li1=[1,2,3,4]
li2=[1,2,3,4]
print("list1 is list2: ",li1 is li2)
x=2
y=2
print("x is y: ",x is y)

print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(5 << 1)
print(5 >> 1)

