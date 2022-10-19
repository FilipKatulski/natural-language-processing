import re
import os 

addition = ".*dodaje się .*[0-9].*"
removal = ".*skreśla się.*"
change = ".*otrzymuje brzmienie.*"

for i in os.listdir(path="ustawy"):
    print("ustawy/"+i)
    with open("ustawy/"+i) as f:
        data = f.read()

    add = re.findall(addition, data)
    rem = re.findall(removal, data)
    cha = re.findall(change, data)
    print(i, ":", len(add), add)
    #print(i, ": ", len(rem))
    #print(i, ": ", len(change))
    