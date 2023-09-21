class InvalidFormatExeption(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
    
    
    def __str__(self):
        return f"{self.code} Number: {self.msg}"

class InvalidNumberExeption(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
    
    
    def __str__(self):
        return f"{self.code} Number: {self.msg}"

class InvalidOperatorExeption(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
    
    
    def __str__(self):
        return f"{self.code} Number: {self.msg}"


class ZeroDivisionErrorNew(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
    
    
    def __str__(self):
        return f"{self.code} Number: {self.msg}"

