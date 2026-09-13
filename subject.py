from db import get_db_connection


def create_subject(data):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
                INSERT INTO subjects (name, code)
                VALUES (%s, %s)
                """

        values = (data['name'], data['code'])

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


def get_all_subjects():
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
                SELECT id, name, code
                FROM subjects
                """

        cursor.execute(query)

        subjects = cursor.fetchall()

        return subjects

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_subject_by_id(subject_id):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
                SELECT id, name, code
                FROM subjects
                WHERE id = %s
                """

        cursor.execute(query, (subject_id,))

        subject = cursor.fetchone()

        return subject

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def update_subject(subject_id, data):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
                UPDATE subjects
                SET name = %s, code = %s
                WHERE id = %s
                """

        values = (data['name'], data['code'], subject_id)

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


def delete_subject(subject_id):
    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
                DELETE FROM subjects
                WHERE id = %s
                """

        cursor.execute(query, (subject_id,))
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
