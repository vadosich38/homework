class Water:
    name = "water"
    answer = "Получается вода\n"

    def __add__(self, other):
        if other.name == "air":
            return Storm
        elif other.name == "land":
            return Dirt
        elif other.name == "fire":
            return Steam


class Air:
    name = "air"
    answer = "Получается воздух\n"

    def __add__(self, other):
        if other.name == "water":
            return Storm
        elif other.name == "land":
            return Dust
        elif other.name == "fire":
            return Zipp


class Land:
    name = "land"
    answer = "Получается земля\n"

    def __add__(self, other):
        if other.name == "water":
            return Dirt
        elif other.name == "air":
            return Dust
        elif other.name == "fire":
            return Lava


class Fire:
    name = "fire"
    answer = "Получается огонь\n"

    def __add__(self, other):
        if other.name == "water":
            return Steam
        elif other.name == "air":
            return Zipp
        elif other.name == "land":
            return Lava


class Zipp:
    answer = "Поулчается молния!\n"
    name = "zipp"

    def __add__(self, other):
        if other.name == "water":
            return Spark
        elif other.name == "air":
            return Thunder
        elif other.name == "land":
            return Earthquake
        elif other.name == "fire":
            return Flash


class Spark:
    name = "spark"
    answer = "Получается искра\n"


class Thunder:
    name = "thunder"
    answer = "Получается гром\n"


class Earthquake:
    name = "earthquake"
    answer = "Получается землетрясение\n"


class Flash:
    name = "flash"
    answer = "Получается вспышка"


class Lava:
    answer = "Поулчается лава!\n"
    name = "lava"

    def __add__(self, other):
        if other.name == "water":
            return Smoke
        elif other.name == "air":
            return FireRain
        elif other.name == "land":
            return Rock
        elif other.name == "fire":
            return Plasma


class Smoke:
    answer = "Поулчается дым!\n"
    name = "smoke"


class FireRain:
    answer = "Поулчается огненный дождь!\n"
    name = "firerain"


class Rock:
    answer = "Поулчается камень!\n"
    name = "rock"


class Plasma:
    answer = "Поулчается плазма!\n"
    name = "plasma"


class Dust:
    answer = "Поулчается пыль!\n"
    name = "dust"

    def __add__(self, other):
        if other.name == "water":
            return Dirt
        elif other.name == "air":
            return SandStorm
        elif other.name == "land":
            return Sand
        elif other.name == "fire":
            return Burn


class SandStorm:
    answer = "Поулчается песчаный шторм!\n"
    name = "sandstorm"


class Sand:
    answer = "Поулчается песок!\n"
    name = "sand"


class Burn:
    answer = "Поулчается гарь!\n"
    name = "burn"


class Storm:
    answer = "Поулчается шторм!\n"
    name = "storm"

    def __add__(self, other):
        if other.name == "water":
            return Tsunami
        elif other.name == "air":
            return Hurricane
        elif other.name == "land":
            return Drift
        elif other.name == "fire":
            return FireStorm


class FireStorm:
    answer = "Поулчается огненный шторм!\n"
    name = "fireStorm"


class Drift:
    answer = "Поулчается материковый дрейф!\n"
    name = "drift"


class Hurricane:
    answer = "Поулчается ураган!\n"
    name = "hurricane"


class Tsunami:
    answer = "Поулчается цунами!\n"
    name = "tsunami"


class Dirt:
    answer = "Поулчается грязь!\n"
    name = "dirt"

    def __add__(self, other):
        if other.name == "water":
            return Swamp
        elif other.name == "air":
            return Clay
        elif other.name == "land":
            return Mount
        elif other.name == "fire":
            return Vulcan

class Swamp:
    answer = "Поулчается болото!\n"
    name = "swamp"


class Clay:
    answer = "Поулчается глина!\n"
    name = "clay"

class Mount:
    answer = "Поулчается гора!\n"
    name = "mount"


class Vulcan:
    answer = "Поулчается вулкан!\n"
    name = "vulcan"

class Steam:
    answer = "Поулчается пар!\n"
    name = "steam"

    def __add__(self, other):
        if other.name == "water":
            return Condensate
        elif other.name == "air":
            return Rain
        elif other.name == "land":
            return Dew
        elif other.name == "fire":
            return Water


class Condensate:
    answer = "Поулчается конденсат!\n"
    name = "condensate"


class Rain:
    answer = "Поулчается дождь!\n"
    name = "rain"


class Dew:
    answer = "Поулчается роса!\n"
    name = "dew"
