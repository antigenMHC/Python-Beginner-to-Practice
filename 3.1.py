#3-1
names = ["zhang","ding","hu"]
print("%s  %s  %s"%(names[0],names[1],names[2]))

#3-2
for_friends = "%s, long time no see"
for j in names:
    print(for_friends%(j))

#3-3
rides = ["bike", "bus", "ship"]
like_ride = "i would like to own a %s"
for i in rides:
    print(like_ride%(i))