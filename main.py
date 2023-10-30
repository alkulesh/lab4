class String:
    def __init__(self,value):
        self.value = value
    def length(self):
        return len(self.value)
    def Capital_letters(self):
        return self.value.upper()
    def Small_letters(self):
        return self.value.lower()
    def Reverse(self):
        return self.value[::-1]
    def Replace(self, old, new):
        return self.value.replace(old, new)
my_string = String(input("Введите строку "))
print(my_string.length())
print(my_string.Capital_letters())
print(my_string.Small_letters())
print(my_string.Reverse())
print(my_string.Replace("Привет", "Пока"))