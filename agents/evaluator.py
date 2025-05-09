from crewai import Agent

def evaluator_agent():
    return Agent(
        role="Evaluator",
        goal="Review and score candidate responses for clarity and accuracy",
        backstory="A fair evaluator with expertise in analyzing technical answers.",
        allow_delegation=False
    )
