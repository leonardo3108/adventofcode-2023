def find_digit(text, step, spelleds):
    interval = range(0, len(text), 1) if step > 0 else range(len(text) - 1, -1, step)
    for position in interval:
        if text[position].isdigit():
            return text[position]
        else:
            for digit, spelled in enumerate(spelleds):
                if spelled == text[position:position+len(spelled)]:
                    return str(digit + 1)

def extract_calibration_values(calibration_document, detect_spelled = False):
    total_sum = 0

    spelleds = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] if detect_spelled else []


    for line in calibration_document:
        # Find the first and last digits in each line
        first_digit = find_digit(line, 1, spelleds)
        last_digit = find_digit(line, -1, spelleds)

        # Combine the first and last digits to form a two-digit number
        calibration_value = int(first_digit + last_digit)
        #print('\t\t', calibration_value)

        # Add to the total sum
        total_sum += calibration_value

    return total_sum

def main():
    print('Example:')

    # Example calibration document
    calibration_document = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet"
    ]

    # Calculate the sum of calibration values and print the result
    result = extract_calibration_values(calibration_document, False)
    print('\tPart one:', result)

    calibration_document = [
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen'
    ]

    # Calculate the sum of calibration values and print the result
    result = extract_calibration_values(calibration_document, True)
    print('\tPart two:', result)

    print('Input file:')
    # Read the calibration document from the file
    with open('input-01.txt', 'r') as file:
        calibration_document = file.readlines()

    # Calculate the sum of calibration values and print the result
    result = extract_calibration_values(calibration_document, False)
    print('\tPart one:', result)

    # Calculate the sum of calibration values and print the result
    result = extract_calibration_values(calibration_document, True)
    print('\tPart two:', result)

if __name__ == "__main__":
    main()
