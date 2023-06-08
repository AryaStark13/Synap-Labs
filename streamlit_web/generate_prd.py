import langchain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate, load_prompt
import wandb
from wandb.integration.langchain import WandbTracer
import openai
import streamlit as st

def generate_prd(company_name, company_desc, existing_feature_list, new_feature, new_feature_desc, wandb_name):
    wandb.login(key=st.secrets["WANDB_API_KEY"])

    wandb.init(
        project="generate_simple_prd",
        config={
            "model": "gpt-3.5-turbo",
            "temperature": 0
        },
        entity="arihantsheth",
        name=wandb_name,
    )

    llm = OpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=st.secrets["OPENAI_API_KEY"])
    prompt_template = load_prompt("prompt_templates/generate_prd_template.json")

    prompt = prompt_template.format(company_name=company_name, company_desc=company_desc,
                                    existing_feature_list=existing_feature_list, new_feature=new_feature, new_feature_desc=new_feature_desc)

    try:
        output = llm(prompt, callbacks=[WandbTracer()])
    except openai.error.AuthenticationError as e:
        print("OpenAI unknown authentication error")
        print(e.json_body)
        print(e.headers)
        return

    with open(f"generated_prds/{company_name}_prd_{new_feature}.md", "w") as f:
        f.write(output)

    wandb.finish()
    return output