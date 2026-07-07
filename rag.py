# Orchestrate the complete RAG pipeline

from llm import generate_response
from prompts import RAG_PROMPT


def answer_question(question, retriever):
    """
    Execute the complete RAG pipeline.

    Args:
        question: User question
        retriever: LangChain retriever

    Returns:
        Generated answer
    """

    documents = retriever.invoke(question)

    if not documents:
        return "I couldn't find any relevant information in the uploaded documents."
    
    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt = RAG_PROMPT.format(
        context=context,
        question=question
    )

    answer = generate_response(prompt)

    return answer