# # write your function here
# def population_density(population, land_area):
#     return population / land_area
#
#
# # test cases for your function
# test1 = population_density(10, 1)
# expected_result1 = 10
# print("expected result: {}, actual result: {}".format(expected_result1, test1))
#
# test2 = population_density(864816, 121.4)
# expected_result2 = 7123.6902801
# print("expected result: {}, actual result: {}".format(expected_result2, test2))


# write your function here
# def readable_timedelta(days):
#     weeks = days // 7
#     remainder = days % 7
#     return "{} week(s) and {} day(s).".format(weeks, remainder)
#
#
# # test your function
# print(readable_timedelta(10))


# def readable_timedelta(days):
#     """
#     Return a string of the number of weeks and days included in days.
#
#     Parameters:
#     days -- number of days to convert (int)
#
#     Returns:
#     string of the number of weeks and days included in days
#     """
#     weeks = days // 7
#     remainder = days % 7
#     return "{} week(s) and {} day(s)".format(weeks, remainder)
#
#
# print(readable_timedelta(10))


# numbers = [
#     [34, 63, 88, 71, 29],
#     [90, 78, 51, 27, 45],
#     [63, 37, 85, 46, 22],
#     [51, 22, 34, 11, 18]
# ]
#
#
# def mean(num_list):
#     return sum(num_list) / len(num_list)
#
#
# # averages = list(map(mean, numbers))
#
# averages = list(map(lambda num: sum(num) / len(num), numbers))
# print(averages)


cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]


def is_short(name):
    return len(name) < 10


# short_cities = list(filter(is_short, cities))
short_cities = list(filter(lambda name: (len(name) < 10), cities))
print(short_cities)
