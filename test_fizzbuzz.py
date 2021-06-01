import pytest
from fizzbuzz import fizzbuzz

def test_num():
    assert(fizzbuzz(1) == '1')
    assert(fizzbuzz(89) == '89')

def test_fizz():
    assert(fizzbuzz(87) == 'Fizz')
    assert(fizzbuzz(69) == 'Fizz')
    assert(fizzbuzz(51) == 'Fizz')

def test_buzz():
    assert(fizzbuzz(55) == 'Buzz')
    assert(fizzbuzz(10) == 'Buzz')
    assert(fizzbuzz(65) == 'Buzz')

def test_fizzbuzz():
    assert(fizzbuzz(75) == 'FizzBuzz')
    assert(fizzbuzz(90) == 'FizzBuzz')
    assert(fizzbuzz(60) == 'FizzBuzz')
