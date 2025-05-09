from crewai import Agent

def interviewer_agent():
    return Agent(
        role="Interviewer",
        goal="Conduct mock interviews on technical topics",
        backstory="An experienced technical interviewer specializing in assessing skills.",
        allow_delegation=False
    )
