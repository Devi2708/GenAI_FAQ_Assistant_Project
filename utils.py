def log_query(query, response):
    with open("logs.txt", "a") as f:
        f.write(f"Q: {query}\nA: {response}\n---\n")