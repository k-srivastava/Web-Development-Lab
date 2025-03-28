from itertools import permutations


class Permutations:
    def __init__(self, numbers: list[int]):
        self.numbers = numbers

    def generate_all_permutations(self):
        return list(permutations(self.numbers))


def main():
    numbers = [int(number) for number in input('Enter a list of numbers: ').split()]
    all_permutations = Permutations(numbers).generate_all_permutations()

    print(f'Permutations: {all_permutations}')


if __name__ == '__main__':
    main()
