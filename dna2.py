# PROMPT:   I DON'T UNDERSTAND PYTHON VARIABLE TYPES, ESPECIALLY NON-PRIMITIVE TYPES, 
#           BUT I'M AT OFFICE HOURS BECAUSE I DON'T UNDERSTAND MY ERROR ON LINE 73.

import csv
import sys

def main():
    # TODO: Check for command-line usage
    if len(sys.argv)!= 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    database = sys.argv[1]
    sequence = sys.argv[2]

    # TODO: Read database file into a variable
    with open(database, "r") as file:
        reader = csv.DictReader(file)

    # TODO: Read DNA sequence file into a variable
    with open(sequence, "r") as file2:
        seq = file2.read()

    # get STR list
    headers = database.fieldnames[1:]

    # TODO: Find longest match of each STR in DNA sequence
    dna_dict = {}
    for i in headers:
        dna_dict[i] = longest_match(sequence, headers)

    # TODO: Check database for matching profiles


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
