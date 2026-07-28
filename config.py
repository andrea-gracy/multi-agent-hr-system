# config.py

import os
from dotenv import load_dotenv
from crewai import LLM

# Load environment variables
load_dotenv()

# -----------------------------
# LLM Configuration
# -----------------------------

llm = LLM(
    model=os.getenv("HR_AGENT_MODEL"),       
    temperature=os.getenv("TEMPERATURE","0.2"),
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("BASE_URL")
)

# -----------------------------
# Application Configuration
# -----------------------------

APP_NAME = "HR Employee Support Crew"

VERBOSE = True

# -----------------------------
# Escalation Keywords
# -----------------------------

ESCALATION_KEYWORDS = """
    1. Harassment,
    2. Bullying,
    3. Discrimination,
    4. Data Privacy,
    5. Legal Issues,
    6. Threats,
    7. Abuse,
    8. Sexual harassment,
    9. Violence,
    10. Confidential matters,
    11. Workplace misconduct,
    12. Extremely urgent situations
"""

# -----------------------------
# Supported HR Categories
# -----------------------------

HR_CATEGORIES = """
    1. Leave,
    2. Payroll,
    3. Benefits,
    4. Internal Transfer,
    5. Grievance,
    6. General HR
"""
#--------------------
# Urgency
#--------------------
URGENCY = """
    1. Low
    2. Medium
    3. High
"""

#--------------------
# Sensitivity
#--------------------
SENSITIVITY = """
    1. Sensitive
    2. Not Sensitive
"""

#--------------------
# HR Contacts
#--------------------

HR_CONTACTS = {
    "Leave": {
        "name": "Ananya Sharma",
        "designation": "Leave & Attendance Specialist",
        "email": "leave.support@abccompany.com",
        "phone": "+91 98765 10001"
    },

    "Payroll": {
        "name": "Rahul Mehta",
        "designation": "Payroll Administrator",
        "email": "payroll.support@abccompany.com",
        "phone": "+91 98765 10002"
    },

    "Benefits": {
        "name": "Priya Nair",
        "designation": "Benefits & Compensation Specialist",
        "email": "benefits@abccompany.com",
        "phone": "+91 98765 10003"
    },

    "Internal Transfer": {
        "name": "Vikram Rao",
        "designation": "Talent Mobility Partner",
        "email": "internal.mobility@abccompany.com",
        "phone": "+91 98765 10004"
    },

    "Grievance": {
        "name": "Neha Kapoor",
        "designation": "Employee Relations Manager",
        "email": "employee.relations@abccompany.com",
        "phone": "+91 98765 10005"
    },

    "General HR": {
        "name": "Aisha Fernandes",
        "designation": "HR Business Partner",
        "email": "hr.support@abccompany.com",
        "phone": "+91 98765 10006"
    }
}