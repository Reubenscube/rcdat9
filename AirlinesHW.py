# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#reads the whole file at once, and outputs it into the variable data
#rU is reading in the universal mode converts different line endings into \n
with open('airlines.csv', 'rU') as f:
    data = [row.split(',') for row in f]
# the output is a list of lists of strings

#1. Create a list containing the avg. # of incidents per year for each airline.
#we're just using the total time period which is 1985 - 2014 = 30 years
incidents = [round((int(row[2]) + int(row[5])) /float(30),2) for row in data[1:]]

#this gives a list of strings
#replace float(30) with 30.0 to get decimals
#round() command to get fewer decimals after the period.

#2. Create a list of airline names (without the star).
airlines = []
for row in data:
    if row[0][-1] =="*":
        row[0].replace("*","")        
        airlines.append(row[0][0:-1]) #This appends all but the last character
    else:
        airlines.append(row[0])
airlines
#LIST COMPREHENSION METHOD
[row[0].replace("*","") for row in data]
#[row[0].strip("*") for row in data] Does the same thing.  There are also commands
#called Lstrip and Rstrip, and they work from either side - maybe you would
#want to keep an asterisk in the middle of the word

#Remove header from the list of airlines, SEE NOTE ABOVE
airlines.pop(0)
# the better way to do this is to define the header as the first row
header = data[0]
data = data[1:]

#3. Create a list (of the same length) that contains 1 if there's a star and 0 if not.
#Expected output: [0, 1, 0, ...]
star_status = []
for airline in airlines:
    if "*" in airline:
        star_status.append(1)
    elif "*" not in airline:
        star_status.append(0)
print(star_status)

#4. BONUS: Create a dictionary in which the key is the airline name
#(without the star) and the value is the average number of incidents.
tuples = zip(airlines, incidents) #Zip combines two lists into a list of tuples

airlines_dict = {k:v for k,v in zip(airlines, star_status)}
#This creates the dictionary
