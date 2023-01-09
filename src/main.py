import sys
import os
from termcolor import colored
from typing import List, Dict


def get_sentences(file_name: str) -> str:
    # Method to get the sentences of the given file, seperated by a newline character (\n)
    with open(file_name, 'r') as sentences_lines:
        return sentences_lines.readlines()


def is_file_valid(file_name: str) -> bool:
    # Method to check if a file is valid and it's contents are readable
    if os.access(file_name, os.R_OK):
        # Return true if the file IS readable
        return True
    # Return false if the file IS NOT readable
    print(colored(f'File {file_name} is not valid. Abandoning.', 'red'))
    return False


def main(file_name: str) -> None:
    # Main method, takes file name as the parameter.
    file_valid = is_file_valid(file_name)
    if file_valid:
        sentences = get_sentences(file_name)
        # Loop through the sentences and mark every occurrence of a word
        word_occurrence: Dict[str, int] = {}
        for i, sentence in enumerate(sentences):
            # Split the sentence by spaces into a list called `words_in_sentence`
            words_in_sentence: List[str] = sentence.split(' ')
            for word in words_in_sentence:
                # Check if the word is already in the dictionary, if it is, increment the value by 1
                if word in word_occurrence:
                    word_occurrence[word] += 1
                else:
                    word_occurrence[word] = 1
            # Ask the user if they like the sentence
            to_ask: str = colored(sentence.replace('\n', ''), 'cyan')
            like = input(f'Do you like the sentence "{to_ask}"? (y/n) ')
            if like == 'y':
                # Increment the value of the "liked" key in the dictionary by 1
                if 'liked' in word_occurrence:
                    word_occurrence['liked'] += 1
                else:
                    word_occurrence['liked'] = 1
            else:
                # Increment the value of the "disliked" key in the dictionary by 1
                if 'disliked' in word_occurrence:
                    word_occurrence['disliked'] += 1
                else:
                    word_occurrence['disliked'] = 1

            # Check if there is a next sentence
            if i + 1 < len(sentences):
                # Split the next sentence by spaces into a list called `next_words_in_sentence`
                next_words_in_sentence: List[str] = sentences[i + 1].split(' ')
                # Compare the words in the current and next sentences
                common_words = set(words_in_sentence) & set(next_words_in_sentence)
                if common_words:
                    print(colored('I predict you will like the next sentence.', 'green'))
                else:
                    print(colored('I predict you will not like the next sentence.', 'yellow'))
    else:
        exit(0)


if __name__ == '__main__':
    # Get file name from command line arguments
    file_name: str = sys.argv[1]
    try:
        main(file_name=file_name)
    except Exception as err:
        print(colored(f'An Exception has occurred: {err}', 'red'))
