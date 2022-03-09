# Dev time: 45 minutes 
import sys

class WordGuesser:
    def __init__(self):
        self.german_to_english = self.read_words("word_list.txt")
        self.key_iter = bidirectional_iterator(list(self.german_to_english.keys()))
        self.english_to_german = {v: k for k, v in self.german_to_english.items()}
        self.learn_words()

    def end_game(self):
        self.print_saved_words()
        sys.exit("Quitting Game")

    def write_words(self, file_name, german_word):
        if german_word =="":
            return
        with open(file_name, 'a+') as f:
            eng = self.german_to_english[german_word]
            f.write(german_word +"\t")
            f.write(eng+"\n")

    def print_saved_words(self):
        self.saved_words = self.read_words("saved_words.txt")
        self.saved_key_list = self.saved_words.keys()
        for word in self.saved_key_list:
            print(word)
            print(self.german_to_english[word])
            print("\n")
            
    def read_words(self, file_path):
        with open(file_path) as f:
            lines = f.readlines()
        german_to_english = {}
        for line in lines:
            german, english = line.strip("\n").split("\t")
            german_to_english[german] = english
        return german_to_english


    def learn_words(self):
        print_val = False
        while True:
            key, word = "", ""
            try:
                text = input("")  # or raw_input in python2
                # if print_val:
                #     print(word)
                if text == "":
                    key, word = self.go_next()
                elif text  == "n":
                    key, word = self.go_next()
                elif text == "b":
                    key, word = self.go_back()
                elif text == "s":
                    self.write_words("saved_words.txt", key)
                    # self.saved_key_list.append(key) 
                elif text == "q":
                    self.end_game()
                    break
                else:
                    print("Unrecognized command of %s" % text)
                # alt = not alt
            except Exception as e:
                print("Issue encountered")
                print(e)
                break
        
    def go_next(self):
        key = self.key_iter.next()
        while True:
            word = self.german_to_english[key]
            print(key)
            text = input("") 
            if text == "":
                print(word)
                return key, word
            elif text  == "n":
                print(word)
                return key, word
            elif text  == "b":
                key = self.key_iter.prev()
            elif text == "s":
                self.write_words("saved_words.txt", key)
                return key, word
            elif text == "q":
                    self.end_game()
                    break
            else:
                print("Unrecognized command")
    
    def go_back(self):
        while True:
            key = self.key_iter.prev()
            word = self.german_to_english[key]
            print(key)
            text = input("") 
            if text == "":
                print(word)
                # self.key_iter.next()
                return key, word
            elif text  == "n":
                print(word)
                # self.key_iter.next()
                return key, word
            elif text == "s":
                self.write_words("saved_words.txt", key)
                return key, word
            elif text == "q":
                    self.end_game()
                    break
            else:
                continue

class bidirectional_iterator(object):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def next(self):
        try:
            self.index += 1
            result = self.collection[self.index]
        except IndexError:
            raise StopIteration
        return result

    def prev(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        result = self.collection[self.index]
        return result

    def __iter__(self):
        return self

wordGuesser = WordGuesser()