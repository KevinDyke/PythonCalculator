class rpncalculator():
    def __init__(self):
        self.stack = []
        self.result = 0
        self.errMsg = ""
        
    def enterValue(self,value):
        self.stack.append(float(value))
        
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
 
    def divide(self):
        self.number2 = self.stack.pop()
        self.number1 = self.stack.pop()
        if self.number2 == 0.0:
           self.errMsg = "Division By Zero"
        else:
           self.result = self.number1 / self.number2
           self.stack.append(self.result)
           print(self.result)
           
    def getResult(self):
        if self.errMsg != "":
           return self.errMsg
        else:
           return str(self.stack[0])