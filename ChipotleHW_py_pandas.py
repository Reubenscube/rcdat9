#PYTHON
#PART 1
import csv
with open('chipotle.tsv') as csvfile:
    file_nested_list = csv.DictReader(csvfile, delimiter='\t')
    #opens the TSV file and sets the delimeter as tabs
    chipotle_list = [row for row in file_nested_list]sv.DictReader(csvfile, delimiter='\t'
    #stick each row into a list of dicts with keys = column header
chipotle_list[0]

#PART 2
r = {'choice_description': 'NULL',
 'item_name': 'Chips and Fresh Tomato Salsa',
 'item_price': '$2.39 ',
 'order_id': '1',
 'quantity': '1'}
r.keys() #confirm what the headers are
header = chipotle_list[0].keys()
r.values() #confirm the values are the chipotle data
data = [row.values() for row in chipotle_list]
#put into list of lists form

#PART 3: Calculate the average price of an order.
clean_item_price = [float(row[3].strip('$ ')) for row in data]
# make the prices into floats instead of strings
sum(clean_item_price)
#Sum all of the order prices - quantity doesn't matter
print(chipotle_list[-1])
#The last row has order_id = 1834, so 1834 orders.
average_order_price = (sum(clean_item_price))/1834
#Average price of an order is the total revenue divided by number of orders
#$18.81

#PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
data = [row.values() for row in chipotle_list]
sodas = []
for row in data:
    if "Canned" in row[1]:
        sodas.append(row[2])
    else:
        pass
sodas_set = set(sodas)

#PART 5: Calculate the average number of toppings per burrito (Advanced Level)
#Note: Let's ignore the 'quantity' column to simplify this task.
item_descriptions = [row[2] for row in data] #just looking at the entree descriptions
toppings = []
burrito_count = 0 #This is the number of rows that include a burrito
for row in data:
    if ("Burrito" or "burrito") in row[1]:
        toppings.append(row[2])
        burrito_count += 1
toppings_length = []
for row in toppings:
    toppings_length.append(len(row.split(','))) #The true delimiter is commas not spaces or brackets
sum(toppings_length)
average_toppings = sum(toppings_length)/burrito_count
# 6323/1172 = 5.39 - even if I put the average_toppings into float it's still off

#PART 6: Create a dictionary in which the keys represent chip orders and
#  the values represent the total number of orders.
# I had to do this in pandas
chipotle[chipotle.item_name.str.contains("Chips")].groupby('item_name').order_id.count()
#Creates a dataframe with the chip order types, and then the quantity
#Convert to dictionary??

#PANDAS
import pandas as pd
chipotle = pd.read_table('chipotle.tsv',sep ='\t')

chipotle.columns # Verify column headers

#What was the meal type breakdown for each protein?
chipotle.item_name[chipotle.item_name.str.contains("Veggie")].value_counts()
#Also for chicken, steak, carnitas, barbacoa.

chipotle.item_name.value_counts()
#What were the most ordered items?

chipotle[chipotle.choice_description.str.contains("Guacamole", na=False) & chipotle.item_name.str.contains("Salad", na=False)]
#How many people ordered a salad with guac as a topping?









