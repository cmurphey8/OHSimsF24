import csv
import sys


def main():

    # TODO: Check for command-line usage
    if (len(sys.argv) != 3):
        print("Usage: python dna.py data.csv sequence.txt")
        return(1)

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as databaseFile:
        reader = csv.DictReader(databaseFile)
        databaseList = list(reader)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as sequenceFile:
        sequence = sequenceFile.read()

    # TODO: Find longest match of each STR in DNA sequence
    longestMatches = []

    # start at 1 because of the initial name value in the first entry
    for i in range(1, len(reader.fieldnames)):
        # figure out what the STR is
        STR = reader.fieldnames[i]
        # append a value to the array and intialize the length of longest matches to 0
        longestMatches.append(0)

        # calculate the longest matches for the given STR and record that value
        longestMatches[i - 1] = longest_match(sequence, STR)

    # TODO: Check database for matching profiles

    # iterate through the people
    for i in range(len(databaseList)):
        # counter for how many STR matches there are
        counter = 0

        # iterate through the types of STR
        for j in range(1, len(reader.fieldnames)):
            # if the given person's max value for the given STR is equal to the max of the sequence then add to the counter
            if databaseList[i][reader.fieldnames[j]] == longestMatches[j - 1]:
                counter += 1
            # if there are as many matches as there are STR's then there is a match
            if counter == len(reader.fieldnames) - 1:
                # print the first value, which should be their name
                print(f"{databaseList[i][0]}")
                return

    print("No Matches")
    return

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
