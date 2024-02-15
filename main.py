import gpt
import csv
from openai import OpenAI
from dotenv import load_dotenv


def get_client() -> OpenAI:
    load_dotenv("key")
    return OpenAI()


def parse_data(filename: str) -> list[list]:
    with open(filename) as f:
        f = csv.reader(f)
        next(f)
        return list(f)


def parse_sample(filename: str = "sample.txt") -> str:
    with open(filename) as f:
        return "".join(f)


def generate_summaries(
    data: list[str], client: OpenAI, sample: str, print_progress: bool = True
) -> list[str]:
    summaries = []
    for i in range(len(data)):
        row = data[i]
        if print_progress:
            print(f"Generating comments... {int(i / len(data) * 100)}%")
        summaries.append(gpt.generate_comment(client, *row, sample))
    return summaries


def write_csv(data: list[str], sample: list[str]):
    with open("comments.csv", "w") as f:
        f.write("Name, Comment\n")
        for row, one_sample in zip(data, sample):
            f.write(f'{row[2]}, "{one_sample}"\n')


def main() -> None:
    print("Hi, welcome to the comment writing helper program")
    print(
        "To begin, please fill out the spreadsheet template by following the link below"
    )
    print(">>> bit.ly/comment-template <<<\n")
    print("Once you finish, hit enter")
    input()
    print(
        "Great! Now in your spreadsheet, click File->Download->"
        "Comma Separated Values (.csv) and paste the file into "
        "the same directory as the program"
    )
    print("Please enter the name of your file")

    data = parse_data(input("> "))

    print("Sample texts can improve the quality of the generated content.")

    while (
        a := input(
            "Would you like to provide a sample of your past comment? (y/n)"
        ).lower()
    ) not in ["y", "n", "yes", "no"]:
        pass

    if a == "y" or a == "yes":
        print("Please enter your sample text in sample.txt, when you finish, hit enter")
        input()

    summaries = generate_summaries(data, get_client(), parse_sample())

    write_csv(data, summaries)

    print("All comments written to comments.csv")


if __name__ == "__main__":
    main()
