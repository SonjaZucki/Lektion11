import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0
wrong_guesses = []

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

for score_dict in score_list:
    score_text = "{0} had {1} attempts on the secret number {2}, with the wrong guesses {3} on {4}".format(score_dict.get("name"),
                                                                                                        str(score_dict.get("attempts")),
                                                                                                        score_dict.get("secret"),
                                                                                                        score_dict.get("guesses"),
                                                                                                            score_dict.get("date"))
    print(score_text)

name: str = input("Hi, what is your name? ")
while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"name": name, "secret": secret, "attempts": attempts, "guesses": wrong_guesses, "date": str(datetime.datetime.now())})
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)