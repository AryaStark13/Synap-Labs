import streamlit as st
import json
import time
from generate_prd import generate_prd
from generate_prd_v2 import generate_prd_v2


def get_prd(company_name, company_desc, existing_feature_list, new_feature, new_feature_desc, prd_version):
    wandb_name = f"{company_name}_prd_{new_feature}"
    start_time = time.time()
    if prd_version == "Version 1":
        output = generate_prd(company_name, company_desc, existing_feature_list,
                              new_feature, new_feature_desc, wandb_name)
    else:
        output = generate_prd_v2(company_name, company_desc, existing_feature_list,
                                 new_feature, new_feature_desc, wandb_name)

    end_time = time.time()
    total_time = str(int(end_time - start_time))
    return output, total_time

def get_company_info(company_name):
    with open("streamlit_web/company_info.json", "r") as f: # For deployment
    # with open("./company_info.json", "r") as f: # For local testing
        company_info = json.load(f)[company_name]

    return company_info


def main():
    dropdown_to_company_name = {
        "Weights and Biases": "wandb",
        "Langchain": "langchain",
    }
    # Create a dropdown selectbox
    dropdown_select = st.selectbox(
        "Select a Company:", ("Weights and Biases", "Langchain", "Other"))

    if dropdown_select == "Other":
        company_info = {
            "company_name": st.text_input("Company Name:"),
            "company_desc": st.text_input("Company Description:"),
            "existing_feature_list": st.text_area("Existing Feature List:"),
        }
        company_name = company_info["company_name"]
    else:
        company_name = dropdown_to_company_name[dropdown_select]
        company_info = get_company_info(company_name)

    # Create text input fields for feature name and description
    feature_name_input = st.text_input(
        "Feature Name:", value="Model Explainability Toolkit (MXT)")
    feature_description_input = st.text_input(
        "Feature Description:", value="Enables users to interpret and explain the outputs and decision-making of their AI Models.")

    # Create a button and check if both text input fields are not empty before enabling it
    prd_version = st.radio("Select PRD Version:", ("Version 1", "Version 2"))
    if st.button("Get PRD", disabled=not (feature_name_input and feature_description_input)):
        with st.spinner(text="Generating PRD..."):
            if 'output' not in st.session_state:
                st.session_state.output, st.session_state.total_time = get_prd(**company_info, new_feature=feature_name_input,
                                                                               new_feature_desc=feature_description_input, prd_version=prd_version)
                st.session_state.edited_output = st.session_state.output

    if 'output' in st.session_state and 'total_time' in st.session_state and 'edited_output' in st.session_state:
        st.write(f"Time taken: {st.session_state.total_time} seconds")

        st.download_button(label="Download PRD", data=st.session_state.edited_output,
                           file_name=f"{company_name}_prd_{feature_name_input}.md", mime="text/markdown")

        if st.button("Edit PRD"):
            pass

        if not st.button("Finish Editing"):
            col1, col2 = st.columns(2)

            with col1:
                st.text("Markdown Editor")
                st.session_state.edited_output = st.text_area(
                    label="Markdown Editor", value=st.session_state.output, height=500, label_visibility="hidden")
            with col2:
                st.text("Live Preview")
                st.markdown(st.session_state.edited_output,
                            help="Generated PRD")

            st.session_state.output = st.session_state.edited_output

        st.markdown(st.session_state.edited_output, help="Generated PRD")


if __name__ == "__main__":
    main()
