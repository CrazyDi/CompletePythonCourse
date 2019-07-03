import csv

movies = [
    {'name': 'The Matrix', 'director': 'Wachowski'},
    {'name': 'Green Book', 'director': 'Farelly'},
    {'name': 'Amadeus', 'director': 'Forman'}
]


def write_to_file(output):
    with open('file.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'director'])
        writer.writeheader()
        writer.writerows(output)


def read_from_file():
    with open('file.csv', 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


if __name__ == "__main__":
    write_to_file(movies)
    print(read_from_file())