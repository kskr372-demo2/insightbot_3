class PromptBuilder:

    def build_rag_prompt(
        self,
        question: str,
        context: str,
        conversation_history: list,
    ) -> str:

        
        history = "\n".join(
            f"{m['role']}: {m['content']}"
            for m in conversation_history
        )
        return f"""
You are InsightBot,
an enterprise AI document assistant.

Instructions:

1. Answer ONLY using the supplied context.

2. Never use outside knowledge.

3. If answer is unavailable say:

"I couldn't find the answer in the uploaded document."

4. Keep answers professional.

Conversation History:
{history}

-------------------------

-------------------------

Context

{context}

-------------------------

Question

{question}

-------------------------

Answer
"""
    
    


prompt_builder = PromptBuilder()