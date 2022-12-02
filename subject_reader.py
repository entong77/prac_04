FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    subject_info(data)


def get_data():
    input_file = open(FILENAME)
    list_of_lists = []
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        print("----------")
        list_of_lists.append(parts)
    input_file.close()
    return list_of_lists


def subject_info(lists):
    for element in lists:
        print("{} is taught by {:12} and has {:3} students".format(element[0], element[1], element[2]))


main()
