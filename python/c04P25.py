class Time:
    def __init__(self, hour:int=0,minute:int=0):
        self.__hour=hour
        self.__minute=minute
        self.__normalize()

    def __normalize(self):
        self.__hour+=self.__minute//60
        self.__minute = self.__minute%60

    def set_time(self, hour=None,minute=None):
        if hour is not None and minute is not None:
            self.__hour=hour
            self.__minute=minute
        elif hour is not None:
            self.__hour=hour
        self.__normalize()   
    def __add__(self,other):
        h = self.__hour + other.__hour
        m = self.__minute + other.__minute
        return Time(h,m)

    def show(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}")



t1 = Time(2, 45)
t2 = Time(1, 30)

t3 = t1 + t2
print("Added time:", end=" ")
t3.show()

t1.set_time(5)      
print("After set_time:", end=" ")
t1.show()

