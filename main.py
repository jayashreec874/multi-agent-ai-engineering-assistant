
from agents.planner import PlannerAgent


def main():

    planner = PlannerAgent()

    user_task = "Explain object oriented programming"

    print("Agent:", planner.name)
    print("\nUser Request:", user_task)

    plan = planner.create_plan(user_task)

    print("\nGenerated Plan:")

    for index, step in enumerate(plan, start=1):
        print(f"{index}. {step}")


if __name__ == "__main__":
    main()