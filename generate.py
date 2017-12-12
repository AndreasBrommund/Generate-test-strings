import re

"""Set the max length of the string"""
max_length = 10

"""Turn on or off debug """
debug = True

"""Is empty string valid"""
is_empty_valid = False

"""Print accept or reject"""
print_accept_or_reject = True

all_permutations = set()
valid_sequences = set()
invalid_sequences = set()

def valid_test( sequence ): 
    
    num_zero = 0
    num_one = 0
    expect_one = True

    for c in sequence:
        if c == '1':
            if expect_one:
                num_one += 1
            else: 
                return False
        else:
            expect_one = False
            num_zero += 1
        

    return num_zero != num_one


def generate_string( sequence ):

    if len(sequence) >= max_length:
        return
    
    all_permutations.add(sequence + "0")
    all_permutations.add(sequence + "1")
    generate_string(sequence + "0")
    generate_string(sequence + "1")


generate_string("")

all_permutations = sorted(all_permutations, key=lambda item: (len(item), item))

if debug:
    print("--------------------------------")
    print("All permutations")
    print("--------------------------------")
    print(all_permutations)
    print("--------------------------------\n")
    print("--------------------------------")
    print("Number of permutations")
    print("--------------------------------")
    print(len(all_permutations))
    print("--------------------------------\n")

for sequence in all_permutations:
    if valid_test(sequence):
        valid_sequences.add(sequence)
    else:
        invalid_sequences.add(sequence)

valid_sequences = sorted(valid_sequences, key=lambda item: (len(item), item))
invalid_sequences = sorted(invalid_sequences, key=lambda item: (len(item), item))



print("--------------------------------")
print("Valid sequences")
print("--------------------------------")
if is_empty_valid:
    print("")
for sequence in valid_sequences:
    if print_accept_or_reject:
        print(sequence + " accept")
    else:
        print(sequence)
print("--------------------------------\n")

print("--------------------------------")
print("Invalid sequences")
print("--------------------------------")
if not is_empty_valid:
    print("")
for sequence in invalid_sequences:
    if print_accept_or_reject:
        print(sequence + " reject")
    else:
        print(sequence)
print("--------------------------------\n")



