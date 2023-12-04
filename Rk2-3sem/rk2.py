class Musician:
    def __init__(self, id, last_name, salary, orchestra_id):
        self.id = id
        self.last_name = last_name
        self.salary = salary
        self.orchestra_id = orchestra_id

class Orchestra:
    # Класс Orchestra остается без изменений.
    def __init__(self, id, name):
        self.id = id
        self.name = name

class MusiciansOrchestra:
    # Класс MusiciansOrchestra остается без изменений.
    def __init__(self, musician_id, orchestra_id):
        self.musician_id = musician_id
        self.orchestra_id = orchestra_id

# Функция для задачи 1
def filter_musicians_by_last_name_and_orchestra(musicians, orchestras, last_name_suffix):
    return [(m.last_name, o.name)
            for m in musicians
            for o in orchestras
            if m.orchestra_id == o.id and m.last_name.endswith(last_name_suffix)]

# Функция для задачи 2
def calculate_average_salaries(musicians, orchestras):
    avg_salaries = {}
    for o in orchestras:
        o_musicians = [m.salary for m in musicians if m.orchestra_id == o.id]
        avg_salaries[o.name] = sum(o_musicians) / len(o_musicians) if len(o_musicians) > 0 else 0
    return sorted(avg_salaries.items(), key=lambda x: x[1], reverse=True)

# Функция для задачи 3
def filter_orchestras_and_list_musicians(musicians, orchestras, name_prefix):
    return {o.name: [m.last_name for m in musicians if m.orchestra_id == o.id] for o in orchestras if o.name.startswith(name_prefix)}

# Пример использования данных
musicians = [
    # Ваши данные...
    Musician(1, 'Smith', 30000, 1),
    Musician(2, 'Johnson', 35000, 2),
    Musician(3, 'Williams', 40000, 1),
    Musician(4, 'Jones', 32000, 2),
    Musician(5, 'Brown', 28000, 1)    
]

orchestras = [
    # Ваши данные...
    Orchestra(1, 'Symphony Orchestra'),
    Orchestra(2, 'Chamber Orchestra')
]

musicians_orchestras = [
    # Ваши данные...
    MusiciansOrchestra(1, 1),
    MusiciansOrchestra(2, 2),
    MusiciansOrchestra(3, 1),
    MusiciansOrchestra(4, 2),
    MusiciansOrchestra(5, 1)
]

# Вызов функций
print("Task 1 Result:", filter_musicians_by_last_name_and_orchestra(musicians, orchestras, 'th'))
print("Task 2 Result:", calculate_average_salaries(musicians, orchestras))
print("Task 3 Result:", filter_orchestras_and_list_musicians(musicians, orchestras, 'C'))

import unittest

class TestFilterMusiciansByLastNameAndOrchestra(unittest.TestCase):
    def test_filter_by_suffix(self):
        musicians = [Musician(1, 'Smith', 30000, 1), Musician(2, 'Johnson', 35000, 2)]
        orchestras = [Orchestra(1, 'Symphony Orchestra'), Orchestra(2, 'Chamber Orchestra')]
        result = filter_musicians_by_last_name_and_orchestra(musicians, orchestras, 'th')
        self.assertEqual(result, [('Smith', 'Symphony Orchestra')])

class TestCalculateAverageSalaries(unittest.TestCase):
    def test_average_salaries(self):
        musicians = [Musician(1, 'Smith', 30000, 1), Musician(2, 'Johnson', 35000, 1)]
        orchestras = [Orchestra(1, 'Symphony Orchestra')]
        result = calculate_average_salaries(musicians, orchestras)
        self.assertEqual(result, [('Symphony Orchestra', 32500.0)])
class TestFilterOrchestrasAndListMusicians(unittest.TestCase):
    def test_filter_orchestras(self):
        musicians = [Musician(1, 'Smith', 30000, 1), Musician(2, 'Johnson', 35000, 2)]
        orchestras = [Orchestra(1, 'Symphony Orchestra'), Orchestra(2, 'Chamber Orchestra')]
        result = filter_orchestras_and_list_musicians(musicians, orchestras, 'C')
        self.assertEqual(result, {'Chamber Orchestra': ['Johnson']})
if __name__ == '__main__':
    unittest.main()
