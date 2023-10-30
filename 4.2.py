class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    def print(self):
        print(self.letters)
    def letters_num(self):
        return len(self.letters)

class EngAlphabet (Alphabet):
    def __init__(self,lang,letters):
        super().__init__(lang,letters)
    __letters_num = 26
    def is_en_letter(self, letter):
        return letter in self.letters
    def letters_num(self):
        return self.__letters_num
    @staticmethod
    def example():
        return "I love Python"
alphabet = EngAlphabet("En", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
alphabet.print()
print(alphabet.letters_num())
print(alphabet.is_en_letter("A"))
print(EngAlphabet.example())
