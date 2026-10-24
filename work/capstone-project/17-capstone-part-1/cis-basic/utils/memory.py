from collections import deque

class Memory:
    def __init__(self, k=5):
        self.history = deque(maxlen=k)

    def add(self, query, response):
        self.history.append((query, response))

    def get_context(self):
        context = ""
        for q, r in self.history:
            context += f"User: {q}\nAssistant: {r}\n\n"
        return context