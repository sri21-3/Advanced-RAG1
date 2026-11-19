from langchain_core.messages import HumanMessage, AIMessage
from src.rag_pipeline import rag_chain

# 1. converstational history storage

store = {}

# 2. get session history

def get_session_history(session_id):
    if session_id not in store:
        store[session_id]=[]
        return store[session_id] # chat History of that particular session/user

# 3.Create user session
session_id = "user1"

chat_history = get_session_history(session_id)

# 4. start the chatbot

print("\nWelcome to conversational chatbot")
print("\n Type exit to stop the chatbot")

# 5. chat loop
while True:
    question=input("\nYou:")

    if question.lower() == 'exit':
        print("Exiting from chatbot ....")
        break

    # 6. initialte the rag chain
    answer = rag_chain.invoke({
        "input":question,
        "chat_history": chat_history[-10:]
    })

    print("\nAI",answer)

    # 7.store the human message in chat history
    chat_history.append(HumanMessage(content=question))

    # 8. Store the AI message
    chat_history.append(AIMessage(content=answer))