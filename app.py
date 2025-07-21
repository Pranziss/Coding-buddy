from flask import Flask, render_template, request, jsonify
from functions.memory_func import load_memory, save_memory
from functions.history_func import load_history, save_history
from functions.journal_func import save_to_journal, view_journal, summarize_journal, get_recent_dialogue
from functions.model_runner import run_model
from functions.prompts import build_nova_prompt
from brain import nova  # brain
import datetime
import os

app = Flask(__name__)

def get_user_role(request):
    creator_ip = "192.168.1.21"  # Replace with your laptop's local IP if needed
    current_ip = request.remote_addr
    return "creator" if current_ip == creator_ip else "guest"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message", "")
    memory = load_memory()
    memory_facts = memory.get("memories", [])
    user_role = get_user_role(request)
    print(f"[ROLE DETECTED]: {user_role}")

    recent_dialogue = get_recent_dialogue(3)
    prompt = build_nova_prompt(user_input, memory_facts, user_role, previous_dialogue=recent_dialogue)

    try:
        raw_output, stderr = run_model(prompt, nova)
        print("Nova's raw output:\n", raw_output)
        if stderr:
            print("[MODEL STDERR]", stderr)

        lines = raw_output.split("\n")
        response_lines = [line for line in lines if not line.strip().startswith(">>>")]
        reply = "\n".join(response_lines).strip() or "I'm here, but something glitched—try asking me again?"

        history = load_history()
        history.append({"user": user_input, "nova": reply})
        save_history(history[-50:])
        save_to_journal({
            "timestamp": datetime.datetime.now().isoformat(),
            "user": user_input,
            "nova": reply
        })

        if "remember that" in user_input.lower():
            memory.setdefault("memories", []).append(user_input)
            save_memory(memory)

        return jsonify({"response": reply})

    except Exception as e:
        print("[ASK ROUTE ERROR]", e)
        return jsonify({"response": f"Nova hit a snag: {str(e)}"})

@app.route("/history", methods=["GET"])
def get_history():
    return jsonify(load_history())

@app.route("/clear-history", methods=["POST"])
def clear_history():
    save_history([])
    return jsonify({"status": "History cleared"})

@app.route("/view-history")
def view_history():
    return render_template("history.html")

@app.route("/journal", methods=["GET"])
def journal_view():
    return jsonify(view_journal())

@app.route("/summarize-journal", methods=["GET"])
def summarize():
    return jsonify(summarize_journal())

if __name__ == "__main__":
    print("🚀 Nova is booting up on http://192.168.1.21:5000/")
    app.run(host="0.0.0.0", port=5000, debug=True)