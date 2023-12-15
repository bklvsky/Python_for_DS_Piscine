from sys import stdin, argv


def count_characters(input: str):
    """
    Counts and outputs specific types of characters in a string:

    - uppercase letters;

    - lowercase letters;

    - punctuation marks;

    - spaces;

    - digits.
    """

    string_punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    upper = sum(1 for char in input if char.isalpha() and char.isupper())
    lower = sum(1 for char in input if char.isalpha() and char.islower())
    punctuation = sum(1 for char in input if char in string_punctuation)
    spaces = sum(1 for char in input if char.isspace())
    digit = sum(1 for char in input if char.isdigit())

    print(
        f"The text contains {len(input)} "
        + ("character:" if len(input) == 1 else "characters:")
    )
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digit} digits")


def get_argument() -> str:
    """
    Validates command line argument or
    if not provided inquires for manual user input.

    Raises AssertionError in case of more than 1 command line argument.

    Returns the argument provided.
    """
    assert len(argv) <= 2, "more than one argument is provided"
    if len(argv) == 1:
        print("What is the text to count?")
        text = stdin.readline()
        if len(text) > 0 and text[-1] != "\n":
            print()
    else:
        text = argv[1]
    return text


def main():
    """
    Analyzes given text and counts frequency of groups of characters
    (such as digits, lower- or uppercase letters, etc.).

    In case of no argument provided prompts for a user input.

    In case of more than one argument outputs an error.
    """
    try:
        text = get_argument()
        count_characters(text)
    except AssertionError as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
