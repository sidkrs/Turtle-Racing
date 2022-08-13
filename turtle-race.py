import random
from turtle import Turtle
from turtle import Screen


print("Racers: 'red', 'orange', 'yellow', 'green', 'blue', 'purple'")

money = int(input("Enter a starting amount of money: $"))
cont = True


while cont:
    race = False
    screen = Screen()
    screen.setup(height=600, width=600)
    player_bet = screen.textinput(title="Make a bet", prompt="Which turtle do you think will win? Enter a color: ")
    amount = int(screen.textinput(title="Make a bet (odds: 10/1)", prompt="How much do you want to bet?: "))
    if amount > money:
        print("not enough money")
#change color of racers here
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    y_position = [-140, -84, -28, 28, 84, 140]
    racers = []

    for tt in range(0, 6):
        racer = Turtle(shape="turtle")
        racer.shapesize(1, 1, 3)
        racer.color(colors[tt])
        racer.penup()
        racer.goto(x=-280, y=y_position[tt])
        racers.append(racer)

    if player_bet:
        race = True

    while race:
        for racer in racers:
            if racer.xcor() > 280:
                winner = racer.pencolor()
                race = False
                if winner == player_bet:
                    print(f"You won! The {winner} turtle won the race!")
                    money -= amount
                    earnings = amount * 10
                    money += earnings
                    print(f"You have ${money}")
                else:
                    print(f"You lose. The {winner} turtle won the race.")
                    money -= amount
                    print(f"You have ${money}")
            #each turtle will take a random from 0 to 10 units
            step = random.randint(0,10)
            racer.forward(step)

    end = True
    while end:
        for racer in racers:
            step = random.randint(0,10)
            racer.forward(step)
            if racer.xcor() > 400:
                end = False
            racer.hideturtle()
    
    if money <= 0:
        cont = False
        print(f"You have no money left. Balance: ${money}")
    
    #Choice to keep playing or not
    option = screen.textinput(title="End Game", prompt="Do you want to keep playing? 'yes' or 'no'?: ")
    
    if option == 'no':
        cont = False
        print("Goodbye.")
        print(f"You left with ${money}")
    else:
        cont = True


