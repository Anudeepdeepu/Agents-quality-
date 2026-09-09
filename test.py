
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import  ChatGoogleGenerativeAI
from dotenv import load_dotenv

import os

load_dotenv()

project =os.getenv("GOOGLE_CLOUD_PROJECT")

#model

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",
                             vertexai=True,
                             project=project

            )


country = input("Enter country name: ")


# lets create array called messages to hold the messages we want to send to the model.
messages = [
    SystemMessage("you are a social teacher of the primary school,explain intresting facts"),
    HumanMessage(f"what is the capital of {country}?")
]
#result = llm.invoke(f"what is the capital of {country}?")
result = llm.invoke(messages)


print (type(result))
print (result)
print(result.content)

