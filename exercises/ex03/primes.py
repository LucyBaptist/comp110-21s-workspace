"""EX03 - prime functions."""

__author__: str = "730386091"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(is_prime(5)), print(list_primes(10, 20))


def is_prime(test: int) -> bool:
    denom: int = 2
    while denom < test:
        if test % denom == 0:
            ans: bool = True
            return ans
        else: 
            ans: bool = False
            return ans
        denom += 1
    return ans


if __name__ == "__main__":
    main()