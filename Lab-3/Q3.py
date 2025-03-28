from collections import defaultdict


def generate_word_count(filename: str) -> defaultdict:
    words = []
    word_count = defaultdict(int)

    with open(filename) as file:
        file_content = file.read()
        words = file_content.split()

    for word in words:
        word_count[word] += 1

    return word_count


def main():
    filename = input('Enter the file name: ')
    word_count = generate_word_count(filename)

    word_count_list = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for i in range(10):
        print(word_count_list[i])


if __name__ == '__main__':
    main()
