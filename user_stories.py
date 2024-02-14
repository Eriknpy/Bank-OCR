"""
Task description:
    Each entry is 4 lines long, and each line has 27 characters.
    The first 3 lines of each entry contain an account number written using pipes and underscores,
    and the fourth line is blank. Each account number should have 9 digits, all of which should be in the range 0-9.
    A normal file contains around 500 entries.

Task bullet points:
    - Vertical 4 lines long - the first 3 lines contain an account number and the 4th is blank
    - Each account number should have 9 digits - range 0-9
    - Horizontal 27 chars long
    - A normal file contains around 500 entries

Task goal:
    - Your first task is to write a program that can take this file and parse it into actual account numbers.
"""


def user_story_1(input_text: str):
    by_line_input_text = input_text.split("\n")
    print(by_line_input_text)

    for i in range(len(by_line_input_text)):
        line = ""
        for j in range(len(by_line_input_text[i])):
            if j % 3 == 0:
                line += "X"
            line += by_line_input_text[i][j]

        print(line)



        # print(by_line_input_text[i])
        # if not input_text[i].isspace():
        #     recognise_one_or_four()

def parse_numbers():
    pass

def recognise_one_or_four():
    print("1 or 4")