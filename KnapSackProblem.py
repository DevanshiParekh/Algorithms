#-------------------------------------------------------------------------------
# Name:       Fractional KnapSack Problem (Greedy Method)
#
#
# Author:      Devanshi
#
# Created:     02-04-2017
# Copyright:   (c) Devanshi 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from collections import OrderedDict
from operator import itemgetter

#Taking neccesary inputs for the problem

num_of_objects=int(input("Enter the number of objects"))
max_weight=int(input("Enter the max weight which the sack can hold"))
profit=list(int(i) for i in input(" Enter profit for each object ").split(" "))
weight=list(int(i) for i in input(" Enter weight for each object ").split(" "))

# calculating the value per weight for each item and sorting it in descending order

density=dict(zip(list(range(num_of_objects)),list(round(float(profit[i])/weight[i],3) for i in range(num_of_objects))))
density=OrderedDict(sorted(density.items(), key=itemgetter(1),reverse=True))

#initialising the current weights and profit to zero

i=0
cur_weight=0.0
benefit=0.0

#implementing fractional knapsack

# Take all the items into the sack wholly

while weight[density.keys()[i]]+cur_weight<= max_weight and i<= num_of_objects:
    cur_weight+=weight[density.keys()[i]]
    benefit+=profit[density.keys()[i]]
    i+=1

# Taking the fractional part of the object

while cur_weight<max_weight:
    rem_weight=max_weight-cur_weight
    cur_weight+=rem_weight
    benefit+=density.values()[i]*rem_weight

print (" The maximum benefit which could be obtained for the above given items is : ", benefit)




