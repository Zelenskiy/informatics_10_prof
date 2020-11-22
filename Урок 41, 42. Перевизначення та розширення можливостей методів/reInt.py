class UAHformat (int):
    def __init__(self,x):
        self.x = x
    def __str__(self):
        s = str(int(self.x))
        c = str(int((self.x - int(self.x))*100))
        s = s[-9:-6] + "`" +s[-6:-3] + "`" + s[-3:]
        return s + " грн " + c + " коп"

x = UAHformat(1500001)
print(x)


