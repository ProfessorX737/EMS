class VenueCapacityException(Exception):
    def __init__(self, field, msg=None):
        self._field = field
        self._msg = msg