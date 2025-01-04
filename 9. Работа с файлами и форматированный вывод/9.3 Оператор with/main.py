

class WordsFinder:
    PUNCTUATION = [",", ".", "=", "!", "?", ";", ":", " - "]
    def __init__(self, *file_names):
        self.file_names = []
        for i in range(0, len(file_names)): self.file_names.append(file_names[i])

    def get_all_words(self):
        all_words = dict()
        list_of_words = []
        for file_name in self.file_names:
            with open(file_name, "r", encoding="utf-8") as file:
                for line in file:
                    #split line into words
                    words = line.split()
                    #check every word in line if it has forbidden symbol
                    for word in words:
                        for forbidden_symbol in self.PUNCTUATION:
                            if forbidden_symbol in word: word = word.replace(str(forbidden_symbol), "")

                        list_of_words.append(word.lower())
            all_words.update({file_name:list_of_words})
        file.close()
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        end_dict = dict()
        for key in all_words.keys():
            for value in all_words.values():
                for words in range(0, len(value)):
                    if word.lower() in value[words]:
                        end_dict.update({key: words+1})
                        return end_dict

        return print("There is no word with that name!")

    def count(self, word):
        all_words = self.get_all_words()
        word_appeared = 0
        end_dict = dict()
        for key in all_words.keys():
            for value in all_words.values():
                for words in range(0, len(value)):
                    if word.lower() in value[words]: word_appeared += 1
            end_dict.update({key: word_appeared})
            word_appeared = 0

        return end_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
