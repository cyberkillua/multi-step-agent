import ollama
import json
from tools import calculator_tools
from tools import execute_calculator_function
from groq import Groq
import os

api_key = os.environ.get("GROQ_API_KEY")

client = Groq(api_key=api_key)


def get_function_call(
    user_question: str, available_functions: list[dict], history: list
):
    tool_descriptions = "\n".join(
        [f"- {tool['name']}: {tool['description']}" for tool in available_functions]
    )
    history_text = (
        "\n".join([f"- {h['name']}({h['args']}) = {h['result']}" for h in history])
        if history
        else "None yet"
    )

    prompt = f"""You are a multi step calculator assistant. You have access to these functions:
{tool_descriptions}

Here is the history of the functions you have called already:
{history_text}

When the user asks a math question, respond with ONLY a JSON object specifying which function to call:

IMPORTANT: Look at the history. If you have already computed the answer to the user's question, call the done function immediately with that answer. Do NOT repeat calculations.
Example:
User: What is 15 + 27?
Response: {{"name": "add", "arguments": {{"a": "15", "b": "27"}}}}

User: Calculate 100 divided by 4
Response: {{"name": "divide", "arguments": {{"a": "100", "b": "4"}}}}

When you have computed the final answer, call the done function:
Response: {{"name": "done", "arguments": {{"answer": "42"}}}}

Now answer this:
User: {user_question}
Response:

"""
    # response = ollama.chat(
    #     model="qwen2.5:7b", messages=[{"role": "user", "content": prompt}]
    # )

    response = client.chat.completions.create(
        model="moonshotai/kimi-k2-instruct",
        messages=[
            {
                "role": "system",
                "content": "You are a calculator assistant that responds only with JSON.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=256,
        temperature=0,
    )

    try:
        function_call = json.loads(response.choices[0].message.content)
        return function_call
    except json.JSONDecodeError:
        raise Exception(f"Failed to parse function call: {response}")


def main():
    user_input = input("Enter expression: ")
    history = []
    max_iterations = 10

    for i in range(max_iterations):
        if user_input.lower() == "quit":
            break
        print("thinking....")

        # call LLM with user_input + history
        function_call = get_function_call(user_input, calculator_tools, history)
        print(f"function call {function_call}")

        # execute the function
        result = execute_calculator_function(
            function_call["name"], function_call["arguments"]
        )
        if function_call["name"] == "done":
            print(f"Final answer: {result}")
            break

        # else, add result to history
        history.append(
            {
                "name": function_call["name"],
                "args": function_call["arguments"],
                "result": result,
            }
        )
        print(f"Step {i + 1}: {function_call['name']} = {result}")


if __name__ == "__main__":
    main()
