prompt = "Tell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True #Active state
while active: #Will continue running as long as True
    message = input(prompt)

    if message == 'quit': #Activates False
        active = False
    else:
        print(message)