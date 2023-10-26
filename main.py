import sqlite3
from pprint import pprint
from seeds import create_db

DB = 'hw.db'
QUERY_DICT = {
    '0': 'Exit',
    '1': '1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.',
    '2': '2. Знайти студента із найвищим середнім балом з певного предмета.',
    '3': '3. Знайти середній бал у групах з певного предмета.',
    '4': '4. Знайти середній бал на потоці (по всій таблиці оцінок).',
    '5': '5. Знайти які курси читає певний викладач.',
    '6': '6. Знайти список студентів у певній групі.',
    '7': '7. Знайти оцінки студентів у окремій групі з певного предмета.',
    '8': '8. Знайти середній бал, який ставить певний викладач зі своїх предметів.',
    '9': '9. Знайти список курсів, які відвідує студент.',
    '10': '10. Список курсів, які певному студенту читає певний викладач.',
    '11': '11. Середній бал, який певний викладач ставить певному студентові.',
    '12': '12. Оцінки студентів у певній групі з певного предмета на останньому занятті.'
}


def execute_query(sql_instruction, DB):
    with open(sql_instruction, 'r', encoding="utf-8") as fd:
        sql = fd.read()
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


def executescript_query(sql_instruction, DB):
    with open(sql_instruction, 'r', encoding="utf-8") as fd:
        sql = fd.read()
    with sqlite3.connect(DB) as conn:
        cur = conn.cursor()
        cur.executescript(sql)
        return cur.fetchall()


if __name__ == '__main__':
    print(r'''
    --------------------------------------------------
     Учні Хргвардсу цілий рік гризли граніт науки,
    якщо бажаєти подивитись їх результати натисніть 1.
     Там все проплачено, створимо нову базу зі своїми
    карапузами, натисніть 2
    --------------------------------------------------
    ''')

    while True:
        user_input = input('-->', )
        if user_input == '1':
            break
        elif user_input == '2':
            executescript_query('create_db.sql', DB)
            create_db()
            print('Нова база створена, можна і попрацювати')
            break
        else:
            print('Зробіть вибір між 1 та 2, це не так важко як здається')
    for key, value in QUERY_DICT.items():
        print(key, ":", value)
    while True:
        print('-' * 80)
        user_input = input('Введть номер завдання, або 0, щоб вийти: ')
        if user_input == '0':
            print('До побачення')
            break
        if user_input in QUERY_DICT:
            try:
                sql_query = f'query_{user_input}.sql'
                print(QUERY_DICT.get(user_input))
                pprint(execute_query(sql_query, DB))
            except FileNotFoundError as error:
                print(error)
        else:
            print(f'Щось пішло не так: "{user_input}". Спробуйте ще раз...')
