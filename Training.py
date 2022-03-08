vowels = "AEIOUaeiou"
name = "VAmsiKrishna"

count = 0

for i in name:
    for j in vowels:
        if(i==j):
            count+=1

print(count)