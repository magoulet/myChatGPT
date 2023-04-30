import openai
import yaml

def main():
    cfg = yaml.load(open('config.yml'), Loader=yaml.FullLoader)
    openai.api_key = cfg['openAI']['key']

    messages = [ {"role": "system", "content": "You are an intelligent assistant." } ]
    exit_words = ("q","Q","quit","QUIT","EXIT")
    print("Type q, Q, quit, QUIT or EXIT and press Enter to end the chat session")

    while True:
        message = input("You: ")
        if message in exit_words:
           print("ENDING CHAT")
           break
        else:

            messages.append(
                {"role": "user", "content": message},
            )

            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=60
            )

            reply = chat.choices[0].message

            print("Assistant: ", reply.content)

            messages.append(reply)

    return None

if __name__ == '__main__':
    main()
