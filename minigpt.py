# Sv
#Task 1: Silly Chatbot

def minichatgpt():
    # Run the chatbot
    print("=== Starting minichatgpt ===")
    print("Hello!")
    
    # we are using 'for' loop so the range is 5 rounds
    for round_num in range(5):
        user_que = input("User: ")
        
        # making it casesensetive/lowercase to its easier
        que_lower = user_que.lower()
        
        #helps with questions so if specific words are in the question the bot answers accordingly
        if 'your name' in que_lower:
            print("minichatgpt: My name is minichatgpt.")
        elif 'weather' in que_lower:
            print("minichatgpt: It's always sunny in my world!")
        elif 'python' in que_lower:
            print("minichatgpt: Python is fun! We're learning it in class.")
        else:
            print("minichatgpt: I don't know.")
     # asking user to chat again
    again = input("minichatgpt: Would you like to chat again? (y/n): ")
    
    # seeing if its a 'y' or a 'n'.
    if again.lower() == 'y':
        minichatgpt()  #calling it again to rechat
    else:
        print("minichatgpt: Goodbye! Thanks for chatting!")
# this helps run the bot
minichatgpt()