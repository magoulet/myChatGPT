# ChatGPT Assistant

The ChatGPT Assistant is a simple Python script that allows interactive conversations with the OpenAI GPT-3.5-turbo model. It acts as an assistant for a technical program manager who excels in writing clear, concise documents and utilizes Python to enhance their work. The script enables the user to have back-and-forth exchanges with the assistant, simulating a chat-like conversation.

## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Configuration](#configuration)
- [Conversation Loop](#conversation-loop)
- [Assistant Reply](#assistant-reply)
- [Handling Errors](#handling-errors)
- [Conclusion](#conclusion)

## Introduction

The ChatGPT Assistant script leverages the OpenAI GPT-3.5-turbo model to provide an intelligent assistant experience. The model is capable of generating human-like responses based on the given conversation context. By interacting with the assistant, the user can benefit from its technical expertise and ability to write clear and concise documents.

## Requirements

To run the ChatGPT Assistant script, you need the following libraries:
- `openai` - The OpenAI Python library for making API calls.
- `os` - Library for interacting with the operating system.
- `pickle` - Library for serializing Python objects.
- `readline` - Library for command-line input and history.
- `rich.console` - Library for rich text formatting in the console.
- `rich.markdown` - Library for rendering Markdown text.
- `sys` - Library for system-specific parameters and functions.
- `time` - Library for time-related functions.
- `yaml` - Library for working with YAML configuration files.

Make sure to install these libraries before running the ChatGPT Assistant script.

## Configuration

The ChatGPT Assistant requires a configuration file named `config.yml` in the base directory. This YAML file should contain your OpenAI API key, which is used to authenticate the API calls. The configuration file follows the structure as shown below:

```yaml
openAI:
  key: <your_personal_key>
```

Replace `<your_personal_key>` with your actual OpenAI API key.

## Conversation Loop

The main function of the ChatGPT Assistant script is the conversation loop. It handles the user's input, sends it to the OpenAI API to generate a response, and displays the assistant's reply.

The script starts by loading the configuration from the `config.yml` file, including the OpenAI API key. The input loop prompts the user for a message and stores the messages in a list for the chat history. The chat history is saved in a pickle file to maintain the conversation state.

If a `messages.pickle` file exists, it will load the chat history from it instead of prompting for user input. This allows the conversation to resume seamlessly if the script is restarted.

## Assistant Reply

The script uses the OpenAI API to pass the chat history to the GPT-3.5-turbo model. The model generates a reply based on the conversation provided. The reply is extracted from the API response and added to the chat history.

The reply from the assistant is displayed using the `rich.console` library, which allows for rich text formatting and rendering of Markdown content. The assistant's reply is printed to the console in a chat-like format, with the label "**Assistant**: " before the text.

## Handling Errors

In case of any errors encountered during the conversation loop, the script catches the exception and sets a flag to retry the conversation with the previous chat history. This ensures that the conversation can continue despite any temporary errors. The script waits for 5 seconds before retrying.
