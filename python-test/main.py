from input import data, criteria

def filter_and_sort(entry, criteria):
    def matches_criteria(item, criteria):
        for key, op, value in criteria:
            if op == '=' and not item.get(key) == value:
                return False
            elif op == '>' and not item.get(key) > value:
                return False


def main():
    # todo: code here
    pass


if __name__ == '__main__':
    main()
