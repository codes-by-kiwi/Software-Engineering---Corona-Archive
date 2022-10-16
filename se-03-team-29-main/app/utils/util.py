import errno


class MissingInput(Exception):
    def __init__(self, message="Missing parameter"):
        self.message = message

    def __str__(self):
        return f'{self.message}'
