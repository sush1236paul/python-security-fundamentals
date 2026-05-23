# Writing to a file

with open("notes.txt", "w") as file:
    file.write("Hello, this is my first file handling program.\n")
    file.write("Learning Python for cybersecurity.\n")


# Reading from a file

with open("notes.txt", "r") as file:
    content = file.read()

    print(content)
