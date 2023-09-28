def sec(): ## ההבדל בין קריאה לגנרטור לקריאה למשתנה השומר אותו
    # קריאה לגנרטור מתחילה את הגנרטור  מהתחלהואילו קריאה למשתנה השומר אותו עוברת לאיבר הבא בגנרטור
    for a in range(2):
        yield a
def main():
    t=sec()
    for j in range(2):
       for i in t:#  כאשר שמים בלולאה את המשתנה אז הערך שהגנרטור מחזיר בסיבוב השני שקוראים ללולאה אינו משתנה
           # נשאר ערך 1
        print(i)
if __name__ == '__main__':
    main()
def sec():
    for a in range(2):
        yield a
def main():
    t=sec()
    for j in range(2):
       for i in sec():# אבל אם שמים בלולאה לא את שם המשתנה אלא קריאה לגנרטור
           # אזי בסיבוב הבא שקוראים ללולאה היא מאתחלת את הגנרטור מהתחלה(חוזר לערך 0)
        print(i)
if __name__ == '__main__':
    main()
"""לסיכום"""
def gen3():
    yield 1
    yield 2
x = gen3()
print(next(gen3()))#1
print(next(gen3()))#1
print(next(x))#1
print(next(x))#2
#5.3
class Employee:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    def get_name(self):
        return self._name

class EmployeeManager:
    def __init__(self):
        self._employee_lst = []
        self.eml_index = -1

    def add_employee(self, new_empl):
        self._employee_lst.append(new_empl)

    def __iter__(self):
        return self

def __next__(self):
    if self.eml_index >= len(self._employee_lst) - 1:
        raise StopIteration()
    self.eml_index += 1
    return self._employee_lst[self.eml_index].get_name()

def main():
    manager = EmployeeManager()
    manager.add_employee(Employee("Lia Levi", 30, 5000))
    manager.add_employee(Employee("Yosef Cohen", 32, 4800))
    manager.add_employee(Employee("Oded Haim", 47, 5100))
    for emp_name in manager:
        print(emp_name)
if __name__ == '__main__':
    main()

#   שעושים list או dict על גנרטור הוא מביא(שומר) את כל הערכים שבהם (כאילו רץ בלולאה על כל הכל)
# לדוגמא:
square_iter =((x,x+1) for x in range(1,11,2))# גנרטור ששומר כל פעם שני ערכים

x=dict(square_iter)
print(x)

#output:
{1: 2, 3: 4, 5: 6, 7: 8, 9: 10}