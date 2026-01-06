class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self,other):
        s = self.__second + other.__second
        m = self.__minute + other.__minute + s // 60
        h = self.__hour + other.__hour + m // 60
        s %= 60
        m %= 60
        return Time(h, m, s)
    def display(self):
        print(self.__hour,self.__minute,self.__second)
t1=Time(4,3,1)
t2=Time(5,7,6)
t3=t2+t1
t3.display()    