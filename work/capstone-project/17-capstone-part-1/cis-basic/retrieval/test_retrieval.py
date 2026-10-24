from retriever import get_retriever
from rich.console import Console
from rich.panel import Panel

console = Console()

def test():
    retriever = get_retriever()

    while True:
        query = input("\n🔍 Enter your query (or 'exit'): ")

        if query.lower() == "exit":
            break

        #docs = retriever.get_relevant_documents(query)
        docs = retriever.invoke(query)

        console.print(f"\n📊 Retrieved {len(docs)} documents\n")

        for i, doc in enumerate(docs, 1):
            console.print(Panel.fit(
                doc.page_content,
                title=f"Result {i}",
                border_style="green"
            ))

if __name__ == "__main__":
    test()