users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]


def calculate_average_age(user_list):
    """
    Calculate the average age of users in a list.

    Parameters
    ----------
    user_list : list of dict
        A list of user dictionaries, where each dictionary may contain an 'age' key.

    Returns
    -------
    float
        The average age of users with valid integer ages. Returns 0.0 if the
        list is empty or no valid ages are found.
    """
    try:
        total_age = 0
        count = 0
        for user in user_list:
            age = user.get("age")
            if isinstance(age, int):
                total_age += age
                count += 1

        if count == 0:
            raise ZeroDivisionError("No valid integer ages found.")

        return float(total_age / count)
    except ZeroDivisionError:
        print("error: cannot calculate average age of an empty list or no valid ages.")
        return 0.0
    except Exception as e:
        print(f"error: an unexpected error occurred: {e}")
        return 0.0


def get_active_user_emails(user_list):
    """
    Get a list of emails for all active users.

    Parameters
    ----------
    user_list : list of dict
        A list of user dictionaries, where each dictionary may contain
        'is_active' and 'email' keys.

    Returns
    -------
    list of str
        A list of email addresses for active users who have an email provided.
    """
    try:
        active_emails = []
        for user in user_list:
            # Using get() to handle missing keys gracefully, as suggested by instructions
            is_active = user.get("is_active", False)
            email = user.get("email")
            if is_active and email:
                active_emails.append(email)
        return active_emails
    except Exception as e:
        print(f"error: failed to get active user emails: {e}")
        return []


if __name__ == '__main__':
    # Call your functions and print results
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")
