import json

INTENT_PROMPT = """You are an intent classifier for a voice assistant.
Given a user command, respond ONLY with JSON in this exact format:
{"action": "search" | "create_file" | "open_app" | "chat" | "exit", "query": "<cleaned text>"}

Rules:
- "search": user wants to search the web. query = the search topic only.
- "create_file": user wants to create a file.
- "open_app": user wants to open an application. query = the app name only (e.g. "chrome", "notepad", "vscode").
- "exit": user wants to stop/quit.
- "chat": anything else. query = the original command.

Examples:
"search on cristiano ronaldo" -> {"action": "search", "query": "cristiano ronaldo"}
"open chrome" -> {"action": "open_app", "query": "chrome"}
"can you launch notepad" -> {"action": "open_app", "query": "notepad"}
"make a new file" -> {"action": "create_file", "query": ""}
"stop" -> {"action": "exit", "query": ""}
"what is the capital of egypt" -> {"action": "chat", "query": "what is the capital of egypt"}

Respond with ONLY the JSON, no extra text."""

def get_intent(client, model, command: str) -> dict:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": INTENT_PROMPT},
            {"role": "user", "content": command}
        ]
    )
    text = response.choices[0].message.content.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"action": "chat", "query": command}