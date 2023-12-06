import time

number_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def read_file(location):
    try:
        f = open(location, "r")
        return f.read()
    except Exception as e:
        print("Error while opening file: ", e)
        return None


def transform(input_text):
    """Transforms written numbers to integer strings and replaces lines with the 2 needed numbers and returns the sum

    Checks literals for each line until it finds a numeric number or a written number. Then the same but reversed.

    :param input_text: String with numbers/written numbers
    :return: Sum of numbers
    """

    numbers = []

    for line in input_text.split('\n'):

        new_line = ""
        sub_string = ""
        limit = 0

        # Go through each literal until you find a numeric number or a written number and add it to the new line
        for l in line:

            if l.isnumeric():
                limit += 1
                new_line += l
                break

            sub_string += l
            for number_string in number_dict.keys():
                if number_string in sub_string:
                    new_line += str(number_dict[number_string])
                    break
            if len(new_line) != limit:
                limit += 1
                break

        sub_string = ""

        # Does the same but backwards
        for l in reversed(line):

            if l.isnumeric():
                new_line += l
                break

            sub_string += l
            for number_string in number_dict.keys():
                if number_string in sub_string[::-1]:
                    new_line += str(number_dict[number_string])
                    break

            if len(new_line) > limit:
                break

        if new_line != "":
            numbers.append(int(new_line))

    return sum(numbers)


start = time.time()

input_string = read_file("1_input.txt")

print(transform(input_string))

end = time.time()

print(f"{(end - start) * 1000}ms")
