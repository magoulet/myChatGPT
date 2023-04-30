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
    tab_size = 4
    console = Console(width=max_width, tab_size=tab_size)

    messages = [ {"role": "system", "content": "You are an intelligent assistant." } ]
    print("Ctrl-D to send the message. Type Ctrl-C to end the chat session")
    lines = []

    while True:
        console.print("You: ", end='')
        while True:
          try:
            try:
              line = input()
              lines.append(line)
            except EOFError:
              break
          except KeyboardInterrupt:
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

        print("")
        str = f"**Assistant**: {reply.content}"
        console.print(Markdown(str))

        messages.append(reply)

    return None

if __name__ == '__main__':
    main()
