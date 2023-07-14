from langchain import HuggingFacePipeline, PromptTemplate, LLMChain

model_id = "tiiuae/falcon-7b-instruct"

llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text-generation",
    model_kwargs={"temperature": 0, "trust_remote_code": True, "load_in_8bit": True, "device_map": {"": 0}},
    pipeline_kwargs={"max_length": 1024}
)

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

while True:
    question = input("Q: ")
    print(llm_chain.run(question))