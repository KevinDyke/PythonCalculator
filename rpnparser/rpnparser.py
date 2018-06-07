import re

class rpnparser():
    def __init__(self,preParsedStr):
        self.preParsedStr = preParsedStr
        self.parsedString = ""
        
    def ParserString(self):
        return self.parsedString

    def parser(self):
        # check only digits, hex digits and x are present
        pattern = "[0-9|A-F|X]+"
    
        if re.search(pattern, self.preParsedStr):
           self.parsedString =  self.preParsedStr
        else:
           self.parsedString = "Unknown Number"
  