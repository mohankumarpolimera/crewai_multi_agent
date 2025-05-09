from crewai import Crew
from agents.interviewer import interviewer_agent
from agents.evaluator import evaluator_agent
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

def create_crew(user_topic: str):
    interviewer = interviewer_agent()
    evaluator = evaluator_agent()

    crew = Crew(
        agents=[interviewer, evaluator],
        tasks=[
            {
                "agent": interviewer,
                "description": f"Ask a technical interview question about: {user_topic} and provide a mock candidate response.",
                "expected_output": f"A question and a detailed sample answer on: {user_topic}"
            },
            {
                "agent": evaluator,
                "description": f"Evaluate the candidate's answer on '{user_topic}' for accuracy and clarity.",
                "expected_output": "An evaluation summary with comments and a score from 1 to 10."
            }
        ],
        llm=llm,
        verbose=True
    )

    return crew, llm