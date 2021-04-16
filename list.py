# list extend method added the specified items to  already list

food = ["bread", "rice", "beans", "fufu", "eba"]
method = food.extend(["spag","indomie"])
print(food)

#list extend method added the specified items to  already list
# note append method add the list as list type

food = ["bread", "rice", "beans", "fufu", "eba"]
method2 = food.append(["spag", "indomie"])
print(food)

# list pop method remove the specified items and display it

food = ["bread", "rice", "beans", "fufu", "eba"]
method3 = food.pop(0)
print(method3)

# list clear method delete all the items in list without display it 
food = ["bread", "rice", "beans", "fufu", "eba"]
method4 = food.clear()
print(food)

# list remove method delete specified items in the list  
food = ["bread", "rice", "beans", "fufu", "eba"]
method5 = food.remove("beans")
print(food)

# list copy method returns the duplicate the original list
food = ["bread", "rice", "beans", "fufu", "eba"]
method6 = food.copy()

# if condition statement confirmed that the items copy by list method is not the same with already list
if method == food:
	print("they are the same")
else:
	print("not the same")

# list insert method add the specified items to already list in provided position
food = ["bread", "rice", "beans", "fufu", "eba"]
method7 = food.insert(0,"ugu")
print(food)

# list sort method arrange already  unarrange list in alphabetical oder or number
food = ["bread", "rice", "beans", "fufu", "eba"]
method8 = food.sort()
print(food)

# list reverse method returns the list in a reverse position
food = ["bread", "rice", "beans", "fufu", "eba"]
method9 = food.reverse()
print(food)

# list index method returns the  index of specified items in the list
food = ["bread", "rice", "beans", "fufu", "eba"]
method10 = food.index("rice")
print(method10)

# return the number of times items appears in the list
number = [1,2,3,4,5,6,7,7,8,9,3,4,9]
method11 = number.count(3)
print(method11)
print(number.count(7))
print(number.count(9))
print(number.count(5))

# python program that added two list together
number1 = [1,2,3,4,5,6]
number2 = [7,8,9,10]
method12 = number1.extend(number2)
print(number1)

words = ["Coding " "Is", "Fun"]
word2 = ["python"]
method13 = " ".join(words)
method14 = words.extend(word2)
print(method13)
print(words)