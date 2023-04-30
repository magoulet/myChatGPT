import openai
import readline
from rich.console import Console
from rich.markdown import Markdown
import sys
import yaml

def main():
    cfg = yaml.load(open('config.yml'), Loader=yaml.FullLoader)
    openai.api_key = cfg['openAI']['key']
    max_width = 80
    console = Console(width=80, tab_size=4)

    messages = [ {"role": "system", "content": "You are an intelligent assistant." } ]
    exit_words = ("q","Q","quit","QUIT","EXIT")
    print("A blankline will send the message. Type Ctrl-d to end the chat session")
    lines = []

    while True:
        console.print("You: ", end='')
        while True:
          try:
            line = input()
            if line:
              lines.append(line)
            else:
              break
          except EOFError:
            console.print("Exiting program...")
            sys.exit(0)

        message = '\n'.join(lines)

        messages.append(
            {"role": "user", "content": message},
        )

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.5
            # max_tokens=60
        )

        reply = chat.choices[0].message

        # print("\n")
        str = f"Assistant: {reply.content}"
        console.print(Markdown(str))

        messages.append(reply)

    return None

if __name__ == '__main__':
    main()
