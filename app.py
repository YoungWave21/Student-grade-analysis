import random


class Grades:
    def __init__(self):
        self.grades = []
        self.randomize_grades()

    def randomize_grades(self):
        for i in range(50):
            self.grades.append(random.randint(0, 100))
        print("Grades randomized")

    def display_all(self):
        for i in range(len(self.grades)):
            print(f'Student {i + 1}: {self.grades[i]}%')

    def stats(self):
        print(f'The highest grade in the class is: {max(self.grades)}%')
        print(f'The lowest grade in the class is: {min(self.grades)}%')
        sum_total = 0
        for i in range(len(self.grades)):
            sum_total += self.grades[i]
        print(f'The class average is: {round(sum_total / len(self.grades), 1)}%')

    def count_honors(self):
        total = 0
        for i in range(len(self.grades)):
            if self.grades[i] > 80:
                total += 1
        print(f'There are {total} student who have received honors')

    def remove_failing(self):
        sum_total = 0
        for i in reversed(range(len(self.grades))):
            if self.grades[i] < 50:
                sum_total += 1
                self.grades.pop(i)
        print(f'Removed {sum_total} students')


def main():
    person = Grades()
    while True:
        print("______________________________")
        print("Main Menu:")
        print("1.Display All Grades")
        print("2.Randomize Grades")
        print("3.Stats")
        print("4.Count Honors")
        print("5.Remove Failing")
        print("6.Exit")
        print("______________________________")
        choice = input("Your choice: ")
        if choice.isnumeric() and 0 < int(choice) < 7:
            options = {
                1: person.display_all,
                2: person.randomize_grades,
                3: person.stats,
                4: person.count_honors,
                5: person.remove_failing,
                6: exit,
            }
            options[int(choice)]()
        else:
            print("The option you have selected does not exist!")


main()
