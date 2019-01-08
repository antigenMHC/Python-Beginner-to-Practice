#2-3
name = "eric"
print(("hello %s,how do you do"%(name)).title())#用括号将想要使用title方法（函数）包起来即可

#2-4
name2 = "diary"
print(name2.upper())
print(name2.lower())
print(name2.title())

#2-5 and 2-6
sayer_name = "zhang"
say = '"i talk : OOP is  amazing"'
print("%s once said,%s"%(sayer_name.title(),say))

#2-7
name3 = " antigenMHC\n"
name4 = "\tantigenMHC  "
name3 = name3.lstrip()
name3 = name3.rstrip("\n")
name4 = name4.lstrip("\t")
name4 = name4.rstrip()
print(name3)
print(name4)
