import random
import sys

if sys.version.startswith('2'):
    get_user_input = raw_input
else:
    get_user_input = input

filename = "20k.txt"


def get_random_lines(file, num_of_lines):
    file.seek(0, 2)
    last_char = file.tell() - 1  # skipping EOF position with -1

    lines = []
    for _ in range(num_of_lines):
        position = random.randint(0, last_char)
        lines.append(get_line(file, position))

    return lines


def get_line(file, position):
    start_position = position
    while True:
        file.seek(position)
        symbol = file.read(1)
        if symbol == '\n' and file.tell() != start_position + 1:  # get line when reaches \n, and when \n was not the first match
            return file.readline().rstrip()

        elif position == 0:                                       # get symbol + rest of the line when reaches start of file
            return symbol + file.readline().rstrip()

        else:
            position -= 1


def main(filename):
    with open(filename) as words_file:
        while True:
            try:
                length = get_user_input('Enter number of words: ')
                length = int(length)
                print(' '.join(get_random_lines(words_file, length)))
            except ValueError:
                print('Please enter a valid integer number or use CTRL+c to exit.')
            except KeyboardInterrupt:
                print('\nHave a nice day!')
                sys.exit(0)
            except:
                raise
                sys.exit(1)


if __name__ == '__main__':
    main(filename)
