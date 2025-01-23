from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

# Путь к файлу CSV
CSV_FILE = 'students.csv'

# Проверка существования файла и создание заголовков, если файл пуст
def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'first_name', 'last_name', 'age'])

# Чтение данных студентов из CSV файла
def read_students():
    students = []
    with open(CSV_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

# Запись данных студентов в CSV файл
def write_students(students):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'first_name', 'last_name', 'age'])
        writer.writeheader()
        writer.writerows(students)

init_csv()

# Получить список всех студентов
@app.route('/students', methods=['GET'])
def get_students():
    students = read_students()
    return jsonify(students), 200

# Получить информацию о студенте по ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    students = read_students()
    student = next((s for s in students if int(s['id']) == id), None)
    if student:
        return jsonify(student), 200
    return jsonify({'message': 'Student not found'}), 404

# Получить информацию о студентах по фамилии
@app.route('/students/lastname/<string:last_name>', methods=['GET'])
def get_students_by_last_name(last_name):
    students = read_students()
    matched_students = [s for s in students if s['last_name'].lower() == last_name.lower()]
    if matched_students:
        return jsonify(matched_students), 200
    return jsonify({'message': f"No students found with last name '{last_name}'"}), 404

# Экспорт данных в JSON
@app.route('/students/export', methods=['GET'])
def export_students_to_json():
    students = read_students()
    return jsonify(students), 200

# Добавить нового студента
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    
    # Проверка
    required_fields = {'first_name', 'last_name', 'age'}
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    if not required_fields.issubset(data):
        missing = required_fields - data.keys()
        return jsonify({'error': f'Missing fields: {", ".join(missing)}'}), 400
    if any(key not in required_fields for key in data.keys()):
        extra_fields = set(data.keys()) - required_fields
        return jsonify({'error': f'Invalid fields: {", ".join(extra_fields)}'}), 400
    
    students = read_students()
    new_id = max([int(s['id']) for s in students], default=0) + 1
    
    try:
        new_student = {
            'id': new_id,
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'age': int(data['age']) 
        }
    except ValueError:
        return jsonify({'error': 'Age must be an integer'}), 400
    
    students.append(new_student)
    write_students(students)
    return jsonify(new_student), 201

# Обновить информацию о студенте
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    # Проверка, на все обязательные поля
    required_fields = {'first_name', 'last_name', 'age'}
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    if not required_fields.issubset(data):
        missing = required_fields - data.keys()
        return jsonify({'error': f'Missing fields: {", ".join(missing)}'}), 400
    if any(key not in required_fields for key in data.keys()):
        extra_fields = set(data.keys()) - required_fields
        return jsonify({'error': f'Invalid fields: {", ".join(extra_fields)}'}), 400
    
    students = read_students()
    student = next((s for s in students if int(s['id']) == id), None)

    if student:
        student['first_name'] = data['first_name']
        student['last_name'] = data['last_name']
        try:
            student['age'] = int(data['age']) 
        except ValueError:
            return jsonify({'error': 'Age must be an integer'}), 400

        write_students(students)
        return jsonify(student), 200  
    else:
        return jsonify({'message': 'Student not found'}), 404 

# Частично обновить информацию о студенте.
@app.route('/students/<int:id>', methods=['PATCH'])
def patch_student(id):
    data = request.get_json()
    
    # Проверка на наличие данных.
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    if 'age' not in data:
        return jsonify({'error': 'Missing field: age'}), 400
    if len(data) > 1: 
        return jsonify({'error': 'Only age field can be updated'}), 400

    students = read_students()
    student = next((s for s in students if int(s['id']) == id), None)

    if student:
        try:
            student['age'] = int(data['age'])  
        except ValueError:
            return jsonify({'error': 'Age must be an integer'}), 400

        write_students(students)
        return jsonify(student), 200 
    else:
        return jsonify({'message': 'Student not found'}), 404  
# Удалить студента
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    students = read_students()  
    student = next((s for s in students if int(s['id']) == id), None)  # Поиск студента по ID

    if student:
        students = [s for s in students if int(s['id']) != id]
        write_students(students)  # Перезапись данных в CSV файл
        return jsonify({'message': 'Student deleted'}), 200  
    else:
        return jsonify({'message': 'Student not found'}), 404
if __name__ == '__main__':
    app.run(debug=True)