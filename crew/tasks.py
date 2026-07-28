# crew/tasks.py

from crewai import Task
from policies.hr_policies import COMPANY_POLICIES
from config import HR_CATEGORIES, URGENCY, SENSITIVITY, ESCALATION_KEYWORDS,HR_CONTACTS


class HRTasks:

    def classify_query(self, agent, employee_query):
        """
        returns: a Task that
        1. Analyze employee query
        2. Identify Employee Intent
        3. Determine Urgency
        4. Determine Sensitivity
        5. Identify any missing information
        """
        return Task(
            name="Query Classification Task",
            description=f"""
You are given the following employee query:

"{employee_query}"

Analyze the query and identify:

1. HR Category:
   {HR_CATEGORIES}

2. Employee Intent

3. Urgency:
   {URGENCY}

4. Sensitivity:
   {SENSITIVITY}

5. Any missing information required.

Return the output in the following format:

Category:
Intent:
Urgency:
Sensitivity:
Missing Information:
            """,

            expected_output="""
A structured summary containing:
- Category
- Intent
- Urgency
- Sensitivity
- Missing Information
            """,

            agent=agent
        )

    def policy_reasoning(self, agent, classification_task):
        """
        returns: Task that
        Based on the hr category classification and using the prescribed HR policies
        1. Determine the appropriate HR policy that applies
        2. Use Common HR practices for the category
        3. Provide:
            a. Applicable Policy
            b. Employee Eligibility
            c. Explanantion
            d. Recommended next steps
        """
        return Task(
            name="Policy Reasoning Task",
            description=f"""
Based on the classification below:

{classification_task}

Use ONLY the following HR policies.

{COMPANY_POLICIES}

Determine the appropriate HR policy that applies.

Use common HR practices for:

{HR_CATEGORIES}

Provide:

1. Applicable Policy
2. Employee Eligibility (if applicable)
3. Explanation
4. Recommended Next Step
            """,

            expected_output="""
Applicable Policy:
Eligibility:
Explanation:
Recommended Next Step:
            """,

            agent=agent,

            context=[classification_task]
        )

    def escalation_decision(self, agent, classification_task, policy_task):
        """
        return : a Task that
        reviews the employee case and determines whether it requires Human HR intervention
        """
        return Task(
            name="Escalation Task",
            description=f"""
Review the employee case and determine whether it requires
Human HR intervention.

Escalate if the query involves:

{ESCALATION_KEYWORDS}

Otherwise, recommend automated resolution.

Provide:

1. Escalation Required (Yes/No)

2. Priority
   {URGENCY}

3. Reason
            """,

            expected_output="""
Escalation Required:
Priority:
Reason:
            """,

            agent=agent,

            context=[
                classification_task,
                policy_task
            ]
        )

    def generate_response(
    self,
    agent,
    classification_task,
    policy_task,
    escalation_task
):
        """
        return: Task that generates response for the employee
        The generated response has the corresponding HR contact details embedded
        """
        return Task(
            name="Response Generation Task",
            description=f"""
You are the Response Generation Agent.

You will receive:

1. Query Classification
2. HR Policy Reasoning
3. Escalation Decision

The Query Classification output contains the HR Category.

Available HR Contacts:

{HR_CONTACTS}

Instructions:

1. Read the HR Category from the Query Classification output.

2. Select the matching HR contact from the list above.

3. If no category matches, use the "General HR" contact.

4. Generate a professional response.

5. If escalation is NOT required:
   - Explain the applicable policy.
   - Explain next steps.

6. If escalation IS required:
   - Acknowledge the concern.
   - Inform the employee that HR will contact them.
   - Maintain confidentiality.

7. End the response with ONLY the selected HR contact.

Example:

For Further Assistance, please contact

Name:
Designation:
Email:
Phone:

Do not invent contact information.
Only use the contacts provided above.

Do not use placeholders such as
[Your Name]
[Company Name]
[Employee Name].

If the employee name is unknown, begin with:

Dear Employee,

""",

        expected_output="""
A professional employee response including the correct HR contact.
""",

        agent=agent,

        context=[
            classification_task,
            policy_task,
            escalation_task
        ]
    )
