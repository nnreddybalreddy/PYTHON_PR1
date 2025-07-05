# print("welcome to exception concept")
# try:
#     fo=open("Nari.txt")
#     print(fo.read())
#     fo.close()
# except:
#     print("Some problem in opening file...")    

# my_list=[2,3,4,5]


# try:
#     print(my_list[5])
# except Exception as e:
#     print(e)


# print("this code will also execute\n")

# import fabric # ModuleNotFoundError

try:
    import fabric
except ModuleNotFoundError:
    print("Handled Module not found error")

