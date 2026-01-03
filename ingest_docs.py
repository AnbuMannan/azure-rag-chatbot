import os
import uuid
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

# Load environment variables
load_dotenv()
print("Embedding deployment:", os.getenv("AZURE_OPENAI_EMBED_DEPLOYMENT"))
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

def upload_text(text: str):
    # Generate embedding
    embedding = openai_client.embeddings.create(
        model=os.getenv("AZURE_OPENAI_EMBED_DEPLOYMENT"),
        input=text
    ).data[0].embedding

    # Create search document
    doc = {
        "id": str(uuid.uuid4()),
        "content": text,
        "embedding": embedding
    }

    # Upload to Azure AI Search
    search_client.upload_documents([doc])
    print("✅ Uploaded:", text)


# ---- SAMPLE DOCUMENTS (you can edit these) ----
upload_text("Employees are entitled to 12 casual leaves per year.")
upload_text("Office working hours are from 9 AM to 6 PM.")
upload_text("Employees must apply leave through the HR portal.")
upload_text("Casual leave requests should be approved by the reporting manager.")
