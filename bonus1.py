item_count = 0
total_price = 0
most_expensive = None
the_cheapest = None
while True:
    item_price = float(input("Enter item price or 0 to finish "))
    if item_price == 0 :
        break
    item_count +=1
    total_price += item_price
    if most_expensive is None or item_price > most_expensive :
        most_expensive = item_price
    if the_cheapest is None or item_price < the_cheapest :
        the_cheapest = item_price
    if item_count == 0:
        print ("No items were added")    
    else:
        average_price = total_price / item_count
print(f"Number of items: {item_count}")
print(f"Total price: {total_price}") 
print(f"Average item price:{average_price}")
print(f"Most expensive item: {most_expensive}") 
print(f"Cheapest item: {the_cheapest}") 
print (50*"=")         