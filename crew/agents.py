#crew/agents.py

from crewai import Agent
from config import llm

class HRAgents:

    def query_classifier(self):
        """
        returns: Query Classification Agent that 
        Classifies the query as one of the HR categories
        """
        return Agent(
            role="Query Classification Agent",
            goal="Classify employee queries into HR categories.",
            backstory="Expert at identifying employee intent, urgency and sensitivity.",
            verbose=True,
            llm=llm
        )

    def policy_reasoner(self):
        """
        returns: HR Policy Reasoning Agent that 
        Applies HR policies to determine eligibility and next steps.
        """
        return Agent(
            role="HR Policy Reasoning Agent",
            goal="Apply HR policies to determine eligibility and next steps.",
            backstory="Experienced HR policy specialist.",
            verbose=True,
            llm=llm
        )

    def escalation_agent(self):
        """
        returns: Human HR escalation Agent that
        Determines if a human HR representative should handle the case.
        """
        return Agent(
            role="Human HR Escalation Agent",
            goal="Determine if a human HR representative should handle the case.",
            backstory="Ensures compliance and confidentiality.",
            verbose=True,
            llm=llm
        )

    def response_generator(self):
        """
        returns: Response Generation Agent that
        Generates a professional response for the employee..
        """
        return Agent(
            role="Response Generation Agent",
            goal="Generate a professional response for the employee.",
            backstory="Creates clear and empathetic HR responses.",
            verbose=True,
            llm=llm
        )