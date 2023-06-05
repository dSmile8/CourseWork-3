from utils import get_data, get_filtered_data, get_formatted_data, get_last_values


def main():
    FILTERED_EMPTY_FROM = True
    COUNT_LAST_VALUES = 5

    data = get_data()

    data = get_filtered_data(data, filter_empty_from=FILTERED_EMPTY_FROM)
    data = get_last_values(data, count_last_values=COUNT_LAST_VALUES)
    data = get_formatted_data(data)
    print('INFO: Вывод транзакций...')
    for i in data:
        print(i, end='\n\n')

if __name__ == "__main__":
    main()


