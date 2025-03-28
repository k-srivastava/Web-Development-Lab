def calculate(numbers: list[int]) -> tuple[float, float, float]:
    mean = sum(numbers) / len(numbers)

    variance = 0
    for number in numbers:
        variance += (number - mean) ** 2
    variance /= len(numbers)

    return mean, variance, variance ** 0.5


def main():
    numbers = [int(number) for number in input('Enter numbers: ').split()]
    mean, variance, std_deviation = calculate(numbers)

    print(f'Mean: {mean}')
    print(f'Variance: {variance}')
    print(f'Standard Deviation: {std_deviation}')


if __name__ == '__main__':
    main()
