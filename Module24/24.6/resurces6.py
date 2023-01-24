class Water:
    __name = "water"

    def __str__(self):
        return "Получается вода\n"

    def get_name(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm
        elif isinstance(other, Land):
            return Dirt
        elif isinstance(other, Fire):
            return Steam


class Air:
    __name = "air"

    def __str__(self):
        return "Получается воздух\n"

    def get_name(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm
        elif isinstance(other, Land):
            return Dust
        elif isinstance(other, Fire):
            return Zipp


class Land:
    __name = "land"

    def __str__(self):
        return "Получается земля\n"

    def get_name(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt
        elif isinstance(other, Air):
            return Dust
        elif isinstance(other, Fire):
            return Lava


class Fire:
    __name = "fire"

    def __str__(self):
        return "Получается огонь\n"

    def get_name(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam
        elif isinstance(other, Air):
            return Zipp
        elif isinstance(other, Land):
            return Lava


class Zipp:
    __name = "zipp"

    def __str__(self):
        return "Поулчается молния!\n"

    def get_name(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Water):
            return Spark
        elif isinstance(other, Air):
            return Thunder
        elif isinstance(other, Land):
            return Earthquake
        elif isinstance(other, Fire):
            return Flash


class Spark:
    __name = "spark"

    def __str__(self):
        return "Получается искра\n"

    def get_name(self):
        return self.__name


class Thunder:
    __name = "thunder"

    def __str__(self):
        return "Получается гром\n"

    def get_name(self):
        return self.__name


class Earthquake:
    __name = "earthquake"

    def __str__(self):
        return "Получается землетрясение\n"

    def get_name(self):
        return self.__name


class Flash:
    __name = "flash"

    def __str__(self):
        return "Получается вспышка"

    def get_name(self):
        return self.__name


class Lava:
    __name = "lava"

    def __str__(self):
        return "Поулчается лава!\n"

    def get_name(self):
        return self.__name

    def __add__(self, other):
        if other.name == "water":
            return Smoke
        elif isinstance(other, Air):
            return FireRain
        elif isinstance(other, Land):
            return Rock
        elif isinstance(other, Fire):
            return Plasma


class Smoke:
    __name = "smoke"

    def __str__(self):
        return "Поулчается дым!\n"

    def get_name(self):
        return self.__name


class FireRain:
    __name = "firerain"

    def __str__(self):
        return "Поулчается огненный дождь!\n"

    def get_name(self):
        return self.__name


class Rock:
    __name = "rock"

    def __str__(self):
        return "Поулчается камень!\n"

    def get_name(self):
        return self.__name


class Plasma:
    __name = "plasma"

    def __str__(self):
        return "Поулчается плазма!\n"

    def get_name(self):
        return self.__name


class Dust:
    __name = "dust"

    def __str__(self):
        return "Поулчается пыль!\n"

    def get_name(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt
        elif isinstance(other, Air):
            return SandStorm
        elif isinstance(other, Land):
            return Sand
        elif isinstance(other, Fire):
            return Burn


class SandStorm:
    __name = "sandstorm"

    def __str__(self):
        return "Поулчается песчаный шторм!\n"

    def get_name(self):
        return self.__name


class Sand:
    __name = "sand"

    def __str__(self):
        return "Поулчается песок!\n"

    def get_name(self):
        return self.__name


class Burn:
    __name = "burn"

    def __str__(self):
        return "Поулчается гарь!\n"

    def get_name(self):
        return self.__name


class Storm:
    __name = "storm"

    def __str__(self):
        return "Поулчается шторм!\n"

    def get_name(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Water):
            return Tsunami
        elif isinstance(other, Air):
            return Hurricane
        elif isinstance(other, Land):
            return Drift
        elif isinstance(other, Fire):
            return FireStorm


class FireStorm:
    __name = "fireStorm"

    def __str__(self):
        return "Поулчается огненный шторм!\n"

    def get_name(self):
        return self.__name


class Drift:
    __name = "drift"

    def __str__(self):
        return "Поулчается материковый дрейф!\n"

    def get_name(self):
        return self.__name


class Hurricane:
    __name = "hurricane"

    def __str__(self):
        return "Поулчается ураган!\n"

    def get_name(self):
        return self.__name


class Tsunami:
    __name = "tsunami"

    def __str__(self):
        return "Поулчается цунами!\n"

    def get_name(self):
        return self.__name


class Dirt:
    __name = "dirt"

    def __str__(self):
        return "Поулчается грязь!\n"

    def get_name(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Water):
            return Swamp
        elif isinstance(other, Air):
            return Clay
        elif isinstance(other, Land):
            return Mount
        elif isinstance(other, Fire):
            return Vulcan


class Swamp:
    __name = "swamp"

    def __str__(self):
        return "Поулчается болото!\n"

    def get_name(self):
        return self.__name


class Clay:
    __name = "clay"

    def __str__(self):
        return "Поулчается глина!\n"

    def get_name(self):
        return self.__name


class Mount:
    __name = "mount"

    def __str__(self):
        return "Поулчается гора!\n"

    def get_name(self):
        return self.__name


class Vulcan:
    __name = "vulcan"

    def __str__(self):
        return "Поулчается вулкан!\n"

    def get_name(self):
        return self.__name


class Steam:
    __name = "steam"

    def __str__(self):
        return "Поулчается пар!\n"

    def get_name(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Water):
            return Condensate
        elif isinstance(other, Air):
            return Rain
        elif isinstance(other, Land):
            return Dew
        elif isinstance(other, Fire):
            return Water


class Condensate:
    __name = "condensate"

    def __str__(self):
        return "Поулчается конденсат!\n"

    def get_name(self):
        return self.__name


class Rain:
    __name = "rain"

    def __str__(self):
        return "Поулчается дождь!\n"

    def get_name(self):
        return self.__name


class Dew:
    __name = "dew"

    def __str__(self):
        return "Поулчается роса!\n"

    def get_name(self):
        return self.__name
