# crew/crew.py

from crewai import Crew, Process
from crew.agents import HRAgents
from crew.tasks import HRTasks


class HRCrew:

    def build(self, employee_query):

        # Initialize helper classes
        agents = HRAgents()
        tasks = HRTasks()

        # -------------------------
        # Create Agents
        # -------------------------

        query_classifier = agents.query_classifier()

        policy_reasoner = agents.policy_reasoner()

        escalation_agent = agents.escalation_agent()

        response_generator = agents.response_generator()

        # -------------------------
        # Create Tasks
        # -------------------------

        classification_task = tasks.classify_query(
            query_classifier,
            employee_query
        )

        policy_task = tasks.policy_reasoning(
            policy_reasoner,
            classification_task
        )

        escalation_task = tasks.escalation_decision(
            escalation_agent,
            classification_task,
            policy_task
        )

        response_task = tasks.generate_response(
            response_generator,
            classification_task,
            policy_task,
            escalation_task
        )

        # -------------------------
        # Build Crew
        # -------------------------

        crew = Crew(
            agents=[
                query_classifier,
                policy_reasoner,
                escalation_agent,
                response_generator
            ],

            tasks=[
                classification_task,
                policy_task,
                escalation_task,
                response_task
            ],

            process=Process.sequential,

            verbose=True
        )

        return crew