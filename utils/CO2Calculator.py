class CO2Calculator(object):
    # Helper class that can return the co2 emissions based on the means of transport:
    #   - car
    #   - cruise
    #   - flight
    #   returns: emission (kilograms of CO2)
    GRAMS_TO_KILOGRAMS = 1000

    @classmethod
    def calculate_co2_emission(cls, distance, weight, means_of_trsp):
        # distance in km
        # weight in kg
        # means of trsp in ('car', 'cruise', 'flight')
        factor = cls.get_emission_factor(means_of_trsp, distance)
        emission = factor * distance * weight
        return emission*cls.GRAMS_TO_KILOGRAMS

    @classmethod
    def get_emission_factor(cls, means, distance):
        # returns factor: kg[CO2]/kg/km
        factor = 0
        factor_map = {
            'car': 0.080,
            'cruise': 0.0059,
            'flight': cls.get_flight_factor(distance)
        }
        factor = factor_map.get(means, "Invalid means")
        return factor

    @classmethod
    def get_flight_factor(cls, distance):
        AIR_THRESHOLD_1 = 200.0  # km
        AIR_THRESHOLD_2 = 500.0  # km
        flight_factor_min = 0.435  # g/km/kg
        flight_factor_max = 0.800  # g/km/kg

        if distance <= AIR_THRESHOLD_1:
            return flight_factor_max
        elif distance < AIR_THRESHOLD_2:
            return cls.map_value_linearly(distance,
                                          [AIR_THRESHOLD_1, AIR_THRESHOLD_2],
                                          [flight_factor_min, flight_factor_max])
        else:
            return flight_factor_min

    @classmethod
    def map_value_linearly(cls, value, source, target):
        return (value-source[0])/(source[1]-source[0]) \
               * (target[1] - target[0]) + target[0]
