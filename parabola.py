class Parabola:
    def __init__(self, tipo="param", p1=None, p2=None, p3=None, p4=None):
        if tipo == "param":
            self.__a = p1
            self.__b = p2
            self.__c = p3
            self.__punti = []

        elif tipo == "fuocoDiret":
            self.__xfuoco = p1
            self.__yfuoco = p2
            self.__diret = p3
            self.__a = (4 * self.__yfuoco - self.__diret * 4) / 2
            self.__b = self.__a * self.__xfuoco * -2
            self.__c = (4 * self.__yfuoco + self.__yfuoco * self.__yfuoco - 1) / (4 * self.__xfuoco)
            self.__punti = []

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
            return c2, f"y={c2}"
        elif asse == "parallelo all'asse delle y":
            c2 = (-1 - ((self.__b * self.__b) - 4 * self.__a * self.__c)) / (4 * self.__a)
            return c2, f"x={c2}"

    def trovaY(self, x):
        y = self.__a * (x ** 2) + self.__b * x + self.__c
        return y

    def trovaX(self, y):
        x = self.__a * (y ** 2) + self.__b * y + self.__c
        return x

    def punti(self, N, M, asse):
        if asse == "parallelo all'asse delle y":
            for x in range(N, M):
                tupla = (x, self.trovaY(x))
                self.__punti.append(tupla)
            return self.__punti

        elif asse == "parallelo all'asse delle x":
            for y in range(N, M):
                tupla = (self.trovaX(y), y)
                self.__punti.append(tupla)
            return self.__punti
