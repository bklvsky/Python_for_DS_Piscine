import sys


def get_arg() -> int:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if len(sys.argv) == 1:
        return None
    try:
        result = int(sys.argv[1])
    except ValueError:
        raise AssertionError("Argument is not an integer")
    return result


def odd_or_even(num: int) -> None:
    if num is None:
        return
    if num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


try:
    arg = get_arg()
    odd_or_even(arg)
except AssertionError as e:
    print(f"{type(e).__name__}: {e}")
