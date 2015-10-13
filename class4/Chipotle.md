# Question 1

##1a)	The columns are named order_id, quantity, item_name, choice_description, and item_price.
Each row represents a food item that was ordered - either as part of a larger purchase,
or unique.  The order_id is a for a particular purchase.  The quantity column identifies
the number of times a particular item was purchased.  The choice_description column
provides additional detail (entrees: lists toppings, sodas: flavor, or NULL).  The final
column is the price for that particular item.
    head -n1 chipotle.tsv
	
##1b) How many orders do there appear to be? 1834 orders
    tail -n1 chipotle.tsv
	
##1c) How many lines are in the file? 4623 lines
    wc -l chipotle.tsv

##1d) Which burrito is more popular, steak or chicken? Chicken
    (553 vs 368 lines, includes column headers, but doesn't account for qty >1)
    grep -i "chicken burrito" chipotle.tsv > chicken_burrito.tsv
    grep -i "steak burrito" chipotle.tsv > steak_burrito.tsv
    wc -l chicken_burrito.tsv
    wc -l steak_burrito.tsv

##1e) Do chicken burritos more often have black beans or pinto beans? Black (some have both)
    grep -i "black beans" chicken_burrito.tsv > black_chicken.tsv
    wc -l black_chicken.tsv
    grep -i "pinto beans" chicken_burrito.tsv > pinto_chicken.tsv
    wc -l pinto_chicken.tsv
	
# Question 2
Count the number of occurrences of the word 'dictionary' (regardless of case)
across all files in the DAT9 repo. 33
	#Searches for instances of the word dictionary and sticks it into a new txt file
	grep -ri "dictionary" DAT-DC-9 > dictionary_count.txt
	#Searches for 
	grep "dictionary" dictionary_count.txt

# Question 3

3) Soft Tacos are more popular order than crispy ones (242 vs 103)
	grep -i "crispy taco" chipotle.tsv | wc -l
	grep -i "soft tacos" chipotle.tsv | wc -l