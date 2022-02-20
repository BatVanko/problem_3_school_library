# problem_3_school_library
Your task is to do online book library.
On the first line you will receive a string representing a shelf with books in the library. Every book is separated with “&”. On the next line until the “Done” command you will be receiving the following command separated with “ | ”:
Input
•	The possible commands are:
o	"Add Book | {book name}"
o	"Take Book | {book name}"
o	"Swap Books | {book1} | {book2}"
o	"Insert Book | {book name}"
o	"Check Book | {index}"
o	"Done"
Output
•	The possible outputs are:
o	"{firstBook}, {secondBook}, … {lastBook}"

Input
Don Quixote&The Great Gatsby&Moby Dick
Add Book | Ulysses
Take Book | Don Quixote
Insert Book | Alice's Adventures in Wonderland
Done

Output
Ulysses, The Great Gatsby, Moby Dick, Alice's Adventures in Wonderland

