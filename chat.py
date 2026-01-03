import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizedQuery
from azure.core.credentials import AzureKeyCredential

# Load environment variables
load_dotenv()

# Azure OpenAI client
openai_client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-01"
)

# Azure AI Search client
search_client = SearchClient(
    endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
    index_name=os.getenv("AZURE_SEARCH_INDEX"),
    credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
)

def ask(question: str):
    # 1️⃣ Embed the user question
    q_embedding = openai_client.embeddings.create(
        model=os.getenv("AZURE_OPENAI_EMBED_DEPLOYMENT"),
        input=question
    ).data[0].embedding

    # 2️⃣ Vector search (NEW API)
    vector_query = VectorizedQuery(
        vector=q_embedding,
        k_nearest_neighbors=3,
        fields="embedding"
    )

    results = search_client.search(
        search_text=None,
        vector_queries=[vector_query]
    )

    context = "\n".join([doc["content"] for doc in results])

    # 3️⃣ Ask GPT with grounded context
    response = openai_client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an HR assistant. "
                    "Answer ONLY using the provided context. "
                    "If the answer is not in the context, say "
                    "'I don't have information about that.'"
                )
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{question}"
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content


# ---- TEST ----
print("\nQ: Casual leave requests approved By?")
print("A:", ask("Casual leave requests approved By?"))

print("\nQ: What are office working hours?")
print("A:", ask("What are office working hours?"))

print("\nQ: Is work from home allowed?")
print("A:", ask("Is work from home allowed?"))
