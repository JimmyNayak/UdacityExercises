def read_file():
    f = open('script/script_demo', 'r')
    file_data = f.read()
    f.close()
    return file_data


def write_file(text):
    f = open('script/script_demo', 'w')
    f.write(text)
    f.close()


# text_data = input("Enter text to write in the file: ")
#
# write_file(text_data)
#
# print(read_file())


#
# Too Many Open Files
# Run the following script in Python to see what happens when you open too many files without closing them!

# files = []
# for i in range(10000):
#     files.append(open('script/script_demo', 'r'))
#     print(i)


# With
# Python provides a special syntax that auto-closes a file for you once you're finished using it.

# with open('script/script_demo', 'r') as f:
#     file_data = f.read()
#     print(file_data)

# Calling the read Method with an Integer
# with open("script/camelot") as song:
#     print(song.read(2))
#     print(song.read(8))
#     print(song.read())


# camelot_lines = []
# with open("script/camelot") as f:
#     for line in f:
#         camelot_lines.append(line.strip())
#
# print(camelot_lines)


def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    # use the for loop syntax to process each line
    # and add the actor name to cast_list

    with open(f'script/{filename}', 'r') as file:
        for line in file:
            cast_list.append(line.split(",")[0])
    return cast_list


cast_list = create_cast_list('flying_circus_cast')
for actor in cast_list:
    print(actor)
