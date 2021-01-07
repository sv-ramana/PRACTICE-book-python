a = "Hello, World!"
print(a[5])


for x in "banana":
    print(x)

b = "Hello, world"
print(len(b))  #length of the b


text = "yah! world is so beutifull"
print("yah!" in text) # it works whether the text are in line sentence
print("so" not in text)


if "ism" in text:
    print("yes its is evalible")
else:
    print("not available ")


print(b[:5]) #print 5 letters
print(b[5:])
print(b[-5:-2])
print(b.upper())
print(b.lower())
print(b.replace("H", "J"))
print(b.split(","))


# age = 36
# txt = "My name is John, I am " + age
# print(txt)  
 # it will not work 
# FORMAT WILL WORK AS SHOW IN THE EXAMPLE #

cost = 20
peaces = 2
item = 3
myoverall = "i \"brough\" cost of {} and peace of {} of item of {}"
print(myoverall.format(cost, peaces, item))


