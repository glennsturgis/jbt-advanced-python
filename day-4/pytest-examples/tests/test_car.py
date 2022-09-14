import pytest
from parking.car import Car


class MyTester:
    def __init__(self, x):
        self.x = x

    def dothis(self):
        assert self.x


@pytest.fixture
def tester(request):
    return MyTester(request.param)


class TestIt:
    @pytest.mark.parametrize('tester', [True, False], indirect=['tester'])
    def test_tc1(self, tester):
        tester.dothis()
        assert True


# ===========================================================================


@pytest.fixture
def fixture_car_with_fuel(request):
    car = Car('Ford', 12)
    car.add_fuel(request.param)
    return car


@pytest.mark.parametrize('fixture_car_with_fuel', [20], indirect=[''])
def test_car_add_fuel(monkeypatch, fixture_car_with_fuel):
    pass


def test_car_init():
    car = Car('Ford', 12)
    assert car.name == 'Ford'
    assert car.parked is False
    assert car.consumption == 12


def test_car_drive(monkeypatch):
    monkeypatch.setattr('time.sleep', lambda x: None)
    car = Car('Jimmy', 20)
    car.drive(100)
    assert car.fuel == 0
    car.add_fuel(10)
    car.drive(100)
    assert car.fuel == 5


def test_car_add_fuel(monkeypatch):
    monkeypatch.setattr('time.sleep', lambda x: None)
    car = Car('Ford', 25)
    car.add_fuel(75)
    assert car.fuel == 75
    with pytest.raises(AssertionError) as exc_info:
        car.add_fuel(-4)
        assert exc_info.value.args[0] == 'Fuel should be positive'


@pytest.mark.parametrize("trip,expected_fuel,expected_km", [
    ([(10, 20), (10, 20), (10, 20)], 27, 60),
    ([(0, 20), (8, 20), (10, 12)], 16.4, 32),
])
def test_car_trip(monkeypatch, trip, expected_fuel, expected_km):
    monkeypatch.setattr('time.sleep', lambda x: None)
    car = Car("jimny", 20)
    for fuel, distance in trip:
        car.add_fuel(fuel)
        car.drive(distance)
    assert car.fuel == expected_fuel
    assert car.kilometrage == expected_km


@pytest.mark.parametrize("fuel,expected_fuel", [
    (100, 100),
    (10001, 1000),
])
def test_car_trip(monkeypatch, fuel, expected_fuel):
    monkeypatch.setattr('time.sleep', lambda x: None)
    car = Car("jimny", 20, 1000)
    car.add_fuel(fuel)
    assert car.fuel == expected_fuel

