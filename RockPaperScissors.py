import random
import time
round_var = 0
wins = 0
sd_win = 0
loss = 0
sd_loss = 0
game = 0
yesno = ''
selection = ''
cpu_selection = ''
sud_death = ''

#Welcome message
def welcome():
    print("Welcome to the Rock-Paper-Scissors Tournament.")
    time.sleep(3)
    print("You'll play 5 rounds against a computer.")
    time.sleep(3)
    print("If you win 3 times, you win the tournament!")
    time.sleep(3)
    print("Are you ready?")
    time.sleep(3)
    global game
    game = 1
    print('')

#Round counter
def round_start():
    global round_var
    round_var += 1 
    print('Round', round_var)
    print('')
    time.sleep(2)

#Select your hand sign
def select():
    global selection
    global cpu_selection
    print('Make a selection!')
    selection = input('Rock / Paper / Scissors: ')
    print('')
    print('Computer is making a choice...')
    time.sleep(3)
    print('')
    cpu_selection = random.choice(['Rock', 'Paper', 'Scissors'])

#Read the results    
def results():
    global selection
    global cpu_selection
    global wins
    global loss
    global sud_death
    global sd_win
    global sd_loss
    print('Rock, ', end = '')
    time.sleep(0.5)
    print('Paper, ', end = '')
    time.sleep(0.5)
    print('Scissors, ', end = '')
    time.sleep(0.5)
    print('SHOOT!')
    time.sleep(1)
    print('You chose:', selection)
    print('Computer chose:', cpu_selection)
    time.sleep(1)
    print('')
    #Rock Options
    if selection == 'Rock' and cpu_selection == 'Paper':
        print('Paper beats rock!')
        print('You lose!')
        loss += 1
        if sud_death == 'ON':
            sd_loss += 1
    elif selection == 'rock' and cpu_selection == 'Paper':
        print('Paper beats rock!')
        print('You lose!')
        loss += 1
        if sud_death == 'ON':
            sd_loss += 1
    elif selection == 'Rock' and cpu_selection == 'Scissors':
        print('Rock beats scissors!')
        print('You win!')
        wins += 1
        if sud_death == 'ON':
            sd_win += 1
    elif selection == 'rock' and cpu_selection == 'Scissors':
        print('Rock beats scissors!')
        print('You win!')
        wins += 1
        if sud_death == 'ON':
            sd_win += 1
    elif selection == 'Rock' and cpu_selection == 'Rock':
        print('Both chose rock!')
        print("It's a draw!")
    elif selection == 'rock' and cpu_selection == 'Rock':
        print('Both chose rock!')
        print("It's a draw!")
    #Paper Options
    elif selection == 'Paper' and cpu_selection == 'Scissors':
        print('Scissors beats paper!')
        print('You lose!')
        loss += 1
        if sud_death == 'ON':
            sd_loss += 1
    elif selection == 'paper' and cpu_selection == 'Scissors':
        print('Scissors beats paper!')
        print('You lose!')
        loss += 1
        if sud_death == 'ON':
            sd_loss += 1
    elif selection == 'Paper' and cpu_selection == 'Rock':
        print('Paper beats rock!')
        print('You win!')
        wins += 1
        if sud_death == 'ON':
            sd_win += 1
    elif selection == 'paper' and cpu_selection == 'Rock':
        print('Paper beats rock!')
        print('You win!')
        wins += 1
        if sud_death == 'ON':
            sd_win += 1
    elif selection == 'Paper' and cpu_selection == 'Paper':
        print('Both chose paper!')
        print("It's a draw!")
    elif selection == 'paper' and cpu_selection == 'Paper':
        print('Both chose paper!')
        print("It's a draw!")
    #Scissors Options
    elif selection == 'Scissors' and cpu_selection == 'Rock':
        print('Rock beats scissors!')
        print('You lose!')
        loss += 1
        if sud_death == 'ON':
            sd_loss += 1
    elif selection == 'scissors' and cpu_selection == 'Rock':
        print('Rock beats scissors!')
        print('You lose!')
        loss += 1
        if sud_death == 'ON':
            sd_loss += 1
    elif selection == 'Scissors' and cpu_selection == 'Paper':
        print('Scissors beats paper!')
        print('You win!')
        wins += 1
        if sud_death == 'ON':
            sd_win += 1
    elif selection == 'scissors' and cpu_selection == 'Paper':
        print('Scissors beats paper!')
        print('You win!')
        wins += 1
        if sud_death == 'ON':
            sd_win += 1
    elif selection == 'Scissors' and cpu_selection == 'Scissors':
        print('Both chose scissors!')
        print("It's a draw!")
    elif selection == 'scissors' and cpu_selection == 'Scissors':
        print('Both chose scissors!')
        print("It's a draw!")
    else:
        print("I can't tell what you put.")
        print("You automatically lose.")
        loss += 1
        if sud_death == 'ON':
            sd_loss += 1
    time.sleep(2)
    print('')

#Checks if the game is over    
def end():
    global game
    global yesno
    global round_var
    global wins
    global loss
    global sd_win
    global sd_loss
    global sud_death
    #Early Game End
    #Early Win
    if wins == 3:
        print('Congratulations! You won!')
        time.sleep(2)
        game = 0

    #Early Loss
    elif loss == 3:
        print('Aw... sorry. You lost!')
        time.sleep(2)
        game = 0

    #Full Game End
    elif round_var == 5:
        print("Well that's it. I guess we'll tally up the score.")
        time.sleep(2)
        print("Let's see here...")
        time.sleep(2)
        print("You won:", wins, 'rounds!')
        time.sleep(2)
        print("Meanwhile, you lost:", loss, 'rounds!')
        time.sleep(2)
        print('Therefore...')
        time.sleep(2)
        print('')
        
        #Win
        if wins > loss:
            print('Congratulations! You won!')
            time.sleep(2)
            game = 0

        #Lose
        elif wins < loss:
            print('Aw... sorry. You lost!')
            time.sleep(2)
            game = 0

        #Sudden Death
        else:
            print("Looks like we'll have to go to sudden death!")
            time.sleep(2)
            print("Next one to win, wins it all!")
            time.sleep(2)
            print('Ready? GO!')
            time.sleep(2)
            print('')
            sud_death = 'ON'
            while game == 1:
                if sd_win == 1:
                    print('Congratulations! You won!')
                    sud_death = ''
                    time.sleep(2)
                    game = 0
                elif sd_loss == 1:
                    print('Aw... sorry. You lost!')
                    sud_death = ''
                    time.sleep(2)
                    game = 0
                else:
                    select()
                    results()
    
    #Play Again?
    if game == 0:
        print("Would you like to play again?")
        time.sleep(3)
        yesno = input("Yes / No : ")
        if yesno == 'Yes':
            print('Alright! Roll it back!') 
            time.sleep(2)
            print('Your tournament starts...')
            time.sleep(1)
            print('NOW!')
            time.sleep(1)
            game = 1
            round_var = 0
            wins = 0
            loss = 0
            print('')
        elif yesno == 'yes':
            print('Alright! Roll it back!') 
            time.sleep(2)
            print('Your tournament starts...')
            time.sleep(1)
            print('NOW!')
            time.sleep(1)
            game = 1
            round_var = 0
            wins = 0
            loss = 0
            print('')
        else:
            print('Alright then. Goodbye!')
            time.sleep(5)

#How the game is meant to run
def main():
    welcome()
    while game == 1:
        round_start()
        select()
        results()
        end()

if __name__ == "__main__":
    main()
