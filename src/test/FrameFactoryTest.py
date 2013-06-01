'''
Created on 01/06/2013

@author: synion
'''
import unittest
from bowlinggame.FrameFactory import FrameFactory
from bowlinggame.Frame import Frame

class FrameFactoryTest(unittest.TestCase):
    '''
    Validates that frames are converted correctly from
    a string
    '''

    def test_convert_normal_frames(self):
        '''
        Convert a normal frame string, without the extra bonus
        '''
        frame_to_convert = "12"
        converted_frame = Frame(1, 2)
        factory = FrameFactory()
        frame = factory.build_frame(frame_to_convert)
        self.assertEqual(converted_frame, frame)

    def test_convert_other_frame(self):
        '''
        Convert a normal frame string, but with other score
        '''
        frame_to_convert = "41"
        converted_frame = Frame(4, 1)
        factory = FrameFactory()
        frame = factory.build_frame(frame_to_convert)
        self.assertEqual(converted_frame, frame)

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

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_convert_normal_frames']
    unittest.main()
