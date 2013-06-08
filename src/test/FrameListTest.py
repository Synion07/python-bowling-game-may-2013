'''
Created on 05/06/2013

@author: synion
'''
import unittest
from bowlinggame.FrameListBuilder import FrameListBuilder
from bowlinggame.Frame import Frame, FinalFrame, LinkedFrame


class FrameListBuilderTest(unittest.TestCase):
    '''
    Tests from FrameList, which contains a list of
    frames linked to each other
    '''

    def test_builds_frame_references(self):
        '''
        Check the builder is able to correctly transform
        a list of frames to linked frames
        '''
        frames = []
        for index in range(0, 9):
            frames += [Frame(index, 0)]
        frames += [FinalFrame(1, 2, 3)]
        
        first_linked_frame = self._ready_linked_frame_list(frames)
        
        builder = FrameListBuilder(frames)
        built_frame = builder.build()
        next_frame = built_frame
        next_expected_frame = first_linked_frame
        
        while next_frame.has_next_frame():
            self.assertEquals(next_expected_frame, next_frame)
            next_frame = next_frame.next_frame
            next_expected_frame = next_expected_frame.next_frame
            
    def _ready_linked_frame_list(self, frames):
        '''
        Readies the linked frames for the test
        '''
        return LinkedFrame(frames[0], 
            LinkedFrame(frames[1], LinkedFrame(frames[2], 
            LinkedFrame(frames[3], LinkedFrame(frames[4], 
            LinkedFrame(frames[5], LinkedFrame(frames[6],
            LinkedFrame(frames[7], LinkedFrame(frames[8], 
            LinkedFrame(frames[9]))))))))))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()