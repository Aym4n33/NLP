import re


substitution = [
    (r".*my name is (\w+).*", r"Hello, \1! How can I assist you today?"),
    (r".*(love|like).*(games|gaming).*", r"What kind of video games do you enjoy?"),
    (r".*(survival games|FPS games).*", r"Do you have a favorite \1 you've played recently?"),
    (r".*suggest.*(survival game|FPS game).*", r"I'd recommend trying out RUST! It's a mix of FPS and survival."),
    (r".*feel.*(sad|down|upset).*", r"I'm sorry to hear that you're feeling \1. Would you like to talk more about it?"),
    (r".*I am (happy|excited|good).*", r"That's wonderful to hear! What made you feel so \1?"),
    (r".*can you (help|assist) me with.*", r"Of course, I'd be happy to help. What specifically do you need assistance with?"),
    (r".*tell me about yourself.*", r"I'm Eliza, your friendly chatbot. I’m here to chat and help!"),
    (r".*what do you think about.*", r"I'm just a chatbot, but I'm happy to share my perspective. What's your take on it?"),
    (r".*thank you.*", r"You're welcome! Is there anything else I can do for you?"),
    (r".*why.*", r"That's an interesting question. Why do you think so?"),
    (r".*what.*", r"Could you clarify your question? I'd love to help!"),
]

def eliza(user_input):
    for pattern, replacement in substitution:
        match = re.search(pattern, user_input, re.IGNORECASE)
        if match:
            return re.sub(pattern, replacement, user_input)
    return "I'm not sure I understand. Could you elaborate?"

# Eliza Chat
print("Eliza: Welcome to Eliza Chatbot! What's your name?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'goodbye']:
        print("Eliza: Bye! Take care!")
        break
    else:
        response = eliza(user_input.lower())
        print(f"Eliza: {response}")
