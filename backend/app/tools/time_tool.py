from datetime import datetime


def get_current_time() -> str:
    return datetime.now().strftime("%I:%M %p")