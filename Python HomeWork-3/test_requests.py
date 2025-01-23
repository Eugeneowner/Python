import requests

BASE_URL = 'http://127.0.0.1:5000/students'

# Функция для записи результатов в файл
def log_to_file(message):
    with open('results.txt', 'a') as f:
        f.write(message + '\n')

# 1. Получить всех студентов (GET)
response = requests.get(BASE_URL)
print("GET /students:", response.status_code, response.json())
log_to_file("GET /students: " + str(response.status_code) + " " + str(response.json()))

# 2. Создать трех студентов (POST)
students_data = [
    {'first_name': 'John', 'last_name': 'Doe', 'age': 22},
    {'first_name': 'Jane', 'last_name': 'Smith', 'age': 23},
    {'first_name': 'Tom', 'last_name': 'Brown', 'age': 24}
]

for student in students_data:
    response = requests.post(BASE_URL, json=student)
    print("POST /students:", response.status_code, response.json())
    log_to_file("POST /students: " + str(response.status_code) + " " + str(response.json()))

# 3. Получить информацию о всех студентах после добавления новых студентов (GET)
response = requests.get(BASE_URL)
print("GET /students after adding:", response.status_code, response.json())
log_to_file("GET /students after adding: " + str(response.status_code) + " " + str(response.json()))

# 4. Обновить возраст второго студента (PATCH)
response = requests.patch(f"{BASE_URL}/2", json={'age': 25})
print("PATCH /students/2:", response.status_code, response.json())
log_to_file("PATCH /students/2: " + str(response.status_code) + " " + str(response.json()))

# 5. Получить информацию о втором студенте (GET)
response = requests.get(f"{BASE_URL}/2")
print("GET /students/2:", response.status_code, response.json())
log_to_file("GET /students/2: " + str(response.status_code) + " " + str(response.json()))

# 6. Обновить имя, фамилию и возраст третьего студента (PUT)
# Мы предположим, что ID третьего студента = 3
updated_student = {
    'first_name': 'Thomas',
    'last_name': 'Brownstein',
    'age': 26
}
response = requests.put(f"{BASE_URL}/3", json=updated_student)
print("PUT /students/3:", response.status_code, response.json())
log_to_file("PUT /students/3: " + str(response.status_code) + " " + str(response.json()))

# 7. Получить информацию о третьем студенте (GET)
response = requests.get(f"{BASE_URL}/3")
print("GET /students/3:", response.status_code, response.json())
log_to_file("GET /students/3: " + str(response.status_code) + " " + str(response.json()))

# 8. Получить всех студентов (GET) после всех изменений
response = requests.get(BASE_URL)
print("GET /students after updates:", response.status_code, response.json())
log_to_file("GET /students after updates: " + str(response.status_code) + " " + str(response.json()))

# 9. Удалить первого студента (DELETE)
# Мы предположим, что ID первого студента = 1
response = requests.delete(f"{BASE_URL}/1")
print("DELETE /students/1:", response.status_code, response.json())
log_to_file("DELETE /students/1: " + str(response.status_code) + " " + str(response.json()))

# 10. Получить всех студентов (GET) после удаления первого студента
response = requests.get(BASE_URL)
print("GET /students after delete:", response.status_code, response.json())
log_to_file("GET /students after delete: " + str(response.status_code) + " " + str(response.json()))