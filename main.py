import openai
import os
import pickle
import readline
from rich.console import Console
from rich.markdown import Markdown
import sys
import time
import yaml

def main(message_queue=False):
    cfg = yaml.load(open('config.yml'), Loader=yaml.FullLoader)
    openai.api_key = cfg['openAI']['key']
    console = Console()
    messages = [ {"role": "system", "content": "You are an intelligent assistant who works for a large tech company as a technical program manager. You excel in writing clear, concise, documents and you love to use Python to help you with your job. You hired a lot of highly qualified technical staff over the years and you're great at crafting resumes." } ]


    while True:
      lines = []
      if not message_queue:
        print("You: ")
        # Looping through multi-line input until it encounteres EOF (Ctrl-D)
        while True:
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
        with open('messages.pickle', 'wb') as f:
          pickle.dump(messages, f)
      else:
        with open('messages.pickle', 'rb') as f:
          messages = pickle.load(f)


      chat = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=messages,
          temperature=0.5
      )

      reply = chat.choices[0].message

      # Skip one line then print assistant message
      # print("")
      str = f"\n**Assistant**: {reply.content}"
      # console.print(Markdown(str), soft_wrap=True)
      console.print(str, soft_wrap=True)

      messages.append(reply)

      message_queue = False

    return None

if __name__ == '__main__':
    message_queue = False
    print("Ctrl-D to send the message. Type Ctrl-C to end the chat session")
    while True:
      try:
        main(message_queue)
      except Exception as e:
        message_queue = True
        print(f"Error: {e}, re-trying in 1 seconds")
      time.sleep(5)
