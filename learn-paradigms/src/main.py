class HouseScheme:
    def __init__(self, rooms, area, bathroomAvailability):
        if (area < 0) or ((bathroomAvailability is not True) and (bathroomAvailability is not False)):
            raise ValueError("Invalid value")

        self.rooms = rooms
        self.area = area
        self.bathroomAvailability = bathroomAvailability


class CountryHouse(HouseScheme):
    def __init__(self, rooms, area, bathroomAvailability, floors, landArea):
        HouseScheme.__init__(self, rooms, area, bathroomAvailability)
        self.floors = floors
        self.landArea = landArea

    def __str__(self):
        return "Country House: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Количество этажей {}, Площадь участка {}.".format(self.rooms, self.area, self.bathroomAvailability, self.floors, self.landArea)

    def __eq__(self, other):
        return (self.area == other.area) and (self.landArea == other.landArea) and (abs(self.floors - other.floors) <= 1)


class Apartment(HouseScheme):
    def __init__(self, rooms, area, bathroomAvailability, floor, side):
        HouseScheme.__init__(self, rooms, area, bathroomAvailability)
        self.floor = floor
        self.side = side

        if self.floor < 1 or self.floor > 15:
            raise ValueError("Invalid value")

        if self.side not in ["N", "S", "W", "E"]:
            raise ValueError("Invalid value")

    def __str__(self):
        return "Apartment: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Этаж {}, Окна выходят на {}.".format(self.rooms, self.area, self.bathroomAvailability, self.floor, self.side)


class CountryHouseList(list):
    def __init__(self, name):
        list.__init__(self)
        self.name = name

    def append(self, p_object):
        if isinstance(p_object, CountryHouse):
            list.append(self, p_object)
        else:
            raise TypeError("Invalid type {}".format(type(p_object)))

    def total_square(self):
        return sum([x.area for x in self])


class ApartmentList(list):
    def __init__(self, name):
        list.__init__(self)
        self.name = name

    def extend(self, iterable):
        filteredIterable = filter(lambda x: isinstance(x, Apartment), iterable)
        list.extend(self, filteredIterable)

    def floor_view(self, floors, directions):
        filteredApartmentList = filter(lambda x: (x.floor >= floors[0]) and (x.floor <= floors[1]) and (x.side in directions), self)
        for i in filteredApartmentList:
            print("{}: {}".format(i.side, i.floor))
