class Product:
    def __init__(self, object):
        # TODO: self.gtin = object['gtin']
        self.name = object['artikel']  # Origin country from Migros logistics db
        self.origin = object['herkunft']  # Origin country from Migros logistics db

        # Values provided by the Eaternity API
        self.__eat_rating = None  # The rating (label)
        self.__eat_co2_value = None  # The CO2 value

    def get_origin(self):
        return self.origin

    def get_name(self):
        return self.name

    def set_eat_rating(self, eat_rating):
        self.__eat_rating = eat_rating

    def set_eat_co2_value(self, co2_value):
        self.__eat_co2_value = co2_value

