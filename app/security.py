import bcrypt
from app.database import get_user_by_username

def encode_password(password: str) -> bytes:
    return password.encode("utf-8")

# I read that some database engines can cause unexpected issues when passing raw bytes
def decode_password(password: bytes) -> str:
    return password.decode("utf-8")


def hash_password(password: str) -> str:
    password_bytes = encode_password(password)
    salt = bcrypt.gensalt()

    password_hash = bcrypt.hashpw(password_bytes, salt)

    return decode_password(password_hash)


def authenticate_user(username: str, password: str) -> bool:
    """Verify a user's password against the stored password_hash.

    Args:
        username: Account username.
        password: Plaintext password input.

    Returns:
        True if authentication succeeds, otherwise False.
    """
    user: dict = get_user_by_username(username)
    if user is None: # I do this first to guard against timing attacks
        return False # username does not exist in the database
    
    password_bytes = encode_password(password)
    password_hash = encode_password(user["password_hash"])

    return bcrypt.checkpw(password_bytes, password_hash)


if __name__ == "__main__":
    from app.database import create_user, get_user_by_username, delete_user

    username = "test_username"
    password = "password"
    create_user(username, hash_password(password))

    user = get_user_by_username(username)
    print(user["password_hash"])

    # correct password test case
    print(authenticate_user("test_username", "password"))
 
    # wrong password test case
    print(authenticate_user("test_username", "wrong_password"))

    delete_user(username)