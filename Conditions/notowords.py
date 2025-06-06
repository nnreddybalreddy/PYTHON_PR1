# num=eval(input("Enter a number between 1 to 10:"))

# if num == 1:
#     print("One")
# elif num == 2:
#     print("Two")
# elif num == 3:      
#     print("Three")
# elif num == 4:  
#     print("Four")
# elif num == 5:
#     print("Five")
# elif num == 6:
#     print("Six")    
# elif num == 7:
#     print("Seven")
# elif num == 8:
#     print("Eight")
# elif num == 9:
#     print("Nine")
# elif num == 10:
#     print("Ten")
# # elif num is not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
# #     print("number is greater than 10")
# else:
#     print("Number is not in the range of 1 to 10")

# num=eval(input("Enter a number between 1 to 10:"))

# if num  in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if  num == 1:
#         print("One")    
#     elif num == 2:
#         print("Two")        
#     elif num == 3:  
#         print("Three")      
# else:
#     print("Number is not in the range of 1 to 10")

# num=eval(input("Enter a number between 1 to 10:"))

# num_word={1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten"}
# if num in num_word:
#     # print(num_word[num])
#     print(num_word.get(num))
# else:   
#     print("Number is not in the range of 1 to 10") 

num=eval(input("Enter a number between 1 to 10:"))
# if num not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     print("Number not in 1 to 10")
# else:
#     if num == 1:
#         print("One")
#     elif num == 2:  
#         print("Two")    
#     elif num == 3:  
#         print("Three")
#     elif num == 4:  
#         print("Four")   
#     elif num == 5:
#         print("Five")        
#     elif num == 6:    
#         print("Six")
#     elif num == 7:
#         print("Seven")
#     elif num == 8:      
#         print("Eight")    
#     elif num == 9:    
#         print("Nine")
#     elif num == 10:    
#         print("Ten")

num_word = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}


if num in num_word:
    print(num_word.get(num))
else:
    print("Number is not in the range of 1 to 10")    