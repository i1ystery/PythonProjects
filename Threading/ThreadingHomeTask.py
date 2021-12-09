import threading
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from enum import Enum, auto
from itertools import repeat


class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    CYAN = auto()


record_list = []          # Used for storing all records
unique_values = set()     # Used for storing unique variables
stop_threads = False      # Used for stopping threads when it's needed
record_count = 0          # Used for counting matched record by category in method count_by_category()
found_record = None       # Used for storing found record from method find_by_value()
lock = threading.Lock()   # Used for locking threads when counting in record_count


def create_record(unique_val: int, int_val: int, str_val: str, enum_val: Color) -> tuple[int, int, str, Color]:
    """
    Creates a record that is eligible to be put into record list.

    :return: New record as tuple with specified values
    """
    assert isinstance(unique_val, int) and isinstance(int_val, int)
    assert unique_val not in unique_values
    assert isinstance(str_val, str) and isinstance(enum_val, Color)
    record = (unique_val, int_val, str_val, enum_val)
    unique_values.add(unique_val)
    return record


def append_records(records_list: list):
    """
    Inserts data into defined list.
    """
    assert isinstance(records_list, list)
    records_list.append(create_record(1, 100, 'a', Color.RED))
    records_list.append(create_record(2, 200, 'b', Color.RED))
    records_list.append(create_record(3, 300, 'c', Color.GREEN))
    records_list.append(create_record(4, 400, 'd', Color.RED))
    records_list.append(create_record(5, 500, 'e', Color.GREEN))
    records_list.append(create_record(6, 600, 'f', Color.CYAN))
    records_list.append(create_record(7, 700, 'g', Color.BLUE))
    records_list.append(create_record(8, 800, 'h', Color.CYAN))
    records_list.append(create_record(9, 900, 'i', Color.RED))
    records_list.append(create_record(10, 1000, 'j', Color.GREEN))
    records_list.append(create_record(11, 1100, 'k', Color.GREEN))
    records_list.append(create_record(12, 1200, 'l', Color.RED))
    records_list.append(create_record(13, 1300, 'm', Color.CYAN))
    records_list.append(create_record(14, 1400, 'n', Color.CYAN))
    records_list.append(create_record(15, 1500, 'o', Color.GREEN))
    records_list.append(create_record(16, 1600, 'p', Color.GREEN))
    records_list.append(create_record(17, 1700, 'q', Color.RED))
    records_list.append(create_record(18, 1800, 'r', Color.GREEN))
    records_list.append(create_record(19, 1900, 's', Color.GREEN))
    records_list.append(create_record(20, 2000, 't', Color.RED))
    records_list.append(create_record(51, 100, 'a', Color.RED))
    records_list.append(create_record(21, 2100, 'u', Color.CYAN))
    records_list.append(create_record(22, 2200, 'v', Color.BLUE))
    records_list.append(create_record(23, 2300, 'w', Color.CYAN))
    records_list.append(create_record(24, 2400, 'x', Color.RED))
    records_list.append(create_record(25, 2500, 'y', Color.GREEN))
    records_list.append(create_record(26, 2600, 'z', Color.BLUE))
    records_list.append(create_record(27, 2700, 'a', Color.CYAN))
    records_list.append(create_record(28, 2800, 'b', Color.CYAN))
    records_list.append(create_record(29, 2900, 'c', Color.CYAN))
    records_list.append(create_record(30, 3000, 'd', Color.RED))
    records_list.append(create_record(31, 3100, 'e', Color.CYAN))
    records_list.append(create_record(32, 3200, 'f', Color.RED))
    records_list.append(create_record(33, 3300, 'g', Color.CYAN))
    records_list.append(create_record(34, 3400, 'h', Color.BLUE))
    records_list.append(create_record(35, 3500, 'i', Color.GREEN))
    records_list.append(create_record(36, 3600, 'j', Color.CYAN))
    records_list.append(create_record(37, 3700, 'k', Color.RED))
    records_list.append(create_record(38, 3800, 'l', Color.BLUE))
    records_list.append(create_record(39, 3900, 'm', Color.CYAN))
    records_list.append(create_record(40, 4000, 'n', Color.BLUE))
    records_list.append(create_record(41, 4100, 'o', Color.CYAN))
    records_list.append(create_record(42, 4200, 'p', Color.RED))
    records_list.append(create_record(43, 4300, 'q', Color.CYAN))
    records_list.append(create_record(44, 4400, 'r', Color.BLUE))
    records_list.append(create_record(45, 4500, 's', Color.BLUE))
    records_list.append(create_record(46, 4600, 't', Color.RED))
    records_list.append(create_record(47, 4700, 'u', Color.CYAN))
    records_list.append(create_record(48, 4800, 'v', Color.CYAN))
    records_list.append(create_record(49, 4900, 'w', Color.BLUE))
    records_list.append(create_record(50, 5000, 'x', Color.RED))
# append_records(record_list)  # Insert data into record_list


def split_list(records_list: list[tuple]):
    """
    Splits list into parts as lists to increase search speed.

    :param records_list: list with records
    :return: list of split parts of the original list
    """
    split_list_length = len(records_list) // 4
    split_1 = records_list[0:split_list_length]
    split_2 = records_list[split_list_length:split_list_length * 2]
    split_3 = records_list[split_list_length * 2:split_list_length * 3]
    split_4 = records_list[split_list_length * 3: len(records_list)]
    return [split_1, split_2, split_3, split_4]


def find_by_value(value, searching_list: list[tuple]):
    """
    Finds record with a specified value from specified list.

    :param searching_list: list that contains records
    :param value: int/str/Enum value to be found in records
    :return: record from specified list that has specified value
    """
    global stop_threads
    global found_record
    for record in searching_list:
        if not stop_threads:
            if value in record:
                found_record = record
                stop_threads = True
                break


def start_find_by_value(value):
    """
    Finds record with specified value in record_list using threads to increase search speed.
    Uses split_list and find_by_value methods to increase search speed.

    :param value: int/str/Enum value to be found in records
    :return: record from record_list that has specified value
    """
    assert isinstance(value, int) or isinstance(value, str) or isinstance(value, Color)
    split = split_list(record_list)
    with ThreadPoolExecutor(max_workers=len(split)) as executor:
        executor.map(find_by_value, repeat(value), split)
    return found_record


def find_all_by_values(values_iterable: tuple[int, str, Color], searching_list: list[tuple]) -> list[tuple]:
    """
     Finds all records with specified values from specified list. Unique values can't be searched.

    :param values_iterable: tuple of values that should be in records
    :param searching_list: list that contains records
    :return: list of records that contains specified values
    """
    found_records = []
    for record in searching_list:
        if values_iterable == record[1:]:
            found_records.append(record)
    return found_records


def start_find_all_by_values(values_iterable: tuple[int, str, Color]):
    """
    Finds all records with specified values from record_list. Unique values can't be searched.
    Uses split_list and find_all_by_values methods to increase search speed.

    :param values_iterable: tuple of values that should be in records
    :return: list of all records that contains specified values
    """
    assert len(values_iterable) == 3
    assert isinstance(values_iterable[0], int) and isinstance(values_iterable[1], str) and isinstance(values_iterable[2], Color)
    split = split_list(record_list)
    with ProcessPoolExecutor(max_workers=len(split)) as executor:
        results = executor.map(find_all_by_values, repeat(values_iterable), split)
    found = []
    for result in results:
        found.extend(result)
    return found


def count_by_category(category: Color, searching_list: list[tuple]):
    """
    Counts number of records with a specified category in specified list.

    :param category: value from Color Enum
    :param searching_list: list that contains records
    """
    global record_count
    with lock:
        for record in searching_list:
            if category in record:
                record_count += 1


def start_count_by_category(category: Color):
    """
    Counts number of records with a specified category in record_list.

    :param category: value from Color Enum
    :return: count of records with a specified category
    """
    assert isinstance(category, Color)
    split = split_list(record_list)
    with ThreadPoolExecutor(max_workers=len(split)) as executor:
        executor.map(count_by_category, repeat(category), split)
    return record_count


if __name__ == '__main__':
    # Test with larger list
    # record_list.append(create_record(324432534, 100, 'm', Color.RED))
    # for i in range(1000000):
    #     if i % 5 == 0:
    #         record_list.append(create_record(i, 100, 'a', Color.RED))
    #     else:
    #         record_list.append(create_record(i, 100, 'a', Color.GREEN))
    #
    # record_list.append(create_record(324532534, 100, 'm', Color.RED))

    # Find record with specified value start
    start = time.time()
    print(start_find_by_value('m'))
    end = time.time()
    print("Run in {:.6f} sec.".format(end - start))
    # Find record with specified value end
    print()
    # Find all record with specified values start
    start = time.time()
    print(start_find_all_by_values((100, 'a', Color.RED)))
    end = time.time()
    print("Run in {:.6f} sec.".format(end - start))
    # Find all record with specified values end
    print()
    # Count record with specified category start
    start = time.time()
    print(start_count_by_category(Color.RED))
    end = time.time()
    print("Run in {:.6f} sec.".format(end - start))
    # Count record with specified category end
