'''
Created on 01/06/2013

@author: synion
'''
from bowlinggame.Frame import Frame

class FrameFactory(object):
    '''
    Converts a string of rolls into a list of Frames
    '''

    def build_frame(self, frame_input):
        '''
        Builds a single frame
        '''
        return Frame(int(frame_input[0]), int(frame_input[1]))

    def __init__(self):
        '''
        Constructor
        '''
        pass
