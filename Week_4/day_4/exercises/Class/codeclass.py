# 1 Create a function that has 2 parameters:
# Your age, and your friends age.
# Return the older age

# def oldest_age(my_age,friend_age):
#     if my_age > friend_age:
#         return my_age
#     return friend_age

# print(oldest_age(34,23))

# 2. Create a function that takes 2 words
# It must return the lenght of the longer word

# def longest_word(word1, word2):
#     if len(word1) > len(word2):
#         return word1
#     else:
#         return word2

# print(longest_word('toto', 'longest word'))

# 3. Write the max() function yourself...

def max(my_list):
    biggest = my_list[0]
    for num in my_list:
        if num > biggest:
            biggest = num
    return biggest

print(max([1,5,43,2,7]))
print(max([1,5,43,2,7,-3]))
print(max([-1,-5,-43,-2,-7]))

# 4.  Create a function that takes a list as an argument
# The list should contain any number of entries.
# each entry should have a name and grade
# return the name of the person with the highest grade

# def highest_grade(my_list):
#     for key in my_list:
#         for key2 in my_list:
#             if my_list[key]>my_list[key2]:
#                 name = key
#             else:
#                 name = key2
#     return name
    
# print(highest_grade ({'mike':40,'jon':60,'dina':90}))


# Example with default argument
# def say_happy_birthday(name, age, from_name=None):
#     print(f"Happy Birthday {name}! You are {age} years old.")
#     if from_name is not None:
#         print(f"From {from_name}")