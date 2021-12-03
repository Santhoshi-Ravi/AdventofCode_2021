fn = "Data/adventofcode_3.txt"
with open(fn, "r") as my_file:
    myl = list(my_file.readlines())
for i in range(0,len(myl)):
    myl[i] = myl[i].replace("\n","")  
# #############################Puzzle one###################################  
bit_range = len(myl[0])
bit_array = []
gamma_rate = []
epsilon_rate = []
bit = 0
for j in range(0,bit_range):
    s = 0
    for i in range(0,len(myl)):
#         print(int(myl[i][j]),end="")
        s+=int(myl[i][j])
#     print(s)
    if s<=int(len(myl)/2):
        gamma_rate.append(0)
        epsilon_rate.append(1)
    else:
        epsilon_rate.append(0)
        gamma_rate.append(1)
#     print(" ")
epsilon_rate.reverse(),gamma_rate.reverse()
g,e = 0,0
for i in range(0,bit_range):
    g += pow(2,(i))*gamma_rate[i]
    e += pow(2,(i))*epsilon_rate[i]
print(g*e)