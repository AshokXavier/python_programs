customer_name=input("Enter Customer Name: ")
food_item=input("Enter Food Item: ")
quantity=int(input("Enter Quantity: "))
price_per_item=float(input("Enter Price Per Item: "))
delivery_distance=int(input("Enter Delivery Distance: "))

print("----- ORDER DETAILS -----\n")

print(f"Customer Name: {customer_name}\nType: {type(customer_name)}\nMemory Address: {id(customer_name)}\n")
print(f"Food Item: {food_item}\nType: {type(food_item)}\nMemory Address: {id(food_item)}\n")
print(f"Quantity: {quantity}\nType: {type(quantity)}\nMemory Address: {id(quantity)}\n")
print(f"Price Per Item: {price_per_item}\nType: {type(price_per_item)}\nMemory Address: {id(price_per_item)}\n")
print(f"Delivery Distance: {delivery_distance}\nType: {type(delivery_distance)}\nMemory Address: {id(delivery_distance)}\n")

delivery_charge=float(input("Enter Delivery Charge: "))
print(f"Delivery Charge: {delivery_charge}\n")

total_food_cost=price_per_item*quantity
final_bill_amount=total_food_cost+delivery_charge
print(f"Final Bill Amount: {final_bill_amount}\nType: {type(final_bill_amount)}\n")

print("Checking Data Types:")
print(f"Quantity is integer: {isinstance(quantity,int)}")
print(f"Price is float: {isinstance(price_per_item,float)}")
print(f"Final Bill is float: {isinstance(final_bill_amount,float)}")