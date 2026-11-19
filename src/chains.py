from langchain_core.output_parsers import StrOutputParser
from src.config import llm
from src.prompts import (
    intent_prompt,
    contextualize_prompt,
    answer_prompt,
    history_prompt,
    general_prompt
    )

# Intent Classification Chain

intent_chain= (
    intent_prompt | llm | StrOutputParser()
)

# rewiting prompt Chain

contextualize_chain = (
    contextualize_prompt | llm | StrOutputParser()
)

# Document Answer Chain

document_answer_chain = (
    answer_prompt | llm | StrOutputParser()
)

# history Answer Chain

history_answer_chain = (
    history_prompt | llm | StrOutputParser()
)

# General Conversational Chain

general_chain = (
    general_prompt | llm | StrOutputParser()
)