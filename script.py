dictionary= {}
#using a dictionary to process the file with name as key and price as value

#input file is in input.txt
with open("input.txt") as f:
  for line in f:
    (key, val) = line.split(':')#since they are seperated by :
    dictionary[key] = int(val.strip())

#storing the values of keys and values of the dictionary as two lists
dictvalues_list=list(dictionary.values())
dictkeys_list=list(dictionary.keys())

#list of the price for operations
dict_list=list(dictionary.values())


number=int(input("Number of the employees: "))
k=len(dict_list)-number
#getting the number of employees and finding out how many values to be removed

#sorting the list of values in ascending values and intializing the values.
dict_list.sort()
l=0
r=len(dict_list) -1

for i in range(k):
  if(dict_list[r-1] - dict_list[l] < dict_list[r] - dict_list[l+1]):
      r-=1
  else:
      l+=1
diff=dict_list[r]-dict_list[l]
#utilising technique of binary search for elimination and calculated the difference.

#Writing the output onto the file.
with open("output.txt",'w') as fi:
  fi.write("\nNumber of the employees: {}\n".format(number))
  fi.write("Here the goodies that are selected for distribution are:\n")
  for i in range(l,r+1):
    position = dictvalues_list.index(dict_list[i])#finding key in the dictionary based on the value.
    fi.write(dictkeys_list[position]+": "+ str(dictionary[dictkeys_list[position]])+"\n")
  fi.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is {}\n\n".format(diff))



