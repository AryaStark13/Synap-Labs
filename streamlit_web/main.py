import streamlit as st
import json
import time
from generate_prd_v1 import generate_prd_v1
from generate_prd_v2 import generate_prd_v2
from generate_prd_v3 import generate_prd_v3
from generate_prd_v3_palm import generate_prd_v3_palm


def get_prd(new_feature, new_feature_desc, prd_version):
    wandb_name = f"{new_feature}_prd_{prd_version[0]+prd_version[-1]}"
    start_time = time.time()
    if prd_version == "Version 1":
        output = generate_prd_v1(new_feature, new_feature_desc, wandb_name)

    elif prd_version == "Version 2":
        output = generate_prd_v2(new_feature, new_feature_desc, wandb_name)

    elif prd_version == "Version 3 (GPT-3.5-Turbo)":
        output = generate_prd_v3(new_feature, new_feature_desc, wandb_name)

    elif prd_version == "Version 3 (Palm)":
        output = generate_prd_v3_palm(
            new_feature, new_feature_desc, wandb_name)

    end_time = time.time()
    total_time = str(int(end_time - start_time))
    return output, total_time


def main():
    feature_name_input = st.text_input(
        "Feature Name:", value="Dual Camera Activation Button")
    feature_description_input = st.text_input(
        "Feature Description:", value="Enables users to capture photos from both front and back cameras simultaneously.")

    # Create a button and check if both text input fields are not empty before enabling it
    prd_version = st.radio("Select PRD Version:",
                           ("Version 1", "Version 2", "Version 3 (GPT-3.5-Turbo)", "Version 3 (Palm)"))
    if st.button("Get PRD", disabled=not (feature_name_input and feature_description_input)):
        with st.spinner(text="Generating PRD..."):
            if 'output' not in st.session_state:
                st.session_state.output, st.session_state.total_time = get_prd(
                    new_feature=feature_name_input, new_feature_desc=feature_description_input, prd_version=prd_version)
                st.session_state.edited_output = st.session_state.output

    if 'output' in st.session_state and 'total_time' in st.session_state and 'edited_output' in st.session_state:
        st.write(f"Time taken: {st.session_state.total_time} seconds")

        st.download_button(label="Download PRD", data=st.session_state.edited_output,
                           file_name=f"{feature_name_input}_prd_{prd_version[0]+prd_version[-1]}.md", mime="text/markdown")

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
