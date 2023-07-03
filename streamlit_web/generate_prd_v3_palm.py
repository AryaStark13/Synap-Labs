import langchain
from langchain.llms import VertexAI
from langchain.prompts import PromptTemplate, load_prompt
import wandb
from wandb.integration.langchain import WandbTracer
import streamlit as st


def generate_prd_v3_palm(new_feature, new_feature_desc, wandb_name):
    wandb.login(key=st.secrets["WANDB_API_KEY"])

    wandb.init(
        project="generate_prd_v3_palm",
        config={
            "model": "text-bison-001",
            "temperature": 0.2
        },
        entity="arihantsheth",
        name=wandb_name,
    )

    llm = VertexAI(max_output_tokens=1024, project="synap-labs-390404", credentials=dict(st.secrets["GOOGLE_APPLICATION_CREDENTIALS"]))
    prompt_template = load_prompt("prompt_templates/generate_prd_template_v2.json") # For deployment
    # prompt_template = load_prompt("../prompt_templates/generate_prd_template_v3.json")  # For local testing

    prompt = prompt_template.format(
        new_feature=new_feature, new_feature_desc=new_feature_desc)

    try:
        output = llm(prompt, callbacks=[WandbTracer()])
    except Exception as e:
        print("GCP Authentication error")
        print(e)
        return

    # with open(f"./generated_prds/{new_feature}_prd_v3_palm.md", "w") as f: # For deployment
    # # with open(f"../generated_prds/{new_feature}_prd_palm.md", "w") as f: # For local testing
    #     f.write(output)

    wandb.finish()
    return output
