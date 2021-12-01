fn = "adventofcode_1.txt"
with open(fn, "r") as my_file:
    myl = list(map(int,my_file.read().replace("\n",",").split(",")))
def increase(myl,win):
    count = 0
    for i in range(1,len(myl)):
        if myl[i]-myl[i-win] >0:
            count += 1
    return count
print(f'for puzze one the answer is {increase(myl,1)} and puzzle two the answer is {increase(myl,3)}')