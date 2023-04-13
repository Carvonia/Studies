import random
import os

outcomes = {
    ("Rock", "Paper"): "Your troops immobilized the Rocks, gaining you an advantage.",
    ("Paper", "Scissors"): "Your troops sliced thy enemies into pieces, no one shall stand!",
    ("Scissors", "Rock"): "The blunt force of your Rocks cracked the enemy`s defences!",
    ("Rock", "Scissors"): "Sun foresaw your strategies, your troops are no more...",
    ("Paper", "Rock"): "The enemy sent his forces to immobilize your troops, he is closing on you!",
    ("Scissors", "Paper"): "Your troops were nothing facing the enemy`s blades."
}
warriors = ["Rock", "Scissors", "Paper"]
score = 0


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def pick_warrior():
    while True:
        warrior_input = str(
            input(
                f"Pick a warrior: \nRock (Defense ++) (Bludgeon +++) \nPaper (Sharpness +++) (Swiftness +) \nScissors (Cutting +++) (Resistance -)\n"
            )
        )
        warrior_input = warrior_input.capitalize()
        if warrior_input in warriors:
            cls()
            return warrior_input
        else:
            cls()
            print(f"You picked an invalid warrior, try again.\n")


def score_update_print(outcome, score):
    if "gain" in outcome or "sliced" in outcome or "cracked" in outcome:
        score += 100
        print(f"\n{outcome}")
        print(f"\nYou gained 100 points!")
        print(f"Your current score is {score}!")
    else:
        score -= 50
        print(f"\n{outcome}")
        print(f"\nYou lost 50 points!")
        print(f"Your current score is {score}!")
    return score

def main(p_choice, score):
    cpu_choice = random.choice(warriors)

    print(f"Your Warrior: {p_choice}")
    print(f"Cpu`s Warrior: {cpu_choice}")

    if cpu_choice == p_choice:
        print(f"\nYou both sent the same type of troops. The battle results in a Tie!")
        print(f"Your score remains {score}.")
    else:
        outcome = outcomes.get((cpu_choice, p_choice))
        score = score_update_print(outcome, score)

    return score


cls()
print(
    f"You dear friend, are a general, a commander preparing to send soldiers to the battlefield."
)
print(f"Your enemy is the great Sun Tzu, he will have no mercy on your troops.")
print(f"Choose your soldiers carefully, and reach 300 points to win the war!\n")
while True:
    user_input = pick_warrior()
    score = main(user_input, score)
    if score >= 300:
        print(f"\nYou won the war, now going foward to conquering the whole world!")
        break
    elif score <= -150:
        print(f"\nYou lost the war, the enemy now lavishes uppon your land...")
        break
    is_loop = str(input(f"\nDo you want to play again? (y/n): ")).lower()
    cls()
    if is_loop == "y" or is_loop == "":
        print(f"Your current score is {score}. ", end="")
        continue
    break
