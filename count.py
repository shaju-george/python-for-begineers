

#find the repeating elements of a sting

string = input('Enter the sting')

#method 1
print('method 1')
## initializing a list to append all the duplicate characters
duplicates = []
for char in string:
   ## checking whether the character have a duplicate or not
   ## str.count(char) returns the frequency of a char in the str
   if string.count(char) > 1:
   ## appending to the list if it's already not present
       if char not in duplicates:
           duplicates.append(char)
print(*duplicates)

## Using dictionart
        
print('method 2')
## initializing a dictionary
duplicates = {}
for char in string:
   ## checking whether the char is already present in dictionary or not
   if char in duplicates:
      ## increasing count if present
      duplicates[char] += 1
   else:
      ## initializing count to 1 if not present
      duplicates[char] = 1
for key, value in duplicates.items():
   if value > 1:
      print(key, end = " ")
print()
print(duplicates)

# another method
print('method 3')
c=0

#Counts each character present in the string  
for i in range(0, len(string)):  
    count = 1
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;
            #Set string[j] to 0 to avoid printing visited character  
            string = string[:j] + '0' + string[j+1:] 
   
    #A character is considered as duplicate if count is greater than 1  
    if(count > 1 and string[i] != '0'):  
        print(string[i])
