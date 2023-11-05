class EventManager:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(EventManager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        pass

    def run(self):
        pass