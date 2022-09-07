# TODO:1. Write a Python script to create a list of first N natural numbers.

# n = int(input('Enter the number:'))
# list=[]
# i=1
# while i<=n:
#   list.append(i)
#   i=i+1
  
# print(list)

#TODO: List Comprehension
# n = int(input('Enter the number:'))
# result = [i for i in range(1,n+1)]
# print(result)

# TODO:2. Write a Python script to create a list of first N odd natural numbers.
# n = int(input('Enter the number:'))*2
# list=[]
# i=1
# while i<=n:
#   if i % 2 !=0:
#     list.append(i)
#   i=i+1
  
# print(list)

# TODO: LIST COMPREHENSION

# n = int(input('Enter the number:'))*2
# result = [i for i in range(1,n) if i % 2 !=0]
# print(result)

#TODO:3. Write a Python script to create a list of first N even natural numbers.
# n = int(input('Enter the number:'))*2
# list=[]
# i=1
# while i<=n:
#   if i % 2==0:
#     list.append(i)
#   i=i+1
# print(list)

# TODO: lIST  COMPREHENSION
# n =int(input('Enter the number:'))*2
# result = [i for i in range(2,n+1) if i % 2 ==0]
# print(result)


#TODO:4. Write a Python script to find the greatest number in a given list of numbers.

# list = [10,20,30,40,50,60,70,80,90,100,90,80]
# maxNumber = 80
# for i in list:
#   if i > maxNumber:
#     maxNumber = i

# print(maxNumber,'is the maximum number in the list')

# TODO: List Comprehension Greatest Number
# listOne = [10,20,30,40,50,60,70,80,90,100,90,80]
# greatestNumber = max([i for i in listOne])
# print(greatestNumber)

#TODO: 5. Write a Python script to find the smallest number in a given list of numbers.

# list = [10,20,30,40,50,60,70,80,90,100]
# smallestNumber = 30

# for i in list:
#   if i< smallestNumber:
#     smallestNumber = i
# print(smallestNumber,'is the smallest number in the list')

#TODO: LIST Comprehension
# list = [10,20,30,40,50,60,70,80,90,100]
# minNumber = min([i for i in list])
# print(minNumber)

#TODO:6. Write a Python script to calculate the sum of elements in a given list of numbers.
# n = eval(input('Enter the number:'))
# sum =0
# for i in n:
#   sum=sum+i
# print(sum)

#TODO: List Comprehension
# n = eval(input('Enter the number:'))
# addNumbers = sum([i for i in n])
# print(addNumbers)

#TODO:7. Write a Python script to remove all non int values from a list.
# list = [10,20,30,'deepak',40,50,'kumar',60,70,'nayak']

# for i in list:
#   if type(i) == str:
#     list.remove(i)

# print(list)

#TODO: LIST Comprehension
# a=[list.remove(i) for i in list if type(i) == str]
# print(list)

# TODO:8. Write a Python script to print distinct elements along with their frequencies of occurrence in the lisT
# list=[10,20,30,10,20,10,40,50,60,10,60,70,80,60]
# element = int(input('Enter the element you want to check:'))
# count = 0
# for i in list:
#   if i == element:
#     count = count+1
# print('The frequencies of occurences of:',element,":",count)

#TODO: List comprehension
# list=[10,20,30,10,20,10,40,50,60,10,60,70,80,60]
# element = int(input('Enter the element you want to check:'))
# result = [i for i in list if i == element]
# print(len(result))



    
# TODO: 9Write a Python script to print indices of all occurrences of a given element in a given list.



# list=[10,20,30,10,20,10,40,50,60,10]
# element = int(input('Enter the element you want to check:'))
# for i in range(len(list)):
#   if list[i] == element:
#     print(i, ":", element, end=" ")

# TODO: List Comprehension
# list=[10,20,30,10,20,10,40,50,60,10]
# element = int(input('Enter the element you want to check:'))
# result = [i for i in range(len(list)) if list[i] == element]
# print('Indices of the element',element,"are:",result)


# TODO: 10. Write a python script to sort a list.
ListOne = [100,180,10,20,50,60,80,90,120,155,132,166]
ListOne.sort()
print(ListOne)