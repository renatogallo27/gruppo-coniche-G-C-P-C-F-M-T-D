class parabola:
    def __init__(self, tipo="param", p1=None, p2=None, p3=None, p4=None):
        if tipo == "param":
            self.__a = p1
            self.__b = p2
            self.__c = p3
            self.punti = []

        elif tipo == "fuocoDiret":  # da completare
            pass

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def fuoco(self):
        x = (-self.__b) / (self.__a * 2)
        y = (-(self.__b * self.__b) - 4 * self.__a * self.__c) / 4 * self.__a

    def direttrice(self):
        c2 = (-1 - ((self.__b * self.__b) - 4 * self.__a * self.__c)) / 4 * self.__a
        return c2
