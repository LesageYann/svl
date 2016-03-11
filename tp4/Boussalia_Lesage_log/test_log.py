
import unittest
from mockito import *
import io
from log import *

#class TestSelector(unittest.TestCase):
#    def test_selector_priority_more_than_required_succes(self):
#        log= mock()
#        log.priority = 7
#        filtre = SelectorLogOnPriority(5)
#        self.assertTrue(filtre.accept(log))

class TestMotor(unittest.TestCase):
    #test en train de changer suite a vos remarques au tableau
    def test_read_one_log_succes(self):
        selector = mock()
        reader =mock()
        
        when(selector).accept(any()).thenReturn(True)
        motor= SelectMotor( selector, reader, selector)
        verify(selector).accept()
