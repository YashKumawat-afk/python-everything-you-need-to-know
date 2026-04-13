# 🐍 Python — Everything You Need to Know

> A comprehensive Python learning repository covering fundamentals to advanced topics, with real-world library implementations used in data science, ML, web dev, and automation projects.

---

## 📁 Repository Structure

```
python-everything-you-need-to-know/
│
├── 01_basics/
│   ├── variables_and_datatypes.py
│   ├── control_flow.py
│   ├── functions.py
│   ├── loops.py
│   └── exception_handling.py
│
├── 02_oop/
│   ├── classes_and_objects.py
│   ├── inheritance.py
│   ├── dunder_methods.py
│   └── decorators.py
│
├── 03_data_structures/
│   ├── lists_tuples_sets.py
│   ├── dictionaries.py
│   ├── comprehensions.py
│   └── stacks_queues.py
│
├── 04_file_handling/
│   ├── read_write_files.py
│   ├── csv_handling.py
│   └── json_handling.py
│
├── 05_libraries/
│   ├── numpy_basics.py
│   ├── pandas_basics.py
│   ├── matplotlib_basics.py
│   ├── seaborn_basics.py
│   ├── scikit_learn_basics.py
│   ├── requests_basics.py
│   ├── flask_basics.py
│   └── os_sys_basics.py
│
├── 06_projects/
│   ├── student_grade_analyzer/
│   ├── weather_dashboard/
│   └── mini_ml_classifier/
│
└── README.md
```

---

## 🚀 Topics Covered

### ✅ 1. Python Basics
- Variables, Data Types, Type Casting
- Conditionals, Loops, Functions
- Lambda, *args, **kwargs
- Exception Handling (try/except/finally)
- List/Dict/Set Comprehensions

### ✅ 2. Object-Oriented Programming
- Classes, Objects, `__init__`
- Inheritance & Polymorphism
- Dunder/Magic Methods
- Decorators (`@staticmethod`, `@classmethod`, `@property`)

### ✅ 3. Data Structures & Algorithms
- Built-in: list, tuple, set, dict
- Stack, Queue, Linked List in Python
- Sorting algorithms from scratch

### ✅ 4. File & Data Handling
- File I/O (text, binary)
- CSV with `csv` and `pandas`
- JSON parsing and writing

### ✅ 5. Libraries (with implementations)
See section below ⬇️

### ✅ 6. Mini Projects
- Student Grade Analyzer (pandas + matplotlib)
- Weather Dashboard (requests + API)
- Mini ML Classifier (scikit-learn)

---

## 📦 Libraries & Implementations

### 🔢 NumPy
```python
import numpy as np

# Array creation
arr = np.array([1, 2, 3, 4, 5])
matrix = np.zeros((3, 3))
rand = np.random.randint(0, 100, (4, 4))

# Operations
print(arr.mean(), arr.std(), arr.sum())
print(rand @ rand.T)          # Matrix multiplication
print(np.linspace(0, 1, 5))   # Evenly spaced values

# Indexing & Slicing
print(rand[1:3, 0:2])
```

---

### 🐼 Pandas
```python
import pandas as pd

# Creating DataFrames
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 92, 78],
    'Grade': ['B', 'A', 'C']
}
df = pd.DataFrame(data)

# Basic Operations
print(df.describe())
print(df[df['Score'] > 80])
df['Pass'] = df['Score'] >= 80

# GroupBy
print(df.groupby('Grade')['Score'].mean())

# Reading CSV
# df = pd.read_csv('data.csv')
```

---

### 📊 Matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 4))
plt.plot(x, y, color='steelblue', linewidth=2, label='sin(x)')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('sine_wave.png')
plt.show()
```

---

### 🌊 Seaborn
```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load built-in dataset
tips = sns.load_dataset('tips')

# Distribution plot
sns.histplot(tips['total_bill'], kde=True, color='coral')
plt.title('Total Bill Distribution')
plt.show()

# Correlation heatmap
sns.heatmap(tips.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
```

---

### 🤖 Scikit-learn
```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

---

### 🌐 Requests (API calls)
```python
import requests

# GET request
response = requests.get('https://api.github.com/users/YashKumawat-afk')

if response.status_code == 200:
    data = response.json()
    print(f"Username: {data['login']}")
    print(f"Public Repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
else:
    print(f"Error: {response.status_code}")

# POST request example (commented)
# payload = {'key': 'value'}
# r = requests.post('https://httpbin.org/post', json=payload)
```

---

### 🌶️ Flask (Mini Web App)
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Alice", "score": 92},
    {"id": 2, "name": "Bob", "score": 85},
]

@app.route('/')
def home():
    return "<h1>Python API is Running!</h1>"

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    return jsonify(student) if student else (jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
```

---

### 🗂️ OS & Sys
```python
import os
import sys

# Directory operations
print(os.getcwd())
os.makedirs('new_folder', exist_ok=True)
files = os.listdir('.')
print(files)

# Path utilities
path = os.path.join('folder', 'subfolder', 'file.txt')
print(os.path.exists(path))
print(os.path.basename(path))

# sys usage
print(sys.version)
print(sys.platform)
# sys.argv for command-line arguments
```

---

## ⚙️ How to Run

```bash
# Clone the repo
git clone https://github.com/YashKumawat-afk/python-everything-you-need-to-know.git
cd python-everything-you-need-to-know

# Install dependencies
pip install -r requirements.txt

# Run any script
python 05_libraries/numpy_basics.py
```

---

## 📋 requirements.txt

```
numpy
pandas
matplotlib
seaborn
scikit-learn
requests
flask
```

---

## 🔧 How to Push to GitHub

### First Time Setup
```bash
# 1. Initialize git (if not done)
git init

# 2. Add all files
git add .

# 3. Commit with message
git commit -m "Initial commit: Python everything you need to know"

# 4. Add remote origin
git remote add origin https://github.com/YashKumawat-afk/python-everything-you-need-to-know.git

# 5. Push to main branch
git push -u origin main
```

### Pushing Updates Later
```bash
git add .
git commit -m "Add: numpy and pandas implementations"
git push
```

### Useful Git Commands
```bash
git status          # See what's changed
git log --oneline   # View commit history
git branch          # List branches
git pull            # Get latest changes
```

---

## 🤝 Contributing

1. Fork this repo
2. Create a feature branch: `git checkout -b feature/add-pytorch`
3. Commit your changes: `git commit -m "Add PyTorch basics"`
4. Push to branch: `git push origin feature/add-pytorch`
5. Open a Pull Request

---

## 📌 Roadmap

- [ ] Add PyTorch / TensorFlow basics
- [ ] Add SQL with Python (sqlite3, SQLAlchemy)
- [ ] Add asyncio & concurrency
- [ ] Add regex module examples
- [ ] Add unit testing with `pytest`
- [ ] Add a Jupyter Notebook version

---

## 👤 Author

**Yash Kumawat**  
GitHub: [@YashKumawat-afk](https://github.com/YashKumawat-afk)

---

*Happy Coding! 🐍*
