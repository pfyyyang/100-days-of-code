import art
import game_data
import random


def person():
    random_person = random.choice(game_data.data)
    return random_person

person1 = person()
person2 = person()

def game(person1, person2):
    current_score = 0

    while True:
        while person1 == person2:
            person2 = person()

        print(
            f"Compare A: {person1['name']}, "
            f"a {person1['description']}, "
            f"from {person1['country']}"
        )

        print(art.vs)

        print(
            f"Compare B: {person2['name']}, "
            f"a {person2['description']}, "
            f"from {person2['country']}"
        )

        follower1 = person1["follower_count"]
        follower2 = person2["follower_count"]

        compare = input(
            "Who has more followers? Type 'A' or 'B': "
        ).upper()

        if follower1 > follower2:
            correct_answer = "A"
        else:
            correct_answer = "B"

        if compare == correct_answer:
            current_score += 1
            print(f"You are right! Current score: {current_score}")

            person1 = person2
            person2 = person()
        else:
            print(f"Sorry, that's wrong. Final score: {current_score}")
            break


game(person1, person2)




