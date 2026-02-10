users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]

def calculate_average_age(users_list):
    """Calculate the average age of users in the list, ignoring non-integer ages.

    Parameters:
    ----------
    users_list : list
        A list of user dictionaries, each containing an 'age' key.

    Returns:
    -------
    float
        The average age of the users, or 0.0 if there are no valid ages.
    """
    total_age = 0
    user_count_for_age = 0
    for user in users_list:
        if isinstance(user.get("age"), int):
            total_age += user["age"]
            user_count_for_age += 1
    if user_count_for_age == 0:
        return 0.0
    return total_age / user_count_for_age


average_age = calculate_average_age(users)
print(f"average user age: {average_age:.2f}")

def get_active_user_emails(users_list):
    """Return emails for users that are active and have an email."""
    return [
        user["email"]
        for user in users_list
        if user.get("is_active") and user.get("email")
    ]


active_user_emails = get_active_user_emails(users)
print(f"active user emails: {active_user_emails}")
