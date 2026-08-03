from app.tools.date_tool import get_current_date
from app.tools.time_tool import get_current_time
from app.tools.random_tool import get_random_number
from app.tools.email_tool import send_email
from app.tools.jira_tool import create_jira_ticket
TOOLS = {
    "date_tool": {
        "function": get_current_date,
        "description": "Returns today's date.",
        "requires_approval": False,
        "accepts_input": False,
    },

    "time_tool": {
        "function": get_current_time,
        "description": "Returns current system time.",
        "requires_approval": False,
        "accepts_input": False,
    },

    "random_tool": {
        "function": get_random_number,
        "description": "Generates a random number.",
        "requires_approval": False,
        "accepts_input": False,
    },
    "email_tool": {
            "function": send_email,
            "description": "Sends an email.",
            "requires_approval": True,
            "accepts_input": True,
        },
    "jira_tool": {
                "function": create_jira_ticket,
                "description": "Creates a Jira ticket.",
                "requires_approval": True,
                "accepts_input": True,
            },
}