from .setup_prompt import instructions
from .lm import *

# Conversation history
messages = [
    {
        "role": "system",
        "content": instructions,
    }
]

model = None
tokenizer = None

model_name = "microsoft/Phi-4-mini-reasoning"

# Load model once
if model is None or tokenizer is None:
    model, tokenizer = init_model(model_name=model_name)


def generate_response(prompt, temperature=0.0, max_new_tokens=512):
    global model, tokenizer, messages

    # Add the user's message
    messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    # Format using the model's official chat template
    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
    ).to(model.device)

    # Generate
    outputs = model.generate(
        inputs,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        do_sample=(temperature > 0),
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

    # Decode only the newly generated tokens
    generated_tokens = outputs[0][inputs.shape[-1]:]

    response = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True,
    ).strip()

    # Save assistant response
    messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

    return response