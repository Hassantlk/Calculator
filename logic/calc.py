import sys
sys.path.append("..")  # Add parent directory to the system path

from Calculator.exeption import ZeroDivisionErrorNew


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multipy(a, b):
    return a * b


def divide(a, b):
    return a/b
