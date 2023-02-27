#Tan Hyong Hsing
#20DDT21F1002
#Simple guessing game (Guess numberr between 1 to 10.)
max_attempt = 3
i = 0

while i < max_attempt:
    guess = int(input('Guess a number . \n'))
    i = i + 1
    if guess == 1 or guess == 2 or guess == 3 or guess == 4 or guess == 5 or guess == 6 or guess == 7 or guess == 8 or guess == 9 or guess == 10:
        print('You Win')
        break
    else :
        print('\n')
else :
    print('You Lost !')
