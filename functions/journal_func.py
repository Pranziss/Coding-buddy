import json
import os
from datetime import datetime
from functions.model_runner import run_model

def save_to_journal(entry):
    try:
        if not os.path.exists("journal.json"):
            journal = []
        else:
            with open("journal.json", "r", encoding="utf-8") as f:
                journal = json.load(f)
                if not isinstance(journal, list):
                    raise ValueError("journal.json must be a list")

        journal.append(entry)
        with open("journal.json", "w", encoding="utf-8") as f:
            json.dump(journal, f, indent=2)
    except Exception as e:
        print("[JOURNAL SAVE ERROR]", e)

def view_journal():
    try:
        with open("journal.json", "r", encoding="utf-8") as f:
            journal = json.load(f)
            return journal if isinstance(journal, list) else []
    except Exception as e:
        print("[VIEW JOURNAL ERROR]", e)
        return []

def summarize_journal():
    try:
        with open("journal.json", "r", encoding="utf-8") as f:
            journal = json.load(f)

        if not isinstance(journal, list) or len(journal) < 2:
            return {"summary": "Not enough entries to summarize just yet."}

        convo_text = "\n".join(f"User: {e['user']}\nNova: {e['nova']}" for e in journal[-10:])
        summary_prompt = f"Summarize the following conversation between Franz and Nova:\n{convo_text}\nSummary:"
        summary, stderr = run_model(summary_prompt)
        if stderr:
            print("[SUMMARY STDERR]", stderr)

        return {"summary": summary or "Something went blank—try again."}
    except Exception as e:
        print("[SUMMARY ERROR]", e)
        return {"error": str(e)}

def get_recent_dialogue(n=3):
    try:
        journal = view_journal()
        if not isinstance(journal, list):
            return ""
        return "\n".join(
            f"User: {entry['user']}\nNova: {entry['nova']}"
            for entry in journal[-n:]
        )
    except Exception as e:
        print("[RECENT DIALOGUE ERROR]", e)
        return ""