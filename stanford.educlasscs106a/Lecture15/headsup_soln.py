import random

def main():
    words = load_data()

    while True:
        input('Press enter: ')
        next_word = random.choice(words)
        print('')
        print(next_word)


def load_data():
    words = []
    for line in open('headsup.txt'):
        line = line[:-1]
        words.append(line)
    return words

if __name__ == '__main__':
    main()
