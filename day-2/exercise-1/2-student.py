class Student:

    def __init__(self, id_number, name, city):
        self._id_number = id_number
        self._name = name
        self._city = city

    @property
    def id_number(self):
        return self._id_number

    @property
    def name(self):
        return self._name

    @property
    def city(self):
        return self._city

    @id_number.setter
    def id_number(self, id_number):
        return

    @name.setter
    def name(self, name):
        self._name = name

    @city.setter
    def city(self, city):
        self._city = city

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'

class UStudent(Student):

    def __int__(self, points, status, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._points = points
        self._status = status

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        if 0 <= points <= 100:
            self._points = points

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str) and status.lower() in ['enrolled', 'graduated']:
            self._status = status

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__dict__} {super()}'


class GStudent(Student):

    def __int__(self, project, supervisor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._project = project
        self._supervisor = supervisor

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, project):
        if 0 <= project <= 100:
            self._project = project

    @property
    def supervisor(self):
        return self._supervisor

    @supervisor.setter
    def supervisor(self, supervisor):
        if isinstance(supervisor, str) and supervisor.lower() in ['enrolled', 'graduated']:
            self._supervisor = supervisor

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__dict__} {super()}'
