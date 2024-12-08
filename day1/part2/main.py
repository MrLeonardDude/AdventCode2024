FILE_LINE_SEPARATOR = "   "


class SecondList:
    """Structure specified for second list since we need to check if a value was seen
    and how many times it was
    """

    def __init__(self):
        self.elements = set()
        self.elements_counter = dict()


class HistoricallySignificantLocationsFileRepository:

    def __init__(self, filename: str):
        self.filename = filename

    def get_locations(self):
        first_list = []

        second_list = SecondList()

        with open(self.filename, "r") as fd:
            for line in fd.readlines():
                first_elem, second_elem = line.split(FILE_LINE_SEPARATOR)
                first_list.append(int(first_elem))
                
                if int(second_elem) not in second_list.elements:
                    second_list.elements_counter[int(second_elem)] = 1
                    second_list.elements.add(int(second_elem))
                else:
                    second_list.elements_counter[int(second_elem)] += 1

        return first_list, second_list


def main(file_repo):
    first_list, second_list = file_repo.get_locations()

    similarity_score = 0
    size_list = len(first_list)
    for i in range(0, size_list):
        similarity_score += first_list[i] * second_list.elements_counter.get(
            first_list[i], 0
        )

    print(f"The solution is {similarity_score}")

if __name__ == "__main__":
    file_repo = HistoricallySignificantLocationsFileRepository("../input.txt")
    main(file_repo)
