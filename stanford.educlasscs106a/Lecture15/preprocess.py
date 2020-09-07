import csv

def main():
    lines = open('us-cities-java.txt').readlines()
    clean_lines = []
    for line in lines:
        clean_lines.append(line[:-1])
    n_cities = len(clean_lines) // 3
    print(n_cities)
    tripplets = make_run(clean_lines, 3)
    print(len(tripplets))
    writer = open('us-cities.txt', 'w')
    for city in tripplets:
        line = city[0] + ',' + city[1] + ',' + city[2]
        line = line.replace(' ', '')
        writer.write(line + '\n')



def make_run(data, k):
    curr = []
    runs = []
    for v in data:
            curr.append(v)
            if len(curr) == k:
                    runs.append(curr)
                    curr = []
    return runs		

if __name__ == '__main__':
    main()
