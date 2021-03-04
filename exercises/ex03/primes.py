"""EX03 - prime functions."""

__author__: str = "730386091"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(3))
    print(is_prime(6))
    print(is_prime(31))
    print(is_prime(110))
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))


def is_prime(test: int) -> bool:
    """Determines if prime."""
    denom: int = 2
    while denom < test:
        if test % denom == 0 or test < 0:
            return False
        denom += 1
    return True


def list_primes(a: int, b: int) -> list[int]:
    """List of primes."""
    num: int = a
    ans: list = []
    while num <= b:
        if is_prime(num) is True:
            ans.append(num)
            num += 1
        else:
            num += 1
    return ans 


if __name__ == "__main__":
    main()