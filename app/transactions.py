from app.database import get_user_by_username, execute_transfer

def transfer(sender: str, reciver: str, quantity: int) -> bool:
    """The function transfers a quantity from sender to reciver.
    Checks if sender has funds for transactions.
    
    Args:
        sender: The username of the user who will lose the funds.
        reciver: The username of the user who will gain the funds.
        quantity: A non-zero, non-negative value.
        
    Returns:
        True if transaction was successful, otherwise False
        """

    if quantity <= 0:
        return False
    
    sender_acc = get_user_by_username(sender)
    reciver_acc = get_user_by_username(reciver)
    if sender_acc is None:
        return False
    if reciver_acc is None:
        return False

    sender_balance = sender_acc["balance"]
    if quantity > sender_balance:
        return False
    
    reciver_balance = reciver_acc["balance"]

    sender_balance -= quantity
    reciver_balance += quantity

    return execute_transfer(sender_acc["username"], sender_balance, reciver_acc["username"], reciver_balance)
    
if __name__ == "__main__":
    from app.database import create_user, delete_user
    from app.security import hash_password
    create_user("user1", hash_password("password"))
    create_user("user2", hash_password("password"))

    transfer_status = transfer("user1", "user2", 200)
    if transfer_status:
        print("Transfer was successful")
    else:
        print("Error with transfer")

    delete_user("user1")
    delete_user("user2")