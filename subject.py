from db import get_db_connection
def create_subject(data):

    try:
       conn=get_db_connection()
       cursor=conn.cursor()

       query ="""
               INSERT INTO subjects (name,code) VALUES (%s,%s);
               """
       values=(data['name'],data['code'])
       cursor.execute(query,values)
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
    try:
        conn=get_db_connection()
        cursor=conn.cursor(dictionary=True)

        query ="""
                SELECT id,name,code FROM subjects;
               """
        cursor.execute(query)

        subjects=cursor.fetchall()
        return subjects
    except Exception as e:
        print(e)
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
