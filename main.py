import gpt
from openai import OpenAI
from dotenv import load_dotenv
    
load_dotenv("key")
client = OpenAI()

def main() -> None:
    print(
        gpt.generate_comment(
            client,
            "Chemistry",
            "Brad Brad Anderson",
            "Joe Smith",
            "B+",
            "A",
            "A",
            "Obtain, evaluate, and communicate information in a variety of methods",
            "Engage in appropriate argument from evidence",
            "Eating and Talking at the same time in class",
            "8",
            "3",
        )
    )


if __name__ == "__main__":
    main()
