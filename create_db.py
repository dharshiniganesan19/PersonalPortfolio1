import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS projects(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT
)
''')

cursor.execute("""
INSERT INTO projects(title,description)
VALUES(
'Titanic Survival Prediction',
'Machine Learning model for predicting passenger survival.'
)
""")

cursor.execute("""
INSERT INTO projects(title,description)
VALUES(
'Neonatal Health Predictor',
'Machine Learning system for neonatal health prediction.'
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")