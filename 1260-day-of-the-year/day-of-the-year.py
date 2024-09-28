class Solution:
    def dayOfYear(self, date: str) -> int:
        days = {
            "01": 0,
            "02": 31,
            "03": 59,
            "04": 90,
            "05": 120,
            "06": 151,
            "07": 181,
            "08": 212,
            "09": 243,
            "10": 273,
            "11": 304,
            "12": 334
        }

        year, month, day = date.split("-")

        if int(month) > 2:
            if int(year) % 400 == 0:
                return days[month] + int(day) + 1
            elif int(year) % 4 == 0 and int(year) % 100 != 0:
                return days[month] + int(day) + 1
        
        return days[month] + int(day)