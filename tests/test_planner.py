
import unittest

from agents.planner import PlannerAgent


class TestPlannerAgent(unittest.TestCase):

    def setUp(self):
        self.planner = PlannerAgent()

    def test_code_generation_plan(self):
        plan = self.planner.create_plan(
            "Create a Python program"
        )

        self.assertIn(
            "Generate the required code.",
            plan
        )

    def test_debugging_plan(self):
        plan = self.planner.create_plan(
            "Debug an error in Python"
        )

        self.assertIn(
            "Identify the possible cause of the error.",
            plan
        )

    def test_general_request(self):
        plan = self.planner.create_plan(
            "Explain object oriented programming"
        )

        self.assertIn(
            "Understand the user's request.",
            plan
        )

    def test_empty_task(self):
        with self.assertRaises(ValueError):
            self.planner.create_plan("")


if __name__ == "__main__":
    unittest.main()
