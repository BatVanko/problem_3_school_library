books = input().split("&")
commands_line = input()

while not commands_line == "Done":
    commands = commands_line.split(" | ")
    command = commands[0]

    if command == "Add Book":
        if commands[1] not in books:
            books.insert(0, commands[1])
    elif command == "Take Book":
        if commands[1] in books:
            books.remove(commands[1])
    elif command == "Swap Books":

        if commands[1] and commands[2] in books:
            book1 = commands[1]
            book2 = commands[2]
            index1 = books.index(commands[1])
            index2 = books.index(commands[2])
            books[index1], books[index2] = books[index2], books[index1]

    elif command == "Insert Book":
        book_name = commands[1]
        if commands[1] not in books:
            books.append(commands[1])
    elif command == "Check Book":
        index = int(commands[1])
        if 0 <= index < len(books):
            print(books[index])

    commands_line = input()

print(", ".join(books))
