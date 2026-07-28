# utils/helper.py

import re


def clean_text(text: str) -> str:
    """
    Normalize employee query text.
    This function cleans and normalizes an employee's query before it is processed by the 
    HR support system. 
    Cleaning text ensures that extra spaces or formatting inconsistencies don't affect 
    later steps such as classification or policy reasoning.
    """
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def contains_keywords(text: str, keywords: list) -> bool:
    """
    Check if any keyword exists in the text.
    """
    text = text.lower()

    return any(keyword.lower() in text for keyword in keywords)


def get_priority(urgency: str) -> str:
    """
    Map urgency to priority.
    """
    urgency = urgency.lower()

    mapping = {
        "low": "Low",
        "medium": "Medium",
        "high": "High"
    }

    return mapping.get(urgency, "Medium")


def print_header(title: str):
    """
    Print a formatted console header.
    """
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def print_section(title: str):
    """
    Print a section divider.
    """
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)