"""The code below takes input from the user,
and tries to match the first word with a command in verb_dict.
If a match is found, the corresponding function is called."""


def get_input():
    command = input("please input verb: ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print("Unknown verb {}".format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))


def say(noun):
    return 'You said "{}"'.format(noun)


verb_dict = {
    "say": say,
}

while True:
    get_input()
