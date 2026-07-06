from llm import get_llm

model = get_llm()

response = model.generate_content(
    "Explain embeddings in one sentence."
)

print(response.text)