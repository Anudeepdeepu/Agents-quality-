## Tool Calling

- Tools are Python functions created to perform specific actions, such as adding numbers, checking weather, calling an API, or searching a database.

- The LLM reads the user's request and decides:
  - Whether a tool is required
  - Which tool should be used
  - What arguments should be passed to the tool

- `bind_tools()` provides the LLM with the tools' names, descriptions, and argument schemas.

- The LLM does not normally execute the tool directly.

- The LLM returns an `AIMessage` containing `tool_calls`, which specifies the selected tool and its arguments.

- Python code, an agent executor, or LangGraph's `ToolNode` executes the selected tool.

- The result of the tool execution is stored in a `ToolMessage`.

- The `ToolMessage` is passed back to the LLM.

- Finally, the LLM uses the tool result to generate the final answer for the user.


### Tool-Calling Flow

User question  
↓  
LLM checks whether a tool is needed  
↓  
LLM selects the tool and prepares its arguments  
↓  
`AIMessage` containing `tool_calls` is generated  
↓  
Python / Agent Executor / `ToolNode` executes the tool  
↓  
Tool result is stored in a `ToolMessage`  
↓  
`ToolMessage` is passed back to the LLM  
↓  
LLM generates the final answer