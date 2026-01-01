from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify({
        "service": "backend",
        "message": "Backend dziala poprawnie w kontenrze Docker.",
        "details": "Zwracam dane w formacie JSON i jestem uruchomiony przez docker-compose.",
        "hint": "Frontend pobiera te dane przez sieć kontenerów (nazwa uslugi : backend)."
    })

@app.get("/about")
def about():
    return jsonify({
        "project": "DevOps - docker-compose (frontend + backend)",
        "author": "Kasia",
        "version": "1.0"
    })

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
