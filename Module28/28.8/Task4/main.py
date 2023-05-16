class Date:
    def __init__(self, day, month, year) -> None:
        self.__year = year
        self.__month = month
        self.__day = day

    def __str__(self) -> str:
        return "День: {}, месяц: {}, год: {}".format(self.__day, self.__month, self.__year)

    @classmethod
    def from_string(cls, text) -> "Date":
        day, month, year = map(int, text.split("-"))
        return cls(day=day, month=month, year=year)

    @classmethod
    def is_date_valid(cls, text) -> bool:
        day, month, year = map(int, text.split("-"))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year < 9999


date = Date.from_string(text='10-12-2077')
print(date)
print(Date.is_date_valid(text='10-12-2077'))
print(Date.is_date_valid(text='40-12-2077'))
