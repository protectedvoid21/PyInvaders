class State:
    def __init__(self):
        self.screen = None
        self.state_manager = None

    def inject(self, state_manager, screen):
        self.state_manager = state_manager
        self.screen = screen
