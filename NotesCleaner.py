n = int(input("How Many Charecters to Prewiew? "))
file = open("Notes.txt","r")
print(file.read(n))
file.close()
print()

file = open("Notes.txt","r")
lines = file.readlines()
file.close()
print("Total Lines: ",len(lines))
for i in range(len(lines)):
    print(i+1,"-->",lines [i].strip())
print()