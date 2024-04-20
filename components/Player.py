class Player (object):
    """Player class."""
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.only_eight_ball_left = False
        self.only_nine_ball_left = False
