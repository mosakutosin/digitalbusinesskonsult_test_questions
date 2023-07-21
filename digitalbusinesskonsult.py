print("----- Question 4 ---------")

# write a program that finds the missing number in a given integer array of 1 to 10 …arr = [1,2,3,4,5,6,7,8,10]

array_list = [1,2,3,4,5,6,7,8,10]
missing_elements = []

for miss in range(array_list[0], array_list[-1]+1):
    if miss not in array_list:
        missing_elements.append(miss)

print("The missing value is : " + str(missing_elements))


print("\n\n----- Question 5 ---------")

# Remove all even integers from an array Input: [4, 1, 9, 10, 15, 22, 5, 14]

lists = [4, 1, 9, 10, 15, 22, 5, 14]

for i in lists:
    if i % 2 == 0:
        lists.remove(i)

        print(lists)
