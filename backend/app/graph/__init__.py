from app.graph.graph_builder import build_graph

from app.graph.nodes.retrieve_node import RetrieveNode
from app.graph.nodes.prompt_node import PromptNode
from app.graph.nodes.llm_node import LLMNode
from app.graph.nodes.intent_node import IntentNode
from app.graph.nodes.general_llm_node import GeneralLLMNode


from app.services.embedding_service import embedding_service
from app.services.vector_service import vector_service
from app.services.citation_service import citation_service
from app.services.prompt_builder import prompt_builder
from app.services.memory_service import memory_service
from app.services.llm_service import llm_service

intent_node = IntentNode()

retrieve_node = RetrieveNode(
    embedding_service=embedding_service,
    vector_service=vector_service,
    citation_service=citation_service,
)

prompt_node = PromptNode(
    prompt_builder=prompt_builder,
    memory_service=memory_service,
)

llm_node = LLMNode(
    llm_service=llm_service,
)



general_llm_node = GeneralLLMNode(
    llm_service=llm_service
)




graph = build_graph(
    intent_node=intent_node,
    retrieve_node=retrieve_node,
    prompt_node=prompt_node,
    llm_node=llm_node,
    general_llm_node=general_llm_node,
)