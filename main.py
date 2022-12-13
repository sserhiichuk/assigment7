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