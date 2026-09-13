from db import get_db_connection


def create_student(data):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
                INSERT INTO students (name, roll_no, email, branch)
                VALUES (%s, %s, %s, %s)
                """

        values = (
            data['name'],
            data['roll_no'],
            data['email'],
            data['branch']
        )

        cursor.execute(query, values)
        conn.commit()

        return True

    except Exception as e:
        print(e)
        return False

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_all_students():
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
                SELECT id, name, roll_no, email, branch
                FROM students
                """

        cursor.execute(query)

        students = cursor.fetchall()

        return students

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_student_by_id(student_id):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
                SELECT id, name, roll_no, email, branch
                FROM students
                WHERE id = %s
                """

        cursor.execute(query, (student_id,))

        student = cursor.fetchone()

        return student

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def update_student(student_id, data):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
                UPDATE students
                SET name = %s,
                    roll_no = %s,
                    email = %s,
                    branch = %s
                WHERE id = %s
                """

        values = (
            data['name'],
            data['roll_no'],
            data['email'],
            data['branch'],
            student_id
        )

        cursor.execute(query, values)
        conn.commit()

        return cursor.rowcount > 0

    except Exception as e:
        print(e)
        return False

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def delete_student(student_id):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
                DELETE FROM students
                WHERE id = %s
                """

        cursor.execute(query, (student_id,))
        conn.commit()

        return cursor.rowcount > 0

    except Exception as e:
        print(e)
        return False

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def search_students(keyword):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
                SELECT id, name, roll_no, email, branch
                FROM students
                WHERE name LIKE %s
                   OR roll_no LIKE %s
                   OR email LIKE %s
                """

        search_value = "%" + keyword + "%"

        cursor.execute(
            query,
            (search_value, search_value, search_value)
        )

        students = cursor.fetchall()

        return students

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
