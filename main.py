import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--all", required=True)
    parser.add_argument("--filename", "-f", required=True)
    parser.add_argument("--medals", "-m", action="store_true", required=False)
    parser.add_argument("--country", "-c", required=False)
    parser.add_argument("--year", "-y", required=False)
    parser.add_argument("--noc", required=False)
    parser.add_argument("--output", "-o", action="store_true", required=False)

    args = parser.parse_args()

    if args.all == "medals":
        taks1(args.filename, args.country, args.year, args.noc, args.output)
    elif args.all == "total":
        task2(args.filename, args.year)
    elif args.all == "overall":
        task3(args.filename, args.country)


def taks1(filename, country, year, noc, output):
    gold = 0
    silver = 0
    bronze = 0
    counter = 0
    result = ""
    result_list = ""

    with open(filename, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            data = line.strip().split("\t")
            if data[14] != "NA":
                if data[6] == country or data[7] == noc and data[9] == year:
                    counter += 1
                    if counter < 11:
                        if data[14] == 'Gold':
                            gold += 1
                        elif data[14] == 'Silver':
                            silver += 1
                        elif data[14] == 'Bronze':
                            bronze += 1
                            result += f'{data[1]} - {data[12]} - {data[14]}\n'
                            result_list = str(result_list) + "".join(result)
                        elif counter == 10:
                            break
                        how_many_medals = f'golds medals - {gold}, silver medals - {silver}, bronze medals - {bronze}'
                        print(result_list)
        print(how_many_medals)
        if output:
            with open("new_file", "w") as file:
                file.write(f"{result_list}\n {how_many_medals}")


def task2(filename, year):
    with open(filename, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            data = line.strip().split("\t")
            if data[9] == year:
                if data[14] != 'NA':
                    result = f'{data[6]} - {data[14]}'
                    print(result)


def task3(filename, country):
    every_country = country.split(',')
    print(every_country)
    idx = 0
    current_country = every_country[idx]
    gold = 0
    silver = 0
    bronze = 0

    print(every_country[idx])
    with open(filename, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            data = line.strip().split("\t")
            if current_country == data[6]:
                for current_country in line:
                    if data[14] != "NA":
                        if data[14] == 'Gold':
                            gold += 1
                        elif data[14] == 'Silver':
                            silver += 1
                        elif data[14] == 'Bronze':
                            bronze += 1
                result = f'{current_country} - {gold} - {silver} - {bronze}\n'
                idx += 1
                print(result)


main()
