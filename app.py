import logging
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# log stuff
logging.basicConfig(level=logging.DEBUG)

# Load Yi model
model = AutoModelForCausalLM.from_pretrained("01-ai/Yi-34B", device_map="auto", torch_dtype="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("01-ai/Yi-34B", trust_remote_code=True)

@app.route('/generate-text', methods=['POST'])
def generate_text():
    content = request.json
    input_text = content['text']
    inputs = tokenizer(input_text, return_tensors="pt")

    # Generate response
    outputs = model.generate(
        inputs.input_ids.cuda(),
        max_length=256,
        eos_token_id=tokenizer.eos_token_id,
        do_sample=True,
        repetition_penalty=1.3,
        no_repeat_ngram_size=5,
        temperature=0.7,
        top_k=40,
        top_p=0.8,
    )
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)

