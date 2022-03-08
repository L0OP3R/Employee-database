#vamsi = input("Enter a phrase: ")
#print("Small= ", min(vamsi).upper())
#print("Large= ", max(vamsi).upper())
i = 0
while i < 9:
    i = i+1
    if i == 3:
        pass
        print('pass')
    print(i)
print("enter a number")
text = input()
text_list = list(text.split(" "))
print(text_list)
sort_list = sorted(text_list, key=len)
print(sort_list[-1])

def add(a, b):
    c=a+b
    print(c)

x=10
y=20

add(x,y)