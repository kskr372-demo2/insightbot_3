from app.graph.graph_builder import build_graph

from app.graph.nodes.retrieve_node import RetrieveNode
from app.graph.nodes.prompt_node import PromptNode
from app.graph.nodes.llm_node import LLMNode
from app.graph.nodes.intent_node import IntentNode
from app.graph.nodes.general_llm_node import GeneralLLMNode
from app.graph.nodes.tool_node import ToolNode
from app.graph.nodes.approval_node import ApprovalNode
from app.graph.nodes.execute_tool_node import ExecuteToolNode
# Parallel nodes
from app.graph.nodes.summarization_node import SummarizationNode
from app.graph.nodes.security_node import SecurityNode

from app.services.embedding_service import embedding_service
from app.services.vector_service import vector_service
from app.services.citation_service import citation_service
from app.services.prompt_builder import prompt_builder
from app.services.memory_service import memory_service
from app.services.llm_service import llm_service

from app.agents.supervisor_agent import SupervisorAgent
from app.agents.general_agent import GeneralAgent
from app.agents.tool_agent import ToolAgent
from app.graph.nodes.supervisor_node import SupervisorNode
from app.graph.nodes.general_agent_node import GeneralAgentNode
from app.graph.nodes.tool_agent_node import ToolAgentNode
from app.graph.nodes.agent_handoff_node import AgentHandoffNode

intent_node = IntentNode()

tool_node = ToolNode()

retrieve_node = RetrieveNode(
    embedding_service=embedding_service,
    vector_service=vector_service,
    citation_service=citation_service,
)

# ------------------------------------------------
# Parallel Nodes
# ------------------------------------------------

summarization_node = SummarizationNode()

security_node = SecurityNode()
# ------------------------------------------------
# Prompt
# ------------------------------------------------
prompt_node = PromptNode(
    prompt_builder=prompt_builder,
    memory_service=memory_service,
)

# ------------------------------------------------
# LLM
# ------------------------------------------------
llm_node = LLMNode(
    llm_service=llm_service,
)



general_llm_node = GeneralLLMNode(
    llm_service=llm_service
)

# ------------------------------------------------
# HITL
# ------------------------------------------------
approval_node = ApprovalNode()

execute_tool_node = ExecuteToolNode()
# ================================================================
# MULTI-AGENT SYSTEM
# ================================================================

# ------------------------------------------------
# Create Agents
# ------------------------------------------------

supervisor_agent = SupervisorAgent()

general_agent = GeneralAgent(
    llm_service=llm_service
)

tool_agent = ToolAgent()


# ------------------------------------------------
# Create Agent Wrapper Nodes
# ------------------------------------------------

supervisor_node = SupervisorNode(
    supervisor_agent=supervisor_agent
)

general_agent_node = GeneralAgentNode(
    general_agent=general_agent
)

tool_agent_node = ToolAgentNode(
    tool_agent=tool_agent
)

agent_handoff_node = AgentHandoffNode()
# ================================================================
# BUILD GRAPH
# ================================================================


graph = build_graph(
    intent_node=intent_node,
    retrieve_node=retrieve_node,
    summarization_node=summarization_node,
    security_node=security_node,
    prompt_node=prompt_node,
    llm_node=llm_node,
    general_llm_node=general_llm_node,
    tool_node=tool_node,
    approval_node=approval_node,
    execute_tool_node=execute_tool_node,
    # Multi-Agent
    supervisor_node=supervisor_node,
    general_agent_node=general_agent_node,
    tool_agent_node=tool_agent_node,
    agent_handoff_node=agent_handoff_node,
)