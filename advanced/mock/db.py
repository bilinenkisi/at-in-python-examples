
def get_db_connection():
    return False

def fetch_data_from_db():
    # Gerçekte DB'ye bağlanır
    if not get_db_connection():
        raise ValueError("db is not connected")
    # Select first_name,last_credit_date, last_payment_due, have_already_debt,mentioned_salary,detected_salary from users
    return ["Alice", "Bob"]