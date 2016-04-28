
class Log:
    def __init__(self, date, priority, msg):
        self.date = date
        self.priority = priority
        self.msg = msg
        
#class SelectorLogOnPriority:
#    def __init__(self, requiredPriority):
#        self.priority= requiredPriority

class SelectMotor:
    def __init__(self, selector, reader,  writer):
        self._writer = writer
        self._reader = reader
        self._selector = selector
        self._start()
        
    def _start(self):
        return None
        
