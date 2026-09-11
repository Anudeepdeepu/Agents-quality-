
Ask a Question, Invoke the AI Agent, and Return Its Final Response

from langchain_core.messages import HumanMessage, BaseMessage


def ask_question_to_agent(
    question: str,
    verbose: bool = True
) -> BaseMessage:

    messages = [HumanMessage(question)]

    response = agent.invoke({
        "messages": messages
    })

    if verbose:
        print(response["messages"])
        print(len(response["messages"]))

    return response["messages"][-1]


question = """
I have purchased a mobile phone for 100000 rupees.
I got a 15% discount. What will I end up paying?
"""


reply = ask_question_to_agent(question=question)