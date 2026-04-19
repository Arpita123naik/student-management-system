import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Configuration for the data file
DATA_FILE = 'students.json'

# --- Helper Functions ---
def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_students(students):
    with open(DATA_FILE, 'w') as f:
        json.dump(students, f, indent=4)

# --- Routes ---

# 1. Home Page (Index) - List all students
@app.route('/')
def index():
    students = load_students()
    return render_template('index.html', students=students)

# 2. Add Student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Get data from form
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        
        new_student = {
            'id': str(len(load_students()) + 1), # Simple ID generation
            'name': name,
            'age': age,
            'grade': grade
        }
        
        students = load_students()
        students.append(new_student)
        save_students(students)
        
        return redirect(url_for('index'))
    
    return render_template('add.html')

# 3. Search Student
@app.route('/search', methods=['GET', 'POST'])
def search_student():
    students = load_students()
    results = []
    
    if request.method == 'POST':
        search_term = request.form.get('search_term', '').lower()
        # Filter students by name or ID
        results = [s for s in students if search_term in s['name'].lower() or search_term in str(s['id'])]
        return render_template('search.html', students=results)
        
    return render_template('search.html', students=students)

# 4. Delete Student
@app.route('/delete/<string:id>')
def delete_student(id):
    students = load_students()
    # Keep students that do NOT match the ID
    students = [s for s in students if s['id'] != id]
    save_students(students)
    return redirect(url_for('index'))

# 5. Update Student (Pre-fill form)
@app.route('/update/<string:id>', methods=['GET', 'POST'])
def update_student(id):
    students = load_students()
    student = next((s for s in students if s['id'] == id), None)
    
    if request.method == 'POST':
        if student:
            student['name'] = request.form['name']
            student['age'] = request.form['age']
            student['grade'] = request.form['grade']
            save_students(students)
        return redirect(url_for('index'))
        
    return render_template('update.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)