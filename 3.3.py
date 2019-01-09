#3-8
scenery = ["japan", "norway", "hawaii", "antarctica", "arctic", "rome"]
print(scenery)
print(sorted(scenery,reverse=False)) #sorted的其中一个参数默认就是reverse=False，所以可以不用额外写上去
print(scenery) #确认顺序未被改变
print(sorted(scenery, reverse=True))
print(scenery) #确认顺序未被改变
scenery.reverse() #将list倒序
print(scenery) #确认顺序变为倒序
scenery.reverse() #再次将list倒序，恢复为原样
print(scenery) #确认恢复为原样
scenery.sort() #按照首字母顺序排序（改变原）
print(scenery) #确认按照首字母顺序排序
scenery.sort(reverse=True) #改为首字母倒序
print(scenery) #确认改为首字母倒序

print("----------------------------")

#3-9（使用3-4）
guests = ["eric", "tim","xu"]
member_nums = len(guests)
print(member_nums)

print("--------------------------------------")

#3-10
moutains = ["huang", "hua", "wu dang"]
moutains.append("qian ling")
moutains.insert(2,"xi feng")
print("喔，我想起来了，中国还有这些山：%s, %s"%(moutains[-1],moutains[2]))
print("对不起啊~，%s 不是名山"%(moutains.pop(2)))
print("啊啊，我不太喜欢%s, 删了吧"%(moutains[0]))
moutains.remove("huang")
print("emmmmm, 华山派我不喜欢，%s也删了把"%(moutains[0]))
del moutains[0]
print("啊，现在又少了：", end = "")
print(moutains[0]+", "+moutains[1])
print("算了给他们两排序算了，emmm按照字母表顺序排吧")
moutains.sort()
print("排好了:", end = "")
print(moutains[0]+", "+moutains[1])
print("再来倒序排排吧：", end = "")
moutains.sort(reverse=True)
print(moutains[0]+", "+moutains[1])
print("额。。。没办法题目要求我们继续，我们就继续吧")
print("接下来是sorted的临时排序时间:")
print(sorted(moutains))
print("然后。。。临时倒序:", end = "")
print(sorted(moutains,reverse=True))
print("啊要死了终于要结束了，接下来是列表长度！！")
print(len(moutains))
