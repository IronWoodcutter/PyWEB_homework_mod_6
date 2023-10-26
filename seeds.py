import faker
import sqlite3
from datetime import datetime, date, timedelta
from random import randint

NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50

disciplines = [
    'Астрономія', 'Заклинання', 'Зілляварення',
    'Історія магії', 'Травологія', 'Трансфігурація',
    'Польоти на мітлах', 'Захист від темних мистецтв'
]

groups = ['Гриффіндор', 'Пуффендуй', 'Слізерін']

fake = faker.Faker()
connect = sqlite3.connect('hw.db')
c = connect.cursor()


def seed_teachers():
    teachers = [fake.name() for _ in range(NUMBER_TEACHERS)]
    sql = 'INSERT INTO teachers(fullname) VALUES (?)'
    c.executemany(sql, zip(teachers, ))


def seed_disciplines():
    sql = 'INSERT INTO disciplines(name, teacher_id) VALUES (?, ?)'
    c.executemany(sql, zip(disciplines, iter(randint(1, NUMBER_TEACHERS) for _ in range(len(disciplines)))))


def seed_groups():
    sql = 'INSERT INTO groups(name) VALUES (?)'
    c.executemany(sql, zip(groups, ))


def seed_students():
    students = [fake.name() for _ in range(NUMBER_STUDENTS)]
    sql = 'INSERT INTO students(fullname, group_id) VALUES (?, ?)'
    c.executemany(sql, zip(students, iter(randint(1, len(groups)) for _ in range(len(students)))))


def seed_grades():
    start_date = datetime.strptime('2022-09-01', '%Y-%m-%d')
    end_date = datetime.strptime('2023-06-15', '%Y-%m-%d')
    sql = 'INSERT INTO grades(discipline_id, student_id, grade, date_of) VALUES (?, ?, ?, ?)'

    def get_list_date(start: date, end: date):
        result = []
        current_date = start
        while current_date <= end:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)

        return result

    list_dates = get_list_date(start_date, end_date)

    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1, NUMBER_STUDENTS) for _ in range(5)]
        for student in random_students:
            grades.append((random_discipline, student, randint(1, 100), day.date()))
    c.executemany(sql, grades)


def create_db():
    try:
        seed_teachers()
        seed_disciplines()
        seed_groups()
        seed_students()
        seed_grades()
        connect.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        connect.close()


if __name__ == '__main__':
    create_db()
