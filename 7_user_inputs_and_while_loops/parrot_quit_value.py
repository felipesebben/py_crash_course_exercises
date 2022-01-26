#This program lets the user choose when to quit:
prompt = "\nTell me something, and I will repeat it back to you: " #two options are given in this prompt
prompt += "\nEnter 'quit' to end the program. "

message = '' #keeps track of what value the user enters; empty string makes sense to Python
while message != 'quit': #While loop runs as long as 'quit' is not mentioned
    message = input(prompt)
    #add an if test to avoid printing 'quit':
    if message != 'quit':
        print(message)