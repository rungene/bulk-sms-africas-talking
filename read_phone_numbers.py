import csv


def read_kenyan_phone_numbers(filename="sample.csv", delimiter=","):
    """Reads phone numbers from a CSV file, replaces numbers
    starting with '0' with '+254',and returns a list of
    modified phone numbers.

    Args:
        filename (str, optional): The name of the CSV file to read.
        Defaults to "sample.csv".
        delimiter (str, optional): The delimiter used in the CSV
        file. Defaults to "," (comma).

    Returns:
        list: A list of modified phone numbers (strings).
    """

    kenyan_phone_numbers = []
    try:
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=delimiter)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    # Skip header - first row contains column names
                    line_count += 1
                    continue

                phone_number = row[3].strip()
                if phone_number.startswith('0') or \
                        phone_number.startswith('+254'):
                    if phone_number.startswith('0'):
                        phone_number = '+254' + phone_number[1:]
                    kenyan_phone_numbers.append(phone_number)
                line_count += 1
    except FileNotFoundError:
        print(f'Error: file "{filename}" not found')
    except Exception as e:
        print(f'Error: {e}')
    if kenyan_phone_numbers:
       return kenyan_phone_numbers


if __name__ == "__main__":
    modified_numbers = read_kenyan_phone_numbers()
    print(modified_numbers)
