# #ljust(width,fillchar)

# s="Hello"
# print(s.ljust(10,"*"))
# # #no new string will be create
# # # Hello*****

# ##########  2

s="Hello"
# print(s.rjust(10))
# #     Hello

# print(s.rjust(10,"_"))
# #_____Hello

# s="Hello"
# print(s.center(10,"*"))
# # **Hello***

# #zfill(width)
# print(s.zfill(10))
# #00000Hello


############ Strip Methods

# lstrip

s="     Hello"
print(s.lstrip())
#by default will be strip " "
# Hello

# s="$$Hello"
# print(s.lstrip("$"))
# #Hello


# s="Hello     "
# print(s.rstrip())
# #Hello


# s="$$$$Hello$$$$"

# print(s.strip("$"))
# #Hello


s="#! Hello  $*"

x=s.strip("#!$*")
print(x)
#Hello 








