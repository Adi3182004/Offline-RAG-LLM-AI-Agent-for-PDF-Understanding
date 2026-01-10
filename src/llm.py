import subprocess

MODEL_NAME = "phi3"

def generate(prompt):
    result = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=prompt.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode("utf-8", errors="ignore").strip()
