from source import utils as u
from source import parser as p
import os


def main():
    directory = "./user_story_inputs/"
    file_name = f"{os.listdir(directory)[0]}"
    file_path = os.path.join(directory, file_name)
    input_file = u.read_file(file_path)
    p.text_to_number(input_file)


if __name__ == "__main__":
    main()
