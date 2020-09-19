class Product:
    def __init__(self, object):
        self.origin = object['herkunft']
        self.name = object['artikel']

    def get_origin(self):
        return self.origin

    def get_name(self):
        return self.name
