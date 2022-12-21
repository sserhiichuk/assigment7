import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--all", required=True)
    parser.add_argument("--filename", "-f", required=True)
    parser.add_argument("--medals", "-m", action="store_true", required=False)
    parser.add_argument("--country", "-c", nargs='+', required=False)
    parser.add_argument("--year", "-y", required=False)
    parser.add_argument("--noc", required=False)
    parser.add_argument("--overall", required=False)
    parser.add_argument("--output", "-o", action="store_true", required=False)

    args = parser.parse_args()

    if args.all == "medals":
        taks1(args.filename, args.country, args.year, args.noc, args.output)
    elif args.all == "total":
        task2(args.filename, args.year)
    elif args.all == "overall":
        task3(args.filename, args.country)
    if args.all == 'interactive':
        task4()


# python main.py --all medals --filename olimpic.tsv --country Ukraine --year 2000 -o
def taks1(filename, country, year, noc, output):
    gold = 0
    silver = 0
    bronze = 0
    counter = 0
    results = ""

    with open(filename, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            data = line.strip().split("\t")
            if data[14] != "NA":
                if (data[6] == country or data[7] == noc) and data[9] == year:
                    if data[14] == 'Gold':
                        gold += 1
                    elif data[14] == 'Silver':
                        silver += 1
                    elif data[14] == 'Bronze':
                        bronze += 1
                    if counter < 10:
                        counter += 1
                        result = f'{data[1]} - {data[12]} - {data[14]}\n'
                        print(result.strip())
                        results += result
        how_many_medals = f'golds medals - {gold}, silver medals - {silver}, bronze medals - {bronze}'
        print(how_many_medals)
        if output:
            with open("new_file", "w") as file:
                file.write(f"{results}\n {how_many_medals}")


# python main.py --all total  --filename olimpic.tsv --year 2000


def task2(filename, year):
    d = dict()
    with open(filename, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            data = line.strip().split("\t")
            country = data[6]
            if data[9] == year and data[14] != "NA":
                if country not in d:
                    d[country] = [0, 0, 0]
                # elif year not in d[country]:
                #     d[country][year] = [0, 0, 0]
                if data[14] == "Gold":
                    d[country][0] += 1
                if data[14] == "Silver":
                    d[country][1] += 1
                if data[14] == "Bronze":
                    d[country][2] += 1
    for country, medals in d.items():
        print(country, medals)


def task3(filename, all_country):
    print(all_country)

    countries = {}
    for i in all_country:
        countries[i] = dict()
    print(countries)

    with open(filename, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            data = line.strip().split("\t")
            years_data = data[9]
            medals_data = data[14]
            counrty_data = data[6]


def task4():
    user_input = input('Enter country')
    with open('olimpic.tsv', "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
        data = line.strip().split("\t")


main()
