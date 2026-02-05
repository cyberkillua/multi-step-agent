calculator_tools = [
    {
        "name": "add",
        "description": "Add two numbers together",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"},
            },
            "required": ["a", "b"],
        },
    },
    {
        "name": "subtract",
        "description": "Subtract second number from first",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number to subtract"},
            },
            "required": ["a", "b"],
        },
    },
    {
        "name": "multiply",
        "description": "Multiply two numbers",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "First number"},
                "b": {"type": "number", "description": "Second number"},
            },
            "required": ["a", "b"],
        },
    },
    {
        "name": "divide",
        "description": "Divide first number by second",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "Numerator"},
                "b": {"type": "number", "description": "Denominator"},
            },
            "required": ["a", "b"],
        },
    },
    {
        "name": "done",
        "description": "Call this when you have the final answer",
        "parameters": {"answer": "number"},
    },
]


def execute_calculator_function(name: str, args: dict):
    if name == "add":
        return float(args["a"]) + float(args["b"])
    elif name == "subtract":
        return float(args["a"]) - float(args["b"])
    elif name == "multiply":
        return float(args["a"]) * float(args["b"])
    elif name == "divide":
        return float(args["a"]) / float(args["b"])
    elif name == "done":
        return float(args["answer"])
    else:
        return "Unknown function"
