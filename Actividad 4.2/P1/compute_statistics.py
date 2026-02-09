"""compute_statistics.py"""
import sys
import time


def read_numbers(file_name):
    """Reads numbers from a file and returns a list of valid numbers and a list of error messages"""
    numbers = []
    errors = []

    with open(file_name, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            value = line.strip()
            if not value:
                continue
            try:
                numbers.append(float(value))
            except ValueError:
                errors.append(
                    f"Invalid data at line {line_number}: {value}"
                )

    return numbers, errors


def mean(numbers):
    """ Calculates the mean (average) of a list of numbers."""
    total = 0.0
    for n in numbers:
        total += n
    return total / len(numbers)


def median(numbers):
    """ Calculates the median of a list of numbers."""
    ordered = sorted(numbers)
    n = len(ordered)

    if n % 2 == 0:
        return (ordered[n // 2 - 1] + ordered[n // 2]) / 2
    return ordered[n // 2]


def mode(numbers):
    """ Calculates the mode of a list of numbers."""
    freq = {}
    for n in numbers:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    max_count = 0
    result = None
    for key, value in freq.items():
        if value > max_count:
            max_count = value
            result = key


    return result


def population_variance(numbers, mean_value):
    """# Calculates the population variance of a list of numbers given the mean."""
    total = 0.0
    for n in numbers:
        total += (n - mean_value) ** 2
    return total / len(numbers)


def population_std_dev(variance_value):
    """# Calculates the population standard deviation given the variance."""
    return variance_value ** 0.5


def main():
    """ Main function to read numbers from a file, compute statistics, and print results."""
    if len(sys.argv) != 2:
        print("Usage: python compute_Statistics.py fileWithData.txt")
        return

    start_time = time.time()
    file_name = sys.argv[1]

    numbers, errors = read_numbers(file_name)

    for err in errors:
        print(err)

    if not numbers:
        print("No valid numeric data found.")
        return

    mean_value = mean(numbers)
    median_value = median(numbers)
    mode_value = mode(numbers)
    variance_value = population_variance(numbers, mean_value)
    std_dev_value = population_std_dev(variance_value)

    elapsed = time.time() - start_time

    results = [
        f"Count: {len(numbers)}",
        f"Mean: {mean_value}",
        f"Median: {median_value}",
        f"Mode: {mode_value}",
        f"Population Variance: {variance_value}",
        f"Population Std Dev: {std_dev_value}",
        f"Execution Time: {elapsed:.6f} seconds",
    ]

    for line in results:
        print(line)

    with open("StatisticsResults.txt", "w", encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
