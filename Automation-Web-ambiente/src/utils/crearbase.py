import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect('basedebromas.db')
c = conn.cursor()

# Eliminar la tabla existente (si existe)
c.execute('DROP TABLE IF EXISTS bromas')

# Crear la tabla con la estructura correcta
c.execute('''
    CREATE TABLE IF NOT EXISTS bromas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        broma TEXT NOT NULL
    )
''')
conn.commit()

def bromaguardada(broma):
    c.execute('INSERT INTO bromas (broma) VALUES (?)', (broma,))
    conn.commit()

def obtener_bromas():
    c.execute('SELECT * FROM bromas')
    return c.fetchall()

def cerrarconexionbase():
    conn.close()
