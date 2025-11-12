from config.bd import create_connection

def login_user(email, password):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO garcons (email, password) VALUES (%s, %s)", (email, password))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
        cursor.close()


def login_admin(email, password):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO admin (email, password) VALUES (%s, %s)", (email, password))
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()
        cursor.close()
