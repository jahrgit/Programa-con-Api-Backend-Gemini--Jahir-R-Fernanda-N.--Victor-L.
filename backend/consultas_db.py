from backend.database import get_connection

def obtener_propietarios():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM propietarios;")
    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    return datos


def obtener_datos_completos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.nombre,
            p.apellido,
            p.telefono,
            p.correo,
            p.direccion,
            m.nombre AS mascota,
            m.especie,
            m.raza,
            m.edad,
            m.sexo,
            c.fecha,
            c.motivo,
            c.diagnostico,
            c.tratamiento,
            c.costo
        FROM propietarios p
        JOIN mascotas m ON p.id_propietario = m.id_propietario
        JOIN consultas c ON m.id_mascota = c.id_mascota;
    """)

    datos = cursor.fetchall()

    cursor.close()
    conn.close()

    return datos