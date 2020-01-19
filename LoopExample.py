# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []
#
# # write your for loop here
# for name in names:
#     usernames.append(name.replace(' ', '_').lower())
#
# print(usernames)


# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# for name in names:
#     name = name.lower().replace(" ", "_")
#
# print(names)


# usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
#
# # write your for loop here
# for index in range(len(usernames)):
#     usernames[index] = usernames[index].lower().replace(' ', '_')
#
# print(usernames)


# tokens = ['<greeting>', 'Hello World!', '</greeting>']
# count = 0
#
# # write your for loop here
# for index in range(len(tokens)):
#     if tokens[index].startswith('<') and tokens[index].endswith('>'):
#         count += 1
#
# print(count)


# items = ['first string', 'second string']
# html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
# # the characters that are after it in html_str are on the next line
#
# # write your code here
# for item in items:
#     html_str += "<li>{}</li>\n".format(item)
# html_str += "</ul>"
#
# print(html_str)


# colors = ['Red', 'Blue', 'Green', 'Purple']
# lower_colors = []
#
# for color in colors:
#     lower_colors.append(color.lower())
#
# print(lower_colors)


# # number to find the factorial of
# number = 6
#
# # start with our product equal to one
# product = 1
#
# # track the current number being multiplied
# current = 1
#
# # write your while loop here
#
# while current <= number:
#     product *= current
#     current+=1
#
#
# # multiply the product so far by the current number
#
#
# # increment current with each iteration until it reaches number
#
#
# # print the factorial of number
# print(product)


# # number to find the factorial of
# number = 6
#
# # start with our product equal to one
# product = 1
#
# # track the current number being multiplied
# current = 1
#
# # write your while loop here
#
# for num in range(2, number + 1):
#     product *= num
#
# # multiply the product so far by the current number
#
#
# # increment current with each iteration until it reaches number
#
#
# # print the factorial of number
# print(product)


# start_num = 2  # provide some start number
# end_num = 100  # provide some end number that you stop when you hit
# count_by = 2  # provide some number to count by
#
#
# # write a while loop that uses break_num as the ongoing number to
# #   check against end_num
# break_num = start_num
# while break_num < end_num:
#     break_num += count_by
#     print(break_num)
#
# print(break_num)


# start_num = 1  # provide some start number
# end_num = 100  # provide some end number that you stop when you hit
# count_by = 2  # provide some number to count by
#
# # write a condition to check that end_num is larger than start_num before looping
# # write a while loop that uses break_num as the ongoing number to
# #   check against end_num
#
# if start_num > end_num:
#     print("Oops! Looks like your start value is greater than the end value. Please try again.")
# else:
#     result = start_num
#     while result < end_num:
#         result += count_by
#
#
# print(result)


# limit = 40
#
# # write your while loop here
# num = 0
# while (num + 1) ** 2 < limit:
#     num += 1
# nearest_square = num ** 2
#
# print(nearest_square)


# num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45,
#             149, 59, 84, 69, 113, 166]
#
# count_odd = 0
# list_sum = 0
# i = 0
# len_num_list = len(num_list)
#
# while (count_odd < 5) and (i < len_num_list):
#     if num_list[i] % 2 != 0:
#         list_sum += num_list[i]
#         count_odd += 1
#     i += 1
#
# print("The numbers of odd numbers added are: {}".format(count_odd))
# print("The sum of the odd numbers added is: {}".format(list_sum))


# HINT: modify the headlines list to verify your loop works with different inputs
# headlines = ["Local Bear Eaten by Man",
#              "Legislature Announces New Laws",
#              "Peasant Discovers Violence Inherent in System",
#              "Cat Rescues Fireman Stuck in Tree",
#              "Brave Knight Runs Away",
#              "Papperbok Review: Totally Triffic"]
#
# news_ticker = ""
# # write your loop here
# for line in headlines:
#
#     if len(news_ticker) > 140:
#         news_ticker = news_ticker[0:140]
#         break
#     else:
#         news_ticker += line+" "
#         # print(news_ticker)
#
# print(news_ticker)



#
# ## Your code should check if each number in the list is a prime number
# check_prime = [26, 39, 51, 53, 57, 79, 85]
#
# ## write your code here
# ## HINT: You can use the modulo operator to find a factor
#
# for num in check_prime:
#     for i in range(2, num):
#         if (num % 2) == 0:
#             print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
#             break
#         if i == num - 1:
#             print("{} IS a prime number".format(num))
