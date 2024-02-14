from user_stories import user_story_1
import os


def main():
    directory = "./user_story_inputs/"
    file_name = f"{os.listdir(directory)[0]}"
    file_path = os.path.join(directory, file_name)
    input_file = get_user_story_content(file_path)
    user_story_1(input_file)


def get_user_story_content(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()


if __name__ == "__main__":
    main()
