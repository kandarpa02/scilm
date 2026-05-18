from .setup_prompt import seed
from .lm import *

messages = [
    {
        "role": "system",
        "content": seed
    }
]

model, tokenizer = None, None

model_name = "Qwen/Qwen2.5-3B-Instruct"

if model or tokenizer is None:
    model, tokenizer = init_model(model_name=model_name)

def generate_text():
    global messages, model, tokenizer

    print("JERVIS ONLINE")
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("Kandarpa: ")

        if user_input.lower() in ["exit", "quit"]:
            print("\nJervis: Shutting down, sir.")
            break

        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        prompt = tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = tokenizer(
            prompt,
            return_tensors="pt"
        ).to(model.device)


        with torch.no_grad():

            outputs = model.generate(
                **inputs,
                max_new_tokens=500,
                temperature=0.8,
                top_p=0.9,
                do_sample=True,
                repetition_penalty=1.1
            )

        response = tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[1]:],
            skip_special_tokens=True
        )

        # Clean response
        response = response.strip()


        print(f"\nJervis: {response}\n")


        messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )


        if len(messages) > 20:
            messages = [messages[0]] + messages[-19:]

