x= [int(i) for i in input("numbers-").split(",")]
square_number = list(map(lambda i:i**2,x))
cube_number = list(map(lambda i:i**3,x))
print(square_number)
print(cube_number)