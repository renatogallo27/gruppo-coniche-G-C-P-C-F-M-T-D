class Parabola:
    def __init__(self, tipo="param", p1=None, p2=None, p3=None, p4=None):
        if tipo == "param":
            self.__a = p1
            self.__b = p2
            self.__c = p3
            self.punti = []

        elif tipo == "fuocoDiret":
            self.__xfuoco = p1
            self.__yfuoco = p2
            self.__diret = p3
            self.__a = (4 * self.__yfuoco - self.__diret * 4) / 2
            self.__b = self.__a * self.__xfuoco * -2
            self.__c = (4 * self.__yfuoco + self.__yfuoco * self.__yfuoco - 1) / (4 * self.__xfuoco)

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def fuoco(self, asse):
        if asse == "parallelo all'asse delle x":
            x = (-self.__b) / (self.__a * 2)
            y = (-(self.__b * self.__b) - 4 * self.__a * self.__c) / 4 * self.__a
            return x, y
        if asse == "parallelo all'asse delle y":
            x = (-(self.__b * self.__b) - 4 * self.__a * self.__c) / 4 * self.__a
            y = (-self.__b) / (self.__a * 2)
            return x, y

    def direttrice(self, asse):
        if asse == "parallelo all'asse delle x":
            c2 = (-1 - ((self.__b * self.__b) - 4 * self.__a * self.__c)) / (4 * self.__a)
            return f"y={c2}"
        elif asse == "parallelo all'asse delle y":
            c2 = (-1 - ((self.__b * self.__b) - 4 * self.__a * self.__c)) / (4 * self.__a)
            return f"x={c2}"
