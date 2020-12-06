class K:
    def __init__ (self, a, b):
        try:
            self.c = a / b
        except ZeroDivisionError:
            print("Ділення на нуль")
        else:
            print("Результат:", self.c)
        finally:
            print("Програма завершена")

k = K(3, 0)
# print(k.c)