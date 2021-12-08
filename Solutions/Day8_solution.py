count = 0
fn = "Data/adventofcode_8.txt"
with open(fn, "r") as my_file:
    myl = list(my_file.readlines())
for line in myl:
    mylist = line.replace("\n","").split("|")[1].split()
    for i in mylist:
        if len(i) in [7,2,4,3]:
            count+=1
print(count)   