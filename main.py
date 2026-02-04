import ollama
import json
from tools import calculator_tools
from tools import execute_calculator_function


def get_function_call(user_question: str, available_functions: list[dict]):
    tool_descriptions = "\n".join(
        [f"- {tool['name']}: {tool['description']}" for tool in available_functions]
    )

    prompt = f"""You are a calculator assistant. You have access to these functions:
{tool_descriptions}

When the user asks a math question, respond with ONLY a JSON object specifying which function to call:

Example:
User: What is 15 + 27?
Response: {{"name": "add", "arguments": {{"a": "15", "b": "27"}}}}

User: Calculate 100 divided by 4
Response: {{"name": "divide", "arguments": {{"a": "100", "b": "4"}}}}

Now answer this:
User: {user_question}
Response:

"""
    response = ollama.chat(
        model="qwen2.5:7b", messages=[{"role": "user", "content": prompt}]
    )

    try:
        function_call = json.loads(response["message"]["content"])
        return function_call
    except json.JSONDecodeError:
        raise Exception(f"Failed to parse function call: {response}")


def main():
    while True:
        user_input = input("Enter your question (or 'quit' to exit): ")
        if user_input.lower() == "quit":
            break

        print("thinking....")

        function_call = get_function_call(user_input, calculator_tools)
        print(f"function call {function_call}")

        result = execute_calculator_function(
            function_call["name"], function_call["arguments"]
        )

        print(f"results: {result}")


if __name__ == "__main__":
    main()
