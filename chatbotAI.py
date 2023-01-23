import re
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# questions to be asked to the user

pairs = [
    [
        r"what is your preferred color for the seat of the hover chair\?$",
        ["My preferred color for the seat of the hover chair is {0}."],
    ],
    [
        r"what is your preferred color for the exterior of the hover chair\?$",
        ["My preferred color for the exterior of the hover chair is {0}."],
    ],
    [
        r"what is your preferred color for the lighting of the hover chair\?$",
        ["My preferred color for the lighting of the hover chair is {0}."],
    ],
    [
        r"what is your preferred color scheme for the hover chair\?$",
        ["My preferred color scheme for the hover chair is {0}."],
    ],
    [
        r"which materials do you prefer for the seat of the hover chair\?$",
        ["I prefer {0} for the seat of the hover chair."],
    ],
    [
        r"which materials do you prefer for the exterior of the hover chair\?$",
        ["I prefer {0} for the exterior of the hover chair."],
    ],
    [
        r"which materials do you prefer for the lighting of the hover chair\?$",
        ["I prefer {0} for the lighting of the hover chair."],
    ],
    [
        r"how do you plan to use the hover chair\?$",
        ["I plan to use the hover chair for {0}."],
    ],
    [
        r"which features are most important to you in a hover chair\?$",
        ["Speed: {0}, Sound System: {1}, Cooking: {2}, Watching movies: {3}, Driving: {4}, Flying: {5}"],
    ],
    [
        r"can you describe the hover chair you envision in the theme of a movie\?$",
        ["I envision a {0} themed hover chair."],
    ],
]


# Define the function to check if the answer is suitable
def check_answer(answer):
    # Use the SentimentIntensityAnalyzer to check if the answer is coherent and suitable
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(answer)
    if sentiment['compound'] >= 0.5:
        # generate a follow-up response based on the sentiment of the user's answer
        follow_up = generate_follow_up_response(sentiment)
        print(follow_up)
    else:
        print("I'm sorry, I didn't understand your answer. Could you please rephrase or provide more information?")

def generate_follow_up_response(sentiment):
    if sentiment['compound'] >= 0.8:
        return "Great, I'm glad you're excited about the hover chair! What else would you like to know?"
    elif sentiment['compound'] >= 0.5:
        return "That's good to hear! What else can I help you with?"
    elif sentiment['compound'] > 0:
        return "I see, thank you for your feedback. Is there anything else you would like to tell me?"
    else:
        return "I'm sorry, we'll make sure to improve the product based on your feedback. Is there anything else you would like to tell me?"

def comment_on_speed(answer):
    if answer != "skip":
        if int(answer) < 3:
            print("You're not in a rush, and that's totally fine! We'll make sure you're comfortable and relaxed in your hover chair.")
        else:
            print("You're all about speed and efficiency, we'll make sure your hover chair is fast and efficient.")

def comment_on_sound_system(answer):
    if answer != "skip":
        if int(answer) < 3:
            print("A sound system might not be a priority for you, but you will still be enjpying the cruise even without some tunes.")
        else:
            print("Everybody need some bass in their lives, Rock 'n Roll Baby!")

def comment_on_cooking(answer):
    if answer != "skip":
        if int(answer) < 3:
            print("Spaghetti with ketchup is fine, whatever, but the real question is: WHERE IS THE LAMBSAUCE??")
        else:
            print("I can't wait to be invited over for dinner, i have the perfect wine to go with steak!")

def comment_on_movies(answer):
    if answer != "skip":
        if int(answer) < 3:
            print("Watching movies might not be a priority for you, but we can still make sure your hover chair has basic entertainment features.")
        else:
            actors = ["Tom Hanks", "Robert De Niro", "Denzel Washington", "Leonardo DiCaprio", "Chris Hemsworth"]
            actor = random.choice(actors)
            print(f"Is {actor} your favourite actor by any chance? I am his biggest fan!")

def comment_on_driving(answer):
    if answer != "skip":
        if int(answer) < 3:
            print("Don't worry, you might not be the fastest on the track but you will still get to the finish line!")
        else:
            drivers = ["Lewis Hamilton", "Sebastian Vettel", "Michael Schumacher"]
            driver = random.choice(drivers)
            print(f"Seems like I am talking to the new rival of {driver} i guess ;)")


def comment_on_flying(answer):
    if answer != "skip":
        if int(answer) < 3:
            print("Flying might not be a priority for you, but we can still make sure your hover chair has basic flying features.")
        else:
            pilots = ["Green Goblin from Spiderman", "Superman", "Iron Man", "Pete Maverick from Top Gun", "the Wright brothers"]
            pilot = random.choice(pilots)
            print(f"I see you are a flying enthusiast as well! Your hover chair will have the most amazing flying ablities so you will just feel like {pilot}")

# Main function to run the chatbot
def chatbot():
    for pair in pairs:
        pattern = re.compile(pair[0])
        while True:
            # Ask the user the question
            question = input(pair[0])
            # Check if the user's answer is suitable using NLTK
            check_answer(question)
            # Check if the user's answer matches the pattern
            match = pattern.match(question)
            if match:
                # If the answer is suitable, get the response template
                response = random.choice(pair[1])
                # Fill in the response template with the user's answer
                answer = match.groups()[0]
                # Print the final response
                print(response.format(answer))
                break
            else:
                print("I'm sorry, I didn't understand your answer. Could you please rephrase or provide more information?")

# Run the chatbot
chatbot()
