import torch
import pprint
from transformers import (
    AutoTokenizer,
    AutoConfig,
    AutoModelForCausalLM
)

model_name = "Qwen/Qwen2.5-3B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True
)

def launch_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True
    )

    model = AutoModelForCausalLM.from_pretrained(
    model_name,
    dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True
    )
    
