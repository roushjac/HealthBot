from langchain import HuggingFacePipeline, PromptTemplate, LLMChain
from flask import Flask, request, jsonify

app = Flask(__name__)

# model_id = "tiiuae/falcon-7b-instruct"
# model_id = "mosaicml/mpt-7b-instruct"
model_id = "bigscience/bloom-3b"

llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text-generation",
    model_kwargs={"temperature": 0, "trust_remote_code": True, "device_map": {"": 0}, "load_in_8bit": True},
    pipeline_kwargs={"max_length": 1024}
)
template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

@app.route('/generate', methods=["POST"])
def generate():
    content = request.json
    inp = content.get("text", "")
    llm_response = llm_chain.run(question=inp)
    return jsonify({"generated_text": llm_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # host of '0.0.0.0' makes the server accessible from the local network