def send_messages(messages, sent_messages):
    """Print each message and move it to new list."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ['hello!', 'goodbye!', 'how are you?', 'have a nice day!', 'thank you!']
sent_messages = []
send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)