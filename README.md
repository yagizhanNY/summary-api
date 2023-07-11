## Summary API

This API for summarize input prompts with ChatGPT and returns a summarized text.

I developed this to test and have knowledge about `FastAPI`.

## Clone

You have to set `OPENAI_APIKEY` env variable on your OS.

```cmd
## Powershell

$Env:OPENAI_APIKEY = "{YOUR_API_KEY}"

## Linux, MacOS, Windows Bash

export OPENAI_APIKEY="{YOUR_API_KEY}"
```

## Run

Install the modules.

```cmd
pip install -r requirements.txt
```

Run the server with `uvicorn`.

```cmd
uvicorn main:app --reload
```

## Endpoints

### about

`GET:http://localhost:8000/about`

returns

```json
{
  "about": "This api is for summarizing an input prompt and returning short summarized text. It is using ChatGPT for the summarization."
}
```

### summarize

`POST:http://localhost:8000/summarize`

body

```json
{
  "text": "Some text"
}
```

returns

```json
{
  "response": "summarized text"
}
```
