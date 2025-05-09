from crew import create_crew
from crewai import Task, Crew

if __name__ == "__main__":
    topic = input("🎯 Enter a topic for the mock interview: ")
    print("\n🚀 Starting Real-Time Interview...\n")

    crew, llm = create_crew(topic)
    interviewer = crew.agents[0]
    evaluator = crew.agents[1]

    context = ""
    round_num = 1

    while True:
        # Step 1: Interviewer generates question based on context
        if round_num == 1:
            prompt = f"Start the interview by asking a technical question about: {topic}."
        else:
            prompt = (
                f"Based on this conversation so far:\n\n{context}\n\n"
                f"Ask a meaningful follow-up technical question on the same topic."
            )

        question_task = Task(
            agent=interviewer,
            description=prompt,
            expected_output="A clear, challenging technical question."
        )
        question_crew = Crew(
            agents=[interviewer],
            tasks=[question_task],
            llm=llm,
            verbose=False
        )
        question = question_crew.kickoff()
        print(f"\n🧑‍💻 Round {round_num} - Interview Question:\n{question}")

        # Step 2: User answers
        user_answer = input("\n🧑 Your Answer (type 'exit' to stop): ")
        if user_answer.strip().lower() == "exit":
            print("\n🛑 Interview session ended.")
            break

        # Step 3: Evaluator reviews answer
        eval_prompt = (
            f"Evaluate the candidate's answer below for the question:\n\n"
            f"Question: {question}\nAnswer: {user_answer}"
        )
        eval_task = Task(
            agent=evaluator,
            description=eval_prompt,
            expected_output="Feedback with a score out of 10."
        )
        eval_crew = Crew(
            agents=[evaluator],
            tasks=[eval_task],
            llm=llm,
            verbose=True
        )
        feedback = eval_crew.kickoff()
        print(f"\n📊 Evaluator Feedback:\n{feedback}")

        # Step 4: Update conversation context for next question
        context += f"\nRound {round_num}:\nQuestion: {question}\nAnswer: {user_answer}\nFeedback: {feedback}\n"
        round_num += 1
