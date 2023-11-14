class Musician:
    def __init__(self, id, last_name, salary, orchestra_id):
        self.id = id
        self.last_name = last_name
        self.salary = salary
        self.orchestra_id = orchestra_id

class Orchestra:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class MusiciansOrchestra:
    def __init__(self, musician_id, orchestra_id):
        self.musician_id = musician_id
        self.orchestra_id = orchestra_id

musicians = [
    Musician(1, 'Smith', 30000, 1),
    Musician(2, 'Johnson', 35000, 2),
    Musician(3, 'Williams', 40000, 1),
    Musician(4, 'Jones', 32000, 2),
    Musician(5, 'Brown', 28000, 1)
]

orchestras = [
    Orchestra(1, 'Symphony Orchestra'),
    Orchestra(2, 'Chamber Orchestra')
]

musicians_orchestras = [
    MusiciansOrchestra(1, 1),
    MusiciansOrchestra(2, 2),
    MusiciansOrchestra(3, 1),
    MusiciansOrchestra(4, 2),
    MusiciansOrchestra(5, 1)
]

# Task 1
task_1_result = [(m.last_name, o.name)
                 for m in musicians
                 for o in orchestras
                 if m.orchestra_id == o.id and m.last_name.endswith('th')]
print("Task 1 Result:", task_1_result)

# Task 2
avg_salaries = {}
for o in orchestras:
    o_musicians = [m.salary for m in musicians if m.orchestra_id == o.id]
    avg_salaries[o.name] = sum(o_musicians) / len(o_musicians) if len(o_musicians) > 0 else 0

sorted_avg_salaries = sorted(avg_salaries.items(), key=lambda x: x[1], reverse=True)
print("Task 2 Result:", sorted_avg_salaries)

# Task 3
task_3_result = {o.name: [m.last_name for m in musicians if m.orchestra_id == o.id] for o in orchestras if o.name.startswith('C')}
print("Task 3 Result:", task_3_result)
