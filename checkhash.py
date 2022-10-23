# CYB333 Final Project - Checksum/Hash Validator
# National University - La Jolla, CA
# Justin Frederick
# October 22, 2022

# Import only required components
from hashlib import md5, sha1, sha224, sha256, sha384, sha512
from sys import argv

# initialize empty dictionary for storing generated checksums/hashes in generate_hash function
hash_results = {}


def main_program(file_input, hash_input):
    # establish filehandler - open file in read binary mode
    file_handler = open(file_input, "rb")

    # store the expected checksum/hash in variable - handle whitespace with .strip()
    expected_hash = hash_input.strip()

    # pass file_handler object to generateHash function
    generate_hash(file_handler)

    # pass expected hash to compareHash function
    compare_hash(expected_hash)


# Autogenerate and display hashes then store in dictionary for function compare_hash to use
def generate_hash(file):
    x = file.read()

    # Dictionary used to store each Python hash algorithm object for generation of the file object hash
    algorithm_dict = {"md5": md5(x), "sha1": sha1(x), "sha224": sha224(x), "sha256": sha256(x), "sha384": sha384(x),
                      "sha512": sha512(x)}

    # loop through list
    for algorithm in algorithm_dict:
        # capture generated hashes in variables
        returned_key = algorithm
        returned_value = algorithm_dict[algorithm].hexdigest()

        # store generated hashes in dictionary
        hash_results[returned_key] = returned_value

        # display returned hashes
        print(f"Algorithm \t Hash\r")
        print(f"--------- \t ----\r")
        print(f"{returned_key.upper()} \t \t {returned_value.upper()} \n")
        print("-" * 141)


def compare_hash(expected_hash):
    # set variable boolean
    found_match = False

    print(f"RESULTS:\r")

    # Cycle through the dictionary with stored generated hashes
    for returned_hash in hash_results:
        returned_key = returned_hash
        returned_value = hash_results[returned_hash]

        # Display the match if any
        if returned_value.upper() == expected_hash.upper():
            print(f"Great news! The expected hash value matched algorithm: {returned_key.upper()} \n")
            print(f"{returned_key.upper()}: \t {returned_value.upper()} \r")
            print(f"Expected: \t {returned_value.upper()} \n")
            found_match = True
            break

    # If there is no match, notify user
    if not found_match:
        print("The expected hash value did not have a match.")


# Start the Program
if __name__ == "__main__":
    # argv[1] file/script to use
    # argv[2] checksum/hash string to verify
    try:
        main_program(argv[1], argv[2])

    except IndexError:
        print("Please try again using the following format:\r")
        print("python.exe [script name] [filename] [expected checksum/hash] \t")
        print("Example: python.exe checkhash.py sample.txt",
              "EF537F25C895BFA782526529A9B63D97AA631564D5D789C2B765448C8635FB6C")

# TODO: Create/Enable additional flexibility from command line to provide a hash to validate or just generate hashes.
