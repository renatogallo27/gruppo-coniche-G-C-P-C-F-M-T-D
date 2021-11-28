class Retta:
    def __init__(self, tipo="param", p1=None, p2=None, p3=None, p4=None):
        if tipo == "param":
            self.__a = p1
            self.__b = p2
            self.__c = p3
            self.__punti = []
            self.__m = p4

        elif tipo == "punti":
            self.__x = p1
            self.__y = p2
            self.__x2 = p3
            self.__y2 = p4
            self.__m = ((self.__y2 - self.__y) / (self.__x2 - self.__x))
            self.__q = (-(self.__m * self.__x)) + self.__y
            self.__b = 1
            self.__a = -self.__m
            self.__c = -self.__q

        elif tipo == "coeff":
            self.__m = p4
            self.__x = p1
            self.__y = p2
            self.__q = (-(self.__m * self.__x)) + self.__y
            self.__b = 1
            self.__a = -self.__m
            self.__c = -self.__q

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def eqImplicita(self):
        if self.__b == 0:
            return f"{self.__a}x+{self.__c}=0"
        elif self.__c == 0:
            return f"{self.__a}x+{self.__b}y=0"
        elif self.__a == 0:
            return f"{self.__b}y+{self.__c}=0"
        else:
            return f"{self.__a}x+{self.__b}y+{self.__c}"

    def eqEsplicita(self):
        if self.__b == 0:
            return f"x={-self.__c}/{self.__a}"
        elif self.__c == 0:
            return f"y={-self.__a}x/{self.__b}"
        elif self.__a == 0:
            return f"y={-self.__c}/{self.__b}"
        else:
            return f"y={-self.__a / self.__b}x+{-self.__c / self.__b}"

    def trovaY(self, x):
        y = ((-self.__a * x) / self.__b + (-self.__c / self.__b))
        return y

    def punti(self, N, M, x):
        for N in range(M, x):
            tupla = (x, self.trovaY(x))
            x = x + 1
            self.__punti.append(tupla)
            return f"Coordinate dei punti: {self.__punti}"

    def m(self):
        if self.__b == 0:
            return f"La retta è parallela all'asse delle ordinate"
        elif self.__a == 0:
            return f"La retta è perpendicolare all'asse delle ascisse"
        else:
            self.__m = -self.__a / self.__b
            return self.__m

    def intersezione(self, a1=None, b1=None, c1=None, m1=None):
        if m1 == self.__m:
            return f"null"

        elif m1 == self.__m and (-self.__c / self.__b) == (-c1 / b1):
            return self.__punti

        else:
            intersezione = (
                ((-self.__c / self.__b) + (c1 / b1)) / ((-self.__b / self.__a) + (b1 / a1)),
                ((-self.__b / self.__c) + (b1 / c1)) / ((-self.__b / self.__a) + (b1 / a1)))
            return intersezione
