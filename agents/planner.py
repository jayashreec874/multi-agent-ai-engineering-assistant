
class PlannerAgent:

    def __init__(self):
        self.name = "Planner Agent"

    def create_plan(self, task):

        if not task or not task.strip():
            raise ValueError("Task cannot be empty.")

        task_lower = task.lower()

        # Check whether the user wants to debug code
        if any(word in task_lower for word in ["debug", "error", "bug", "fix"]):

            steps = [
                "Analyse the given code and error message.",
                "Identify the possible cause of the error.",
                "Suggest a suitable correction.",
                "Review the corrected code.",
                "Test the solution."
            ]

        # Check whether the user wants to generate code
        elif any(word in task_lower for word in [
            "write", "create", "build", "generate", "implement", "code"
        ]):

            steps = [
                "Understand the programming requirements.",
                "Design the solution logic.",
                "Generate the required code.",
                "Review the code for possible errors.",
                "Test the program with sample inputs."
            ]

        # Handle other types of requests
        else:

            steps = [
                "Understand the user's request.",
                "Identify the important requirements.",
                "Prepare a suitable solution.",
                "Review the result.",
                "Return the final response."
            ]

        return steps