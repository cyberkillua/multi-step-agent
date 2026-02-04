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
]


def execute_calculator_function(name: str, args: dict):
    a = float(args["a"])
    b = float(args["b"])

    if name == "add":
        return a + b
    elif name == "subtract":
        return a - b
    elif name == "multiply":
        return a * b
    elif name == "divide":
        return a / b
    else:
        return "Unknown function"
