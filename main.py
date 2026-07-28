import asyncio
from crew.crew import HRCrew
from data.sample_queries import SAMPLE_QUERIES
from utils.helper import (
    print_header,
    clean_text,
    contains_keywords,
    get_priority
)


async def process_employee_query(employee_query):
    """
    This function takes an employee's question, 
    coordinates the required processing steps, '
    and returns the most appropriate response or escalation.
    """

    employee_query = clean_text(employee_query)

    # Demo logging only
    if contains_keywords(
        employee_query,
        ["harassment", "bullying", "privacy", "discrimination"]
    ):
        print("\nSensitive query detected.")
        print(f"Suggested Priority: {get_priority('high')}")

    crew = HRCrew().build(employee_query)
    result = await crew.kickoff_async()

    print("\n" + "=" * 80)
    print("Employee Query")
    print("=" * 80)
    print(employee_query)

    print("\n" + "-" * 80)
    print("Response")
    print("-" * 80)
    print(result)

    print("=" * 80)

async def main():

    print_header("HR Employee Support System")

    for query in SAMPLE_QUERIES:
        await process_employee_query(query)

#This is a common Python pattern used to make a script executable while also allowing it to be imported as a module without running the main code automatically.

if __name__ == "__main__":
    asyncio.run(main())