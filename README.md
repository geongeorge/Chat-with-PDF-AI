## Chat with PDF

You will be able to chat with a pdf using this program. The program will make embeddings of the pdf and then you can ask questions to the pdf.

1. Add [together.ai](https://www.together.ai/) api key in .env file

2. Add the pdf file in the root folder as book.pdf

```bash
pipenv install   # Install dependencies

pipenv run python3 embed.py   # Make embeddings

pipenv run python3 chat.py   # Run the program
```
