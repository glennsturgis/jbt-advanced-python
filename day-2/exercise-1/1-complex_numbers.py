class ComplexNumber:
    """
    Represents a complex number
    """

    def __init__(self, real: int, img: float = 0.0):
        self._real = real
        self._img = img

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, real):
        # check that number is int
        if isinstance(real, int):
            self._real = real

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, img):
        if isinstance(img, float) or isinstance(img, int):
            self._img = float(img)

    def print(self):
        print(self)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'

class PositiveComplex(ComplexNumber):

    def __init__(self, real, img=0.0):
        super().__init__(real, img)

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, real: int):
        # check that number is int
        if isinstance(real, int) and real > 0:
            self._real = real

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, img):
        if isinstance(img, float) or isinstance(img, int) and img > 0:
            self._img = float(img)



if __name__ == '__main__':
    c = ComplexNumber(1)
    c.print()
    c.real = 5
    c.print()
    c.img = 5
    c.print()
    c.img = 7.0
    c.print()
    c.img = 'adasd'
    c.print()

    pc = PositiveComplex(1)
    pc.print()
    pc.real = -5
    pc.print()
    pc.img = 5
    pc.print()
    pc.img = 7.0
    pc.print()
    pc.img = 'adasd'
    pc.print()

    complexes = [
        ComplexNumber(1, 1),
        PositiveComplex(2, 3)
    ]
    print('-' * 80)
    print(*complexes, sep='\n')
    print('-' * 80)


