from input import data, criteria

def filter_and_sort(entry, criteria):
    """
    This function filters the data based on the criteria and sorts the data based on the priority
    :param entry:
    :param criteria:
    :return:
    """
    def matches_criteria(item, criteria):
        """
        This function checks if the item matches the criteria
        :param item:
        :param criteria:
        :return:
        """
        for key, op, value in criteria:
            if op == '=' and not item.get(key) == value:
                return False
            elif op == '>' and not item.get(key) > value:
                return False
            elif op == '>=' and not item.get(key) >= value:
                return False
            elif op == '<' and not item.get(key) < value:
                return False
            elif op == '<=' and not item.get(key) <= value:
                return False
        return True

    filtered_items = [item for item in entry if matches_criteria(item, criteria)]
    remaining_items = [item for item in entry if not matches_criteria(item, criteria)]

    def sort_by_priority(items):
        """
        This function sorts the items based on the priority
        :param items:
        :return:
        """
        n = len(items)
        for i in range(n):
            for j in range(0, n - i - 1):
                if items[j]['priority'] < items[j + 1]['priority']:
                    items[j], items[j + 1] = items[j + 1], items[j]

    sort_by_priority(filtered_items)

    return filtered_items + remaining_items

def main():
    """
    This function prints the sorted data
    :return:
    """
    sorted_data = filter_and_sort(data, criteria)
    for item in sorted_data:
        print(item)

if __name__ == '__main__':
    main()