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
        if frame_input == "X-":
            return Frame(10, 0)
        else:
            return Frame(int(frame_input[0]), int(frame_input[1]))
    
    def build_game(self, game_string):
        '''
        Builds a full game
        '''
        frame_list = [game_string[i:i+2] for i in range(0, len(game_string), 2)]
        final_frames = []
        for frame in frame_list:
            final_frames += [self.build_frame(frame)]
        return final_frames

    def __init__(self):
        '''
        Constructor
        '''
        pass
