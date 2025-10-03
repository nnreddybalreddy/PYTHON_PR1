# Resturant
# for i in range(1,5):
#     menu=input(f'Please enter menu:{i}::')
#     price=input(f'Please enter price for this {i}:::')
#     dash=20-len(menu)-len(price)
#     print(menu + "-" * dash + str(price))


# for i in range(1,5):
#     menu=input(f'Please enter menu:{i}::')
#     price=input(f'Please enter price for this {i}:::')
#     dash=20-len(menu)-len(price)
#     print(f'{menu}  {"-" * dash}  {price}')

##### Card Payment
card="4455 1122 3344 8899"
display=card[15:]

print(display)

# for i in range(len(card)):
#     if i>=0 and i<15 and card[i].isdigit():
#         print("x",end="")
#     elif card[i].isspace():
#         print(" ",end="")    
# print(f"{display}")

# #2nd Method
# four="x"*4 + " "
# DispNo=four * 3 + display
# print(DispNo)

# four="x" * 4 + " "
# display_t=3 * four + display

# print(display_t)

four= "*" * 4 + " "
display_t=3 * four + display
print(display_t)



##################
##### URL Parsing:

    