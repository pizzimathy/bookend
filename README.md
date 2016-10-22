## booklist

A tool for keeping track of the books you want to read.

### usage

`$ booklist [-a | --add]` Prompts for a new book to be added to the list.

`$ booklist [-l | --list]` Prettyprints a list of all the books currently in the list.

`$ booklist [-c | --checkout] <title>` Specify the title of a book, and it'll be removed from the list.

`$ booklist [-s | --search] <term>` Searches the list of books for a string matching the term provided.


### checklist

- [ ] close-match string searching
- [ ] faster string searching
- [ ] create queryable server to store lists remotely
- [x] case-insensitivie searching