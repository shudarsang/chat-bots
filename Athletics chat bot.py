from openai import OpenAI

client = OpenAI(api_key="")

system_message = """
You are a friendly chatbot for Athletics, a website that organizes sports events.
Your job is to assist users in enrolling in sports events.

Start by asking:
1. Which sport would you like to enroll in?
2. What is your preferred location or city?

After that, follow up with questions like:
- Age group?
- Are you registering as an individual or team?
- Preferred date or time?
- Any previous experience in this sport?

Keep responses clear and engaging. Always guide the user step-by-step through the enrollment.
"""


def get_chatbot_reply(conversation_history):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        temperature=0.2
    )
    return response.choices[0].message.content.strip()


def main():
    print(" Welcome to Athletics – Sports Event Enrollment Assistant!")
    print("Type 'exit' anytime to quit.\n")

    messages = [{"role": "system", "content": system_message}]

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thanks for using Athletics. See you on the field! 🏆")
            break

        messages.append({"role": "user", "content": user_input})

        # Get bot's reply
        try:
            bot_reply = get_chatbot_reply(messages)
            messages.append({"role": "assistant", "content": bot_reply})
            print("Bot:", bot_reply)
        except Exception as e:
            print(" Error:", str(e))
            break


if __name__ == "__main__":
    main()