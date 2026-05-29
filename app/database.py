import sqlite3

DATABASE_PATH = "database/database.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def create_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        balance INTEGER NOT NULL DEFAULT 1000
    )
    """)
    connection.commit()
    connection.close()

    print("Database and users table created.")


def create_user(username: str, password_hash: str):
    """Creates a user, if username already exists
    retun sqlite.IntegrityError
    else return None
    """
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO users (username, password_hash)
        VALUES (?, ?)
        """, (username, password_hash))

        connection.commit()

        return True
    except sqlite3.IntegrityError:
        return False
    
    finally:
        connection.close()


def get_user_by_username(username: str):
    """Finds user in database by username
    returns user
    if not found returns None
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE username = ?
    """, (username,))

    user = cursor.fetchone()
    connection.close()

    return user


def execute_transfer(sender: str, sender_new_balance: int, reciver: str, reciver_new_balance: int) -> bool:
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE users
        SET balance = ?
        WHERE username = ?
        """, (sender_new_balance, sender))

        cursor.execute("""
        UPDATE users
        SET balance = ?
        WHERE username = ?
        """, (reciver_new_balance, reciver))

        connection.commit()
        return True

    except Exception:
        connection.rollback()
        return False

    finally:
        connection.close()


def delete_user(username: str):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    DELETE FROM users
    WHERE username = ?
    """, (username,))

    connection.commit()
    connection.close()

    print(f"User '{username}' deleted.")


if __name__ == "__main__":
    create_database()

    username = "test_username"
    password = "password"
    create_user(username, password)

    user = get_user_by_username(username)
    print(f"{user["id"]}: {user["username"]}")
    print(user["password_hash"])
    print(user["balance"])

    print(get_user_by_username("not_in_the_database"))

    delete_user(username)