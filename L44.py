#the authors' names are Abby Newton and Sydney Eidelbes
def rock_paper_scissors(choice):
    if choice=="scissor":
        print("scissors beats paper")
    elif choice=="paper":
        print("paper eats rock")
    else:
        print("rock hits scissors")
choice=["paper","rock","paper","scissor","rock", "rock","scissor","paper"]
for item in choice:
    rock_paper_scissors(item)
