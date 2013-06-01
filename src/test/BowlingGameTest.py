'''
Created on 01/06/2013

@author: synion
'''
import unittest
from bowlinggame.BowlingGame import BowlingGame
from bowlinggame.Frame import Frame


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
        self._score_test_helper(frames, 30)

    def test_normal_scoring_other_score(self):
        '''
        Test normal score (no spares or strikes) but with other
        scoreboard
        '''
        self._score_test_helper("12121212121212121215", 33)

    def test_spare_scoring(self):
        '''
        Now add an spare into the mix. Spares are when two
        hits from the same frame add up to 10 pins. This
        has a bonus score equal to the next roll
        '''
        self._score_test_helper("82500000000000000000", 20)

    def _score_test_helper(self, score, expected_score):
        '''
        Helper method to be DRY
        '''
        game = BowlingGame()
        self.assertEqual(game.score(score), expected_score)




if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
