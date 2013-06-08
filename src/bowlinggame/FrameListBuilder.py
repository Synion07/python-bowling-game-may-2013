'''
Created on 05/06/2013

@author: synion
'''
from bowlinggame.Frame import LinkedFrame

class FrameListBuilder(object):
    '''
    List of linked frames
    '''
    
    def build(self):
        '''
        Builds a LinkedFrame that links to subsequent frames
        '''
        last_frame = None
        for frame in reversed(self._list_of_frames):
            last_frame = LinkedFrame(frame, last_frame)
        return last_frame


    def __init__(self, list_of_frames):
        '''
        Constructor
        '''
        self._list_of_frames = list_of_frames