# pdfGPT Plugin for ChatGPT

This repository contains a plugin for ChatGPT based on the [pdfGPT](https://github.com/bhaskatripathi/pdfGPT) repository by [bhaskatripathi](https://github.com/bhaskatripathi). This plugin allows ChatGPT to interact with the contents of a PDF file, effectively turning your PDF files into a chatbot.

## What does it do?

The pdfGPT Plugin allows you to chat with an uploaded PDF file using GPT functionalities. The application intelligently breaks the document into smaller chunks and employs a powerful Deep Averaging Network Encoder to generate embeddings. A semantic search is first performed on your PDF content and the most relevant embeddings are returned. A custom logic generates precise responses. The responses are much better than the naive responses by OpenAI.

## PDF Input

The plugin requires a PDF link that is accessible by the host. This link will be used to retrieve the PDF file for processing.

## Running with Docker

You can easily run the pdfGPT Plugin using Docker. Simply use the following command:

```
docker-compose up -d
```

This will start the plugin in detached mode, allowing it to run in the background. Upon initialization, the plugin will open port 3334.

## Acknowledgements

This plugin is based on the [pdfGPT](https://github.com/bhaskatripathi/pdfGPT) repository by [bhaskatripathi](https://github.com/bhaskatripathi). I would like to express my gratitude for their work in creating an open-source solution that allows us to turn PDF files into a chatbot.
