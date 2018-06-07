class rpncalculator():
    def __init__(self):
        self.stack = []
        self.result = 0
        
    def enterValue(self,value):
        self.stack.append(value)
        
    def sum(self):
        self.number2 = self.stack.pop()
        self.number1 = self.stack.pop()
        self.result = self.number1 + self.number2
        self.stack.append(self.result)
     
    def difference(self):
        self.number2 = self.stack.pop()
        self.number1 = self.stack.pop()
        self.result = self.number1 - self.number2
        self.stack.append(self.result)
 
    def multiply(self):
        self.number2 = self.stack.pop()
        self.number1 = self.stack.pop()
        self.result = self.number1 * self.number2
        self.stack.append(self.result)
 
    def getResult(self):
        return self.stack[0]