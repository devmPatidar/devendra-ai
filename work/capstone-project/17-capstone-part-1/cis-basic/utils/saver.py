from datetime import datetime

def save_response(query, response):
    filename = "outputs.txt"

    with open(filename, "a") as f:
        f.write(f"\n--- {datetime.now()} ---\n")
        f.write(f"Query: {query}\n")
        f.write(f"Response:\n{response}\n")