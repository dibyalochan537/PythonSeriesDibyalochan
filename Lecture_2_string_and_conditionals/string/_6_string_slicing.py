# str[start_index:end_index] // end index not count
# for -ve indexing also same end index not included i.e. -5,-4,-3,-2,-1
str1="Raju Dash"
print(str1[:len(str1)]) #this means starts from zero index and end index is length of the string
print(str1[:]) #this means starts from zero index and end index is length of the string
print(str1[1:]) #this means starts from 1 index and end index is length of the string
# for -ve
print(str1[-3:-1])#end index is length-1 and start index is -3 from right to left now calculate i.e. as
