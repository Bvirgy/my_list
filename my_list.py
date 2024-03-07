my_list=[] #Create an empty list called my_list
my_list.append(10) #Append the element 10 to my_list
my_list.append(20) #Append the element 20 to my_list
my_list.append(30) #append the element 30 to my_list
my_list.append(40) #Append the element 40 to my_list

my_list.insert(1,15) #Insert the value 15 at the second position in the list

my_list.extend([50,60,70]) #Extend my_list with another list:[50,60,70]

my_list.pop() #Remove the last element from my_list

my_list.sort() #Sort my_list in ascending order

index_of_30 = my_list.index(30) #Find the index of the value 30 in my_list
print(index_of_30) #Print theindex of 30 in my_list
