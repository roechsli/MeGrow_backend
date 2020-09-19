class Product:
    def __init__(self, object):
        # Values from Migros db
        # TODO: self.gtin = object['gtin']
        self.name = object['artikel']  # article name
        self.origin = object['herkunft']  # origin country
        self.quantity = object['quantity']  # quantity given in units
        self.unit = object['unit']  # units of measure ('m3' or 'kg')

        # Values provided by the Eaternity API
        self.__eat_rating = None  # The rating (label)
        self.__eat_co2_value = None  # The CO2 value

    def get_origin(self):
        return self.origin

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

    def get_unit(self):
        return self.unit

    def set_eat_rating(self, eat_rating):
        self.__eat_rating = eat_rating

    def set_eat_co2_value(self, co2_value):
        self.__eat_co2_value = co2_value

