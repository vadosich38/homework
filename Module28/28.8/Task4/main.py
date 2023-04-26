class Date:
    def __init__(self, day, month, year) -> None:
        self.__year = year
        self.__month = month
        self.__day = day

    def __str__(self) -> str:
        return "День: {}, месяц: {}, год: {}".format(self.__day, self.__month, self.__year)

    @classmethod
    def from_string(cls, text) -> "Date":
        day, month, year = text.split("-")
        return Date(day=day, month=month, year=year)

    @classmethod
    def is_date_valid(cls, text) -> bool:
        day, month, year = text.split("-")
        if 31 >= int(day) >= 1 and 1 <= int(month) <= 12 and int(year) > 0:
            return True

        return False


date = Date.from_string(text='10-12-2077')
print(date)
print(Date.is_date_valid(text='10-12-2077'))
print(Date.is_date_valid(text='40-12-2077'))
