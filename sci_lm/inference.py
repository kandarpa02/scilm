from .setup_prompt import instructions
from .lm import *

messages = [
    {
        "role": "system",
        "content": instructions
    }
]

model, tokenizer = None, None

model_name = "microsoft/Phi-4-mini-reasoning"

if model or tokenizer is None:
    model, tokenizer = init_model(model_name=model_name)

def generate_response(prompt, temperature=0.1, max_new_tokens=2048):
    global model, tokenizer
    messages.append({"role": "user", "content": prompt})
    input_text = "\n".join([f"{m['role']}: {m['content']}" for m in messages])
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    outputs = model.generate(
        **inputs,
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response.split("assistant:")[-1].strip()
    messages.append({"role": "assistant", "content": response})
    return response

