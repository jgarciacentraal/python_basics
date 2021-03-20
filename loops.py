#while statement

# count = 0
# while count < 10:
#     print("The condition is True")
#     count = count + 1

# print("After the loop")


#for
# items = [1, 2, 3, 4]
# for item in items:
#     print(item)

#range() specifict amount of times
for item in range(5):
    print(item)

# index helping with len()
for index in range(len(values)):
    value = values[index]
    print(index, value) 
# enumarate()
for count, value in enumerate(values):
    print(count, value)       


#When used in conditions, 0, 0.0, and '' (the empty string) are considered False