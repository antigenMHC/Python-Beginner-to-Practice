#3-4
guests = ["eric", "tim","xu"]
print("%s, invite you to dinner"%(guests[0].title()))
print("%s, invite you to dinner"%(guests[1].title()))
print("%s, invite you to dinner"%(guests[2].title()))

print("-------------------------------------------")

#3-5
guests = ["eric", "tim","xu"]
print("%s, invite you to dinner"%(guests[0].title()))
print("%s, invite you to dinner"%(guests[1].title()))
print("%s, invite you to dinner"%(guests[2].title()))
print("oh, %s can't come"%(guests[2].title()))
guests = ["eric", "tim","zhang"]
print("%s, invite you to dinner"%(guests[0].title()))
print("%s, invite you to dinner"%(guests[1].title()))
print("%s, invite you to dinner"%(guests[2].title()))

print("--------------------------------------")

#3-6
guests = ["eric", "tim","zhang"]
print("%s, invite you to dinner"%(guests[0].title()))
print("%s, invite you to dinner"%(guests[1].title()))
print("%s, invite you to dinner"%(guests[2].title()))
print("oh, i find a bigger table")
guests.insert(0, "ding")
guests.insert(2, "wang")
guests.append("hawell")
print("%s, invite you to dinner"%(guests[0].title()))
print("%s, invite you to dinner"%(guests[1].title()))
print("%s, invite you to dinner"%(guests[2].title()))
print("%s, invite you to dinner"%(guests[3].title()))
print("%s, invite you to dinner"%(guests[4].title()))
print("%s, invite you to dinner"%(guests[5].title()))

print("--------------------------------------")

#3-7
print("%s, invite you to dinner"%(guests[0].title()))
print("%s, invite you to dinner"%(guests[1].title()))
print("%s, invite you to dinner"%(guests[2].title()))
print("%s, invite you to dinner"%(guests[3].title()))
print("%s, invite you to dinner"%(guests[4].title()))
print("%s, invite you to dinner"%(guests[5].title()))
print("sorry,".title()+" my table can't delivered in time")
#对六名成员进行操作，删除四名成员并进行说明
one_guest = guests.pop()
print("sorry %s, i can't invite to you"%(one_guest).title())
two_guest = guests.pop(0)
print("sorry %s, i can't invite to you"%(two_guest).title())
three_guest = guests.pop()
print("sorry %s, i can't invite to you"%(three_guest).title())
four_guest = guests.pop()
print("sorry %s, i can't invite to you"%(four_guest).title())
#接下来对剩余人员进行邀请
print("%s, you can join me"%(guests[0]).title())
print("%s, you can join me"%(guests[1]).title())
#最后，对两名成员进行删除，让名单变空
del guests[0]  #这里如果先删除0号的话，那剩下的唯一一个元素就是0号了（-1也行，因为只剩下一个是，是开始也是结束）
del guests[0]  #这里可以使用0/-1
#核实名单变空
print(guests)