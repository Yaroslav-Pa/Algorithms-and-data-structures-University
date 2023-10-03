from datetime import datetime

employees = [
    {
        "прізвище": "Іванов",
        "ім`я": "Петро",
        "по батькові": "Олександрович",
        "посада": "інженер",
        "стаж": 5,
        "домашня адреса": "вул. Головна, 123",
        "дата народження": "1990-05-15"
    },
        {
        "прізвище": "Іванов",
        "ім`я": "Данило",
        "по батькові": "Олександрович",
        "посада": "інженер",
        "стаж": 4,
        "домашня адреса": "вул. Головна, 123",
        "дата народження": "1990-05-15"
    },
    {
        "прізвище": "Петрова",
        "ім`я": "Марія",
        "по батькові": "Іванівна",
        "посада": "бухгалтер",
        "стаж": 2,
        "домашня адреса": "вул. Центральна, 45",
        "дата народження": "1992-10-20"
    },
    {
        "прізвище": "Сидоренко",
        "ім`я": "Олег",
        "посада": "менеджер",
        "стаж": 3,
        "домашня адреса": "вул. Паркова, 67",
        "дата народження": "1992-03-30"
    }
]

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and (calculateAge(arr[i]["дата народження"]) < calculateAge(arr[left]["дата народження"]) or
                     (calculateAge(arr[i]["дата народження"]) == calculateAge(arr[left]["дата народження"]) and arr[i]["стаж"] < arr[left]["стаж"])):
        largest = left

    if right < n and (calculateAge(arr[largest]["дата народження"]) < calculateAge(arr[right]["дата народження"]) or
                      (calculateAge(arr[largest]["дата народження"]) == calculateAge(arr[right]["дата народження"]) and arr[largest]["стаж"] < arr[right]["стаж"])):
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def calculateAge(date_of_birth):
    today = datetime.today()
    birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
    age = today.year - birth_date.year
    return age

heapSort(employees)

for employee in employees:
    age = calculateAge(employee["дата народження"])
    print(f"{employee['прізвище']} {employee['ім`я']} - {age} років, стаж: {employee['стаж']} років")





