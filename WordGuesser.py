# Dev time: 45 minutes 

class WordGuesser:
    def __init__(self):
        self.german_to_english = self.read_words("word_list.txt")
        self.key_iter = bidirectional_iterator(list(self.german_to_english.keys()))
        self.english_to_german = {v: k for k, v in self.german_to_english.items()}
        self.saved_key_list = []
        self.learn_words()

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
                    self.saved_key_list.append(key) 
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
                    self.saved_key_list.append(key) 
            else:
                print("Unrecognized command")
    
    def go_back(self):
        while True:
            prev_key = self.key_iter.prev()
            prev_word = self.german_to_english[prev_key]
            print(prev_key)
            text = input("") 
            if text == "":
                print(prev_word)
                # self.key_iter.next()
                return prev_key, prev_word
            elif text  == "n":
                print(prev_word)
                # self.key_iter.next()
                return prev_key, prev_word
            elif text == "s":
                    self.saved_key_list.append(key) 
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