import string
rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]

def check_line(line):
    rude_count = 0
    word_index = 0
    words = line.split(" ")

    for word in words:

       stripped_word = word.strip(string.punctuation).lower()
       if stripped_word in rude_words:
           rude_count += 1
           print(f"Found rude word: {word}")
           words[word_index] = bleeper(word)
       word_index += 1
    line = " ".join(words)

    return line, rude_count
def check_file(filename):
    with open(filename) as myfile:
        rude_count = 0
        lines = []
        for line in myfile:
            line, rude_subtotal = check_line(line)
            rude_count += rude_subtotal
            lines.append(line)

    if rude_count == 0:
        print("Congratulations, your file has no rude words.")
        print("At least, no rude words I know.")

    else:
        with open("bleeped_copy.txt", "w") as bleeped_copy:
            bleeped_copy.write("\n".join(lines))
            print(f"Found {rude_count} rude words in your file. See                           bleeped_copy.txt for a censored copy of your file.")


def bleeper(word):
    pos = 0
    for character in word:
        if character not in string.punctuation:
            character = "*"
        word = word.replace(word[pos], character)
        pos += 1
    return word

if __name__ == '__main__':
    check_file("my_other_story.txt")
