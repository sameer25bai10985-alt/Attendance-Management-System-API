from db import get_db_connection

def mark_attendance(data):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO attendance
            (student_id, subject_id, attendance_date, status)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            data["student_id"],
            data["subject_id"],
            data["attendance_date"],
            data["status"]
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


def get_attendance_by_student(student_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT *
            FROM attendance
            WHERE student_id = %s
            ORDER BY attendance_date
        """

        cursor.execute(query, (student_id,))
        records = cursor.fetchall()
        return records

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def get_attendance_by_date(attendance_date):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT *
            FROM attendance
            WHERE attendance_date = %s
        """

        cursor.execute(query, (attendance_date,))
        records = cursor.fetchall()
        return records

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_attendance_percentage_overall(student_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT
                COUNT(*) AS total,
                SUM(CASE WHEN status = 'present' THEN 1 ELSE 0 END) AS present_count
            FROM attendance
            WHERE student_id = %s
        """

        cursor.execute(query, (student_id,))
        result = cursor.fetchone()

        if result["total"] == 0:
            return None

        percentage = (result["present_count"] / result["total"]) * 100
        return round(percentage, 2)

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_attendance_percentage_subject(student_id, subject_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT
                COUNT(*) AS total,
                SUM(CASE WHEN status = 'present' THEN 1 ELSE 0 END) AS present_count
            FROM attendance
            WHERE student_id = %s AND subject_id = %s
        """

        cursor.execute(query, (student_id, subject_id))
        result = cursor.fetchone()

        if result["total"] == 0:
            return None

        percentage = (result["present_count"] / result["total"]) * 100
        return round(percentage, 2)

    except Exception as e:
        print(e)
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
