from .setup_prompt import instructions
from .lm import *
import torch

# Conversation history
messages = [
    {
        "role": "system",
        "content": instructions,
    }
]

# Load model once
if model is None or tokenizer is None:
    model, tokenizer = init_model(model_name)


def model_setup(model_name):
    model, tokenizer = init_model(model_name)
    def generate_response(instructions, prompt, temperature=0.0, max_new_tokens=512):
        # Add user message
        messages = [
            {

            "role": "system",
            "content": instructions,

            },
            {

            "role": "user",
            "content": prompt,

            }
        ]

        inputs = tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt",
        )

        # Move everything to the model device
        inputs = inputs.to(model.device)

        # Generation
        if temperature > 0:
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=temperature,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )
        else:
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )

        # Remove prompt tokens
        input_length = inputs["input_ids"].shape[1]
        generated_tokens = outputs[0][input_length:]

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

    return generate_response