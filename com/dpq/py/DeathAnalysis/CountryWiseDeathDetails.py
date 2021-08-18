class CountryWiseDeathDetails:

    def __init__(self, year, country, gender, deaths):
        self.year = year
        self.country = country
        self.gender = gender
        self.deaths = deaths

    def __members(self):
        # return (self.year, self.country, self.gender)
        return (self.country)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__members() == other.__members()
        else:
            return False

    def __hash__(self):
        return hash(self.__members())

    def __str__(self):
        return str(self.year) + " " + self.country + " " + self.gender + " " + str(self.deaths)


if __name__ == '__main__':
    details = CountryWiseDeathDetails(2001, 'france', 'female', 201)
    details1 = CountryWiseDeathDetails(2002, 'france', 'male', 301)
    details2 = CountryWiseDeathDetails(2002, 'france', 'male', 300)
    print({details, details1, details2})
    lst = [details1, details2, details]
    map = {}

    for detail in lst:
        if detail in map:
            map[detail] += detail.deaths
        else:
            map[detail] = detail.deaths

    print(map)


