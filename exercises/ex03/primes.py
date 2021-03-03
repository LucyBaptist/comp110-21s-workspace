"""EX03 - prime functions."""

__author__: str = "730386091"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(3))
    print(is_prime(6))
    print(is_prime(31))
    print(is_prime(110))
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))


def is_prime(test: int) -> bool:
    denom: int = 2
    while denom < test:
        if test % denom == 0:
            return True
        denom += 1
    return False


if __name__ == "__main__":
    main()