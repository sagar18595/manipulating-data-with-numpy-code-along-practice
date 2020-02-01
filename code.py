# --------------
import numpy as np
from collections import Counter
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.
data = np.genfromtxt(path,dtype = str,delimiter = ",",skip_header = 1)

# Number of unique matches 
print ("Unique matches number : ", np.unique(data[:,0]).size)


 # How many matches were held in total we need to know so that we can analyze further       statistics keeping that in mind.

# Number of unique teams
print ("Unique teams : ", np.unique(data[:,3:5]))
 # this exercise deals with you getting to know that which are all those six teams that   played in the tournament.

# Sum of all extras
print ("sum of extras are : ", sum(data[:,17].astype(int)))
 # An exercise to make you familiar with indexing and slicing up within data.

# Delivery number when a given player got out
#delivery_number = np.array([[j,k] for i,j,k in zip(data[:,-3],data[:,-12],data[:,-2]) if len(i) > 0])
delivery_number = data[data[:,-3] != ''][:,[-12,-2]]
print (delivery_number)

 # Get the array of all delivery numbers when a given player got out. Also mention the wicket type.

# Number of times Mumbai Indians won the toss
print("toss winner MI : ", np.unique(data[data[:,5] == 'Mumbai Indians'][:,0]).size)
 # this exercise will help you get the statistics on one particular team

# Filter record where batsman scored six and player with most number of sixex
record = data[data[:,-7].astype(int)== 6][:,-10]
print (Counter(record).most_common(2))
 # An exercise to know who is the most aggresive player or maybe the scoring player 







