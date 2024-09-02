# open a starting letter which has all contents need to be sent out, you need to change the name only.
# Under read mode, you can read the file and save the contents to a variable 'sam_letter'
with open('./Input/Letters/starting_letter.txt', mode='r') as sample_letter:
    sam_letter = sample_letter.read()
    # print(sam_letter)  # during coding, you can print your contents to make sure everything is good

    # Read 'invited_names.txt' file in 'r' mode, store all names in a list called names
    with open('./Input/Names/invited_names.txt', mode='r') as names:
        # Here I used readlines so that each line in the text file will be a string in a list 'names'
        names = [name for name in names.readlines()]

        # Here I used strip method to get rid of \n and have a new variable for the updated name
        for name in names:
            stripped_name = name.strip()

            # In this for loop, I replaced the '[name]' in sam_letter with stripped_name
            # and saved it to variable 'new_letter'
            new_letter = sam_letter.replace('[name]', stripped_name)

            # I used print to check whether the replacement was successful.
            # print(new_letter)

            # Finally I opened a new file and save the "ready to send letter" (new_letter) to ready_letter
            # The letter name was replaced with letter_for_'stripped_name'.
            with open(f'Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as ready_letter:
                ready_letter.write(new_letter)
