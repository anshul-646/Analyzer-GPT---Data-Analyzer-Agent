from autogen_agentchat.agents import CodeExecutorAgent

def getCodeExecutorAgent(code_executor):
    Code_executor_aget=CodeExecutorAgent(
        name="PythonCodeExecutor",
        code_executor=code_executor
    )
    
    return Code_executor_aget