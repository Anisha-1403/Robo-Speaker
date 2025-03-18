import pyttsx3

input("Press Enter to start RoboSpeaker...")  # Prevents instant closure at the start

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Me")
    
    engine = pyttsx3.init()
    
    while True:
        x = input("Enter what you want me to speak (or type 'goodbye' to exit): ")
        if x.lower() == "goodbye":
            engine.say("Goodbye! Have a great day!")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()

# Keep window open after execution
input("\nPress Enter to exit...")
