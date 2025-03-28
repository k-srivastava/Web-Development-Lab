def sort_and_write(input_file: str, output_file: str):
    with open(input_file) as file:
        contents = file.read()

    new_contents = contents[::-1]
    with open(output_file, 'w') as file:
        file.write(new_contents)


def main():
    input_file = input('Enter the input file name: ')
    output_file = input('Enter the output file name: ')

    sort_and_write(input_file, output_file)


if __name__ == '__main__':
    main()
