from math import fabs

FILE_LINE_SEPARATOR = "   "

class HistoricallySignificantLocationsFileRepository:

    def __init__(self, filename: str):
        self.filename = filename

    def get_locations(self) -> list[list[int]]:
        locations_lists = [
            [],
            []
        ]

        with open(self.filename, 'r') as fd:
            for line in fd.readlines():
                first_elem, second_elem = line.split(FILE_LINE_SEPARATOR)      
                locations_lists[0].append(int(first_elem))
                locations_lists[1].append(int(second_elem))

        return locations_lists

def main(file_repo):
    localtion_lists = file_repo.get_locations()

    localtion_lists[0].sort()
    localtion_lists[1].sort()
    
    difference = 0
    size_list = len(localtion_lists[0])
    for i in range(0, size_list):
        if i < 10:
            print(f"{localtion_lists[0][i]}-{localtion_lists[1][i]}")

        difference += fabs(localtion_lists[0][i] - localtion_lists[1][i])

    print(difference)

if __name__ == "__main__":
    file_repo = HistoricallySignificantLocationsFileRepository('input.txt')
    main(file_repo)
