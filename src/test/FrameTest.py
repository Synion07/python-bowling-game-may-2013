'''
Created on 02/06/2013

@author: synion
'''
import unittest
from bowlinggame.Frame import Frame

class FrameTest(unittest.TestCase):
    '''
    Tests related about Frames
    '''

    def test_adds_rolls_correctly(self):
        '''
        The rolls are added correctly
        '''
        frame = Frame(4, 1)
        self.assertEqual(frame.total_frame_score(), 5)

    def test_detects_a_spare_correctly(self):
        '''
        Detects a spare
        '''
        frame = Frame(5, 5)
        self.assertTrue(frame.is_spare())

    def test_detects_a_strike_correctly(self):
        '''
        Detects a strike
        '''
        frame = Frame(10, 0)
        self.assertTrue(frame.is_strike())

    def test_a_strike_is_not_a_spare(self):
        '''
        Strike = True != Spare == True
        '''
        frame = Frame(10, 0)
        self.assertTrue(frame.is_strike())
        self.assertFalse(frame.is_spare())
    
    def test_two_different_frames(self):
        '''
        Two different frames shouldn't be equal
        '''
        frame = Frame(10, 0)
        other_frame = Frame(10, 0)
        self.assertTrue(frame == other_frame)
        self.assertFalse(frame != other_frame)
    
    def test_a_Frame_does_not_equal_other_object(self):
        '''
        If not a Frame, shouldn't be equals
        '''
        frame = Frame(10, 0)
        other = 'other'
        self.assertFalse(frame == other)
        self.assertTrue(frame != other)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()