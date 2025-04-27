class User:
    def __init__(self, user_id, is_premium=False):
        self.user_id = user_id
        self.is_premium = is_premium

def check_premium_access(user: User):
    if not user.is_premium:
        return {"error": "This feature is available to premium users only. Upgrade to access."}
    return None
