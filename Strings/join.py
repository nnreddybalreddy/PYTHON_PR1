# my_str="Python"
# my_str1="_".join(my_str)
# print(my_str1)
#   # P_y_t_h_o_n
# # my_str1="\t".join(my_str)
# # print(my_str1)
# #  # P    y   

my_str="Python"
my_new_str="Python Scripting"
my_new_str1="String operation"

# print(my_str.center(20))
#  #                 Python

print(f'{my_str.center(20)}\n{my_new_str.center(20)}\n{my_new_str1.center(20)}')
#        Python
#  Python Scripting
#   String operation

print(my_str.zfill(10))
# 0000Python