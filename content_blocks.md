for block in response_with_tools.content_blocks:
    if block['type']=='tool_call':
        if block ['name']=='multiply':
            result = multiply.invoke(block['args'])


            for the above what is happening

            LLM response
    ↓
content_blocks is a LIST
    ↓
for loop takes one item
    ↓
stores that item in "block"
    ↓
block is a DICTIONARY
    ↓
block['type']
    ↓
"tool_call"
    ↓
Is it a tool call?
YES
    ↓
block['name']
    ↓
"multiply"
    ↓
Does LLM want multiply?
YES
    ↓
block['args']
    ↓
{'a': 100000, 'b': 0.03}
    ↓
multiply.invoke(...)
    ↓
a = 100000
b = 0.03
    ↓
a * b
    ↓
3000.0
    ↓
result = 3000.0