'''
Created on 01/06/2013

@author: synion
'''
import unittest
from bowlinggame.BowlingGame import BowlingGame
from bowlinggame.Frame import Frame
from bowlinggame.Frame import FinalFrame


class BowlingGameTest(unittest.TestCase):
    '''
    Class to test the bowling game
    '''

    def test_normal_scoring(self):
        '''
        Test that normal scores (no spares or strikes) are
        added normally
        '''
        frames = [Frame(1, 2)] * 10
        self._assert_score_equals(frames, 30)

    def test_normal_scoring_other_score(self):
        '''
        Test normal score (no spares or strikes) but with other
        scoreboard
        '''
        frames = [Frame(1, 2)] * 9 + [Frame(1, 5)]
        self._assert_score_equals(frames, 33)

    def test_spare_scoring(self):
        '''
        Now add an spare into the mix. Spares are when two
        hits from the same frame add up to 10 pins. This
        has a bonus score equal to the next roll
        '''
        frames = [Frame(8, 2)] + [Frame(5, 2)] + [Frame (0, 0)] * 8
        self._assert_score_equals(frames, 22)
        
    def test_strike_scoring(self):
        '''
        Roll a strike, should count the next frame as bonus
        '''
        frames = [Frame(10, 0)] + [Frame(5, 2)] + [Frame(0, 0)] * 8
        self._assert_score_equals(frames, 24)
        
    def test_several_spares_scoring(self):
        '''
        Roll several spares, see what happens
        '''
        frames = [Frame(8, 2)] * 4 + [Frame(0, 0)] * 6
        self._assert_score_equals(frames, 18+18+18+10)
    
    def test_several_strikes_scoring(self):
        '''
        Roll several strikes, see what happens
        '''
        frames = [Frame(10, 0)] * 4 + [Frame(0, 0)] * 6
        self._assert_score_equals(frames, 30+30+20+10)
        
    def test_mix_spares_and_strikes(self):
        '''
        Mix spares and strikes
        '''
        frames = [Frame(10, 0)] + [Frame(5, 5)] + [Frame(5, 5)]
        frames += [Frame(10, 0)] + [Frame(10, 0)] + [Frame(5, 5)]
        frames += [Frame(5, 0)] + [Frame(0, 0)] * 3
        self._assert_score_equals(frames, 20+15+20+25+20+15+5)

    def test_final_frame_spare(self):
        '''
        Test the final frame acts as expected
        '''
        frames = [Frame(0, 0)] * 9 + [FinalFrame(5, 5, 3)]
        self._assert_score_equals(frames, 13)
        
    def test_last_frame_strike(self):
        '''
        Second last frame has a strike
        '''
        frames = [Frame(0, 0)] * 8 + [Frame(10, 0)]
        frames += [FinalFrame(2, 3, 0)]
        self._assert_score_equals(frames, 15+2+3)
        
    def test_last_frame_strike_spare(self):
        '''
        Second last frame has a strike
        '''
        frames = [Frame(0, 0)] * 8 + [Frame(10, 0)]
        frames += [FinalFrame(7, 3, 3)]
        self._assert_score_equals(frames, 33)
        
    def test_final_frame_strike(self):
        '''
        Test the final frame strikes act as expected
        '''
        frames = [Frame(0, 0)] * 9 + [FinalFrame(10, 1, 1)]
        self._assert_score_equals(frames, 12)

    def _assert_score_equals(self, frames, expected_score):
        '''
        Helper method to be DRY
        '''
        game = BowlingGame(frames)
        self.assertEqual(game.score(), expected_score)




if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
