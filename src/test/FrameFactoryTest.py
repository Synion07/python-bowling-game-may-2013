'''
Created on 01/06/2013

@author: synion
'''
import unittest
from bowlinggame.FrameFactory import FrameFactory
from bowlinggame.Frame import Frame, FinalFrame

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
        self._assert_conversion_is_correct(converted_frame, frame_to_convert)

    def test_convert_other_frame(self):
        '''
        Convert a normal frame string, but with other score
        '''
        frame_to_convert = "41"
        converted_frame = Frame(4, 1)
        self._assert_conversion_is_correct(converted_frame, frame_to_convert)
        
    def test_convert_strike(self):
        '''
        Convert a strike "X-"
        '''
        frame_to_convert = "X-"
        converted_frame = Frame(10, 0)
        self._assert_conversion_is_correct(converted_frame, frame_to_convert)

    def _assert_conversion_is_correct(self, converted_frame, frame_to_convert):
        '''
        Helper method to assert the conversion is correct
        '''
        factory = FrameFactory()
        frame = factory.build_frame(frame_to_convert)
        self.assertEqual(converted_frame, frame)

    def test_full_game_into_frames(self):
        '''
        Pass a full normal game and check it's
        correctly converted into frames
        '''
        game_string = "00102030405060708090"
        expected_frames = [Frame(0, 0)] + [Frame(1, 0)] + [Frame(2, 0)]
        expected_frames += [Frame(3, 0)] + [Frame(4, 0)] + [Frame(5, 0)] 
        expected_frames += [Frame(6, 0)] + [Frame(7, 0)] + [Frame(8, 0)]
        expected_frames += [FinalFrame(9, 0, 0)]
        factory = FrameFactory()
        self.assertEqual(factory.build_game(game_string), expected_frames)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_convert_normal_frames']
    unittest.main()
