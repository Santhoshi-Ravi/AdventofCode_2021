fn = "Data/adventofcode_2.txt"
with open(fn, "r") as my_file:
    myl = list(my_file.readlines())
def day_2(arr,puzzle):
    forw = 0
    aim = 0
    depth = 0
    for i in myl:
        key,value = i.replace("\n","").split(" ")
        if key == 'forward':
            forw += int(value)
            if depth!=0 and puzzle==2:
                add_depth = depth*int(value)
                aim +=add_depth
        elif key == 'down':
            depth += int(value)
        else:
            depth -= int(value)
    if puzzle ==1:
        return forw*depth
    else:
        return forw*aim
print(f'for puzze one the answer is {day_2(myl,1)} and puzzle two the answer is {day_2(myl,2)}')