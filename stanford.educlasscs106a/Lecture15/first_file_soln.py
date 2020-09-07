'''
Read all the lines in the file holdup.txt
and print them to the screen
'''

def main():
    for line in open('holdup.txt'):
        line = line[:-1]
        print(line)

if __name__ == '__main__':
    main()
