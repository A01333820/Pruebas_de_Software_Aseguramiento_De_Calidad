"""word_count.py"""
import sys
import time


def clean_word(word):
    #pylint: disable=line-too-long
    """Cleans a word by removing leading and trailing non-alphabetic characters and converting to lowercase"""
    start = 0
    end = len(word) - 1

    while start <= end and not word[start].isalpha():
        start += 1

    while end >= start and not word[end].isalpha():
        end -= 1

    return word[start:end + 1].lower()


def main():
    """Main function to read words from a file, count their frequencies, and print results."""
    if len(sys.argv) != 2:
        print("Usage: python word_count.py fileWithData.txt")
        return

    start_time = time.time()
    file_name = sys.argv[1]

    frequencies = {}

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for _, line in enumerate(file, start=1):
                words = line.strip().split()

                for raw_word in words:
                    word = clean_word(raw_word)

                    if word == "":
                        continue

                    if word in frequencies:
                        frequencies[word] += 1
                    else:
                        frequencies[word] = 1

    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    elapsed = time.time() - start_time

    ordered_words = sorted(frequencies.keys())

    results = []
    for word in ordered_words:
        results.append(f"{word}: {frequencies[word]}")

    results.append(f"Execution Time: {elapsed:.6f} seconds")
    results.append(f"Grand Total Unique Words: {len(frequencies)}")
    results.append(f"Total Words: {sum(frequencies.values())}")

    for line in results:
        print(line)

    with open("WordCountResults.txt", "w", encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
