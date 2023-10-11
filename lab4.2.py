class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def set_income(self, wage, bonus):
        self._income["wage"] = wage
        self._income["bonus"] = bonus

    income = property(get_total_income, set_income)


employee1 = Position("Иван", "Иванов", "Менеджер", 2000, 200)
employee2 = Position("Петр", "Петров", "Аналитик", 2500, 250)
employee3 = Position("Евгений", "Карпенко", "Строитель", 1230, 400)

print("Имя сотрудника 1:", employee1.name)
print("Должность сотрудника 2:", employee2.position)
print("Должность сотрудника 3 ", employee3.position)

print("Полное имя сотрудника 1:", employee1.get_full_name())
print(f"Общий доход с учетом премии сотрудника 2:{employee2.income} и сотрудника 3:{employee3.income}")
print("")
