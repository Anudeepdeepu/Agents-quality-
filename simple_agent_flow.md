An agent receives the user’s HumanMessage, uses the LLM to select a suitable tool, executes that tool, stores the result as a ToolMessage, and uses the LLM again to generate the final AIMessage.


User question
     ↓
HumanMessage
     ↓
Agent receives the message
     ↓
LLM understands the question
     ↓
LLM decides to use the add tool
     ↓
AIMessage contains a tool request
     ↓
Agent executes the add tool
     ↓
ToolMessage contains the result
     ↓
LLM reads the tool result
     ↓
Final AIMessage is generated
     ↓
Final answer is returned to the user



HumanMessage → AIMessage (tool request) → ToolMessage → AIMessage (final answer)

Example question: "What is 2 + 2?"

HumanMessage: Stores the user’s question, for example, HumanMessage(content="What is 2 + 2?").
First AIMessage: The LLM decides which tool to use and requests add(a=2, b=2).
ToolMessage: Stores the result returned by the add tool, for example, ToolMessage(content="4").
Final AIMessage: Uses the tool result to provide the final answer to the user, for example, AIMessage(content="The answer is 4").