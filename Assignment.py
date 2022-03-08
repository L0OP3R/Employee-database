#mylist = []

#for i in range(1,11):
 #   mylist.append(i)

#for num in mylist:

 #   if num % 2 == 0:
  #      print(num)

#inbetween 2-100 which is divisible b seven
new_list = []
for i in range(2,100):
    new_list.append(i)
for num in new_list:
    if num % 7 == 0:
        print(num)


myList = []
for i in range(1,100):
    if(i%7==0):
        myList.append(i)
print(myList)
List = [i for i in range(1,101) if i%7 == 0]
print(List)

N1 = [i.lower() for i in ["HELLO", "SAMPLE"]]
print(N1)
