class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __members(self):
        return (self.name, self.age)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__members() == other.__members()
        else:
            return False

    def __hash__(self):
        return hash(self.__members())


if __name__ == '__main__':
    Alex1 = Employee('Alex', 20)
    Alex2 = Employee('Alex', 20)
    Deepak = Employee("Deepak", 30)
    Deepak1 = Employee("Deepak", 30)
    Deepak2 = Employee("Deepak", 31)

    L = {Alex1, Alex1, Deepak, Deepak1, Deepak2}
    print(L)
    print(len(L))
