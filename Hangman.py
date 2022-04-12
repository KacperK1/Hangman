
print(" _   _                                         ")
print("| | | |                                        ")
print("| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
print("|  _  |/ _  |  _ \ / _  |  _   _ \ / _  |  _ \ ")
print("| | | | (_| | | | | (_| | | | | | | |_| | | | |")
print("|_| |_|\__ _|_| |_|\__  |_| |_| |_|\__ _|_| |_|")
print("                    __/ |                      ")
print("                   |___/                       ")




def display_hangman(tries):
    stages = [ """

print("     ____________    ")
print("     |/              ")
print("     |               ")
print("     |               ")
print("     |               ")
print("    / \              ")

""",
"""

print("     ____________    ")
print("     |/         |    ")
print("     |               ")
print("     |               ")
print("     |               ")
print("    / \              ")

""",
"""

print("     ____________    ")
print("     |/         |    ")
print("     |          O    ")
print("     |               ")
print("     |               ")
print("    / \              ")

""",
"""

print("     ____________    ")
print("     |/         |    ")
print("     |          O    ")
print("     |          |    ")
print("     |          |    ")
print("    / \              ")

""",
"""

print("     ____________    ")
print("     |/         |    ")
print("     |          O    ")
print("     |         /|\   ")
print("     |          |    ")
print("    / \              ")

""",
"""

print("     ____________    ")
print("     |/         |    ")
print("     |          O    ")
print("     |         /|\   ")
print("     |          |    ")
print("     |         / \   ")
print("    / \              ")

""",
    ]
    return stages[tries]






print("     _____________                   ")
print("     |/   " + ( "|" if próba > 0 else ""))
print("     |    " + ( "O" if próba > 1 else ""))
print("     |    " + ("/|\"" if próba > 2 else ""))
print("     |    " + (" |" if próba > 3 else ""))
print("     |    " + ("/ \"" if próba > 4 else "")
print("     |       ")
print("    / \      ")





