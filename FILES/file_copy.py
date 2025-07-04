sfile=input("Enter your source file:\n")
dfile=input("Enter your dest file:\n")

sfo=open(sfile,"r")
content=sfo.read()
sfo.close()

dfo=open(dfile,"w")
dfo.write(content)
dfo.close()
