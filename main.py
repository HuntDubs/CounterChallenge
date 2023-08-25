import sys


def run_tests():
    # each test assertion is run with the strip() function to clear any new-lines attached to the end
    assert run_challenge('It was many and many a year ago').strip() == 'I0t w1s m2y a1d m2y a y2r a1o'
    assert run_challenge('Copyright,Microsoft:Corporation').strip() == "C7t,M6t:C6n"
    assert run_challenge('Look,A Plane or... is it Superman!').strip() == "L1k,A P3e o0r... i0s i0t S6n!"
    assert run_challenge('four sccores and seven years ago').strip() == "f2r s4s a1d s2n y3s a1o"
    return "Tests Passed"


def parse_word(word):
    counter = 0
    original_letters = []
    new_word = ""

    new_word = new_word + word[0]
    # check to see if word is one letter, in which case we are done
    if len(word) == 1:
        return new_word

    # pass through every character in the current word, incrementing the count as long as the character is original
    for character in word[1:-1]:
        if character in original_letters:
            pass
        else:
            original_letters.append(character)
            counter += 1

    new_word = new_word + str(counter) + word[-1]
    return new_word


# iterate through every word in the sentence, passing each word to parse_word()
def parse_sentence(sentence):
    current_word = ""
    new_sentence = ""

    for character in sentence:
        if character.isalnum():
            current_word = current_word + character
        else:
            # Handles multiple non-alphabetic characters in a row (ex. 'or..' , 'hello! ')
            if current_word == "":
                new_sentence = new_sentence + character
                continue
            new_sentence = new_sentence + parse_word(current_word) + character
            current_word = ""

    return new_sentence


# sys.argv is an array, so we change it to a string and send it to parse_sentence()
def run_challenge(sentence=""):
    if len(sys.argv) <= 1:
        print("Wrong number of command line arguments.\n")
    else:
        # Add an extra space at the end of the string to process the last word of the sentence
        if not sentence:
            sentence = ' '.join(sys.argv[1:]) + ' '
        else:
            sentence = sentence + ' '
        counted_sentence = parse_sentence(sentence)
        return counted_sentence


if __name__ == '__main__':
    if sys.argv[1] == "RunTest":
        result = run_tests()
    else:
        result = run_challenge()
    print(result)
