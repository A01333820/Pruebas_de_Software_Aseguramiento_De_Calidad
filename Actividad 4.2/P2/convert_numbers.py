"""convert_numbers.py"""
import sys
import time

HEX_CHARS = "0123456789ABCDEF"

def to_complemento_a_2(binary):
    """Converts a binary string to its two's complement representation."""
    inverted = ""
    for bit in binary:
        inverted += "1" if bit == "0" else "0"

    carry = 1
    result = ""

    for bit in reversed(inverted):
        if bit == "1" and carry == 1:
            result = "0" + result
        elif bit == "0" and carry == 1:
            result = "1" + result
            carry = 0
        else:
            result = bit + result

    return result

def to_binary(number):
    """Converts a decimal number to its binary representation."""
    n = abs(number)
    result = ""
    while n > 0:
        result = str(n % 2) + result
        n //= 2
    #pylint: disable=superfluous-parens
    if (number < 0):
        result = to_complemento_a_2(result)
    return result

def to_complemento_a_2_hexadecimal(hex_value):
    """Converts a hexadecimal string to its two's complement representation."""  
    inverted = ""
    for char in hex_value:
        inverted += HEX_CHARS[15 - HEX_CHARS.index(char)]
    result = ""
    carry = 1

    for char in reversed(inverted):
        value = HEX_CHARS.index(char)

        if value == 15 and carry == 1:
            result = "0" + result
        else:
            result = HEX_CHARS[value + carry] + result
            carry = 0

    return result


def to_hexadecimal(number):
    """Converts a decimal number to its hexadecimal representation."""
    result = ""
    n = abs(number)
    while n > 0:
        result = HEX_CHARS[n % 16] + result
        n //= 16
    if number < 0:
        result = to_complemento_a_2_hexadecimal(result)
    return result


def main():
    """Main function to read numbers from a file, convert them, and print results."""
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py fileWithData.txt")
        return

    start_time = time.time()
    file_name = sys.argv[1]
    output = []

    with open(file_name, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            value = line.strip()
            if not value:
                continue
            try:
                number = int(value)
                binary = to_binary(number)
                hexa = to_hexadecimal(number)
                output.append(
                    f"{number} | BIN={binary} | HEX={hexa}"
                )
            except ValueError:
                print(
                    f"Invalid data at line {line_number}: {value}"
                )

    elapsed = time.time() - start_time
    output.append(f"Execution Time: {elapsed:.6f} seconds")

    for line in output:
        print(line)

    with open("ConvertionResults.txt", "w", encoding="utf-8") as file:
        for line in output:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
