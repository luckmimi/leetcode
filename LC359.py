class Logger:

    def __init__(self):
        self.dct = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dct:
            self.dct[message] = timestamp
            return True
        else:
            if self.dct[message] + 10 > timestamp:
                return False
            else:
                 self.dct[message] = timestamp
                 return True
                


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
