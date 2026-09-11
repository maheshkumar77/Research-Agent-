from agent import agent


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }
    )

    print("Agent:", result["messages"][-1].content)