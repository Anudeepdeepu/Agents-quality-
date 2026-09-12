AI Agent Tool Calling Flow

User Question
     ↓
HumanMessage
     ↓
LLM understands the request
     ↓
LLM decides whether a tool is needed
     ↓
AIMessage contains tool_call
     ↓
tool name + args are generated
     ↓
Tool executes
     ↓
ToolMessage contains result
     ↓
Result goes back to LLM
     ↓
LLM creates final AIMessage
     ↓
User gets final answer