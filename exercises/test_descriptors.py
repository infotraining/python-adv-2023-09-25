
import pytest

class PositiveValueValidator:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner_class=None):
        value = getattr(instance, self.private_name)
        return value

    def __set__(self, instance, value):
        if value >= 0:
            setattr(instance, self.private_name, value)
        else:
            raise AttributeError("Cannot set negative integer")

class Person:

    age = PositiveValueValidator()    
    height = PositiveValueValidator()

    def __init__(self, name: str, age: int, height: int) -> None:
        self.name = name
        self.age = age
        self.height = height


def test_init_negative_age_raises_error():
    with pytest.raises(AttributeError):
        p = Person("John", -3, 170)


def test_init_negative_height_raises_error():
    with pytest.raises(AttributeError):
        p = Person("John", 44, -20)


def test_init_positive_values():
    p = Person("John", 44, 180)    
    assert p.age == 44
    assert p.height == 180


def test_age_setting_negative_value_raises_error():
    p = Person("John", 44, 180)    
    with pytest.raises(AttributeError):
        p.age = -78    


def test_height_setting_negative_value_raises_error():
    p = Person("John", 44, 180)    
    with pytest.raises(AttributeError):
        p.height = -78    


def test_age_setting_positive_value():
    p = Person("John", 44, 180)    
    p.age = 78    
    assert p.age == 78


def test_height_setting_positive_value():
    p = Person("John", 44, 180)    
    p.height = 178    
    assert p.height == 178
        
