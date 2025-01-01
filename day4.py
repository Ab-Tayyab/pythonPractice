# list
# task 1 
# str1 = input("Enter value 1: ")
# str2 = input("Enter value 2: ")
# str3 = input("Enter value 3: ")

# mainList = []
# mainList.append(str1)
# mainList.append(str2)
# mainList.append(str3)

# print(mainList)

# task 2 

pList = [1,"abc",1,]
copyList = pList.copy()
copyList.reverse()
if(pList == copyList):
    print("List is palindrom")
else:
    print("list is not palindrom")