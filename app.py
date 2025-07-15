# app.py

import streamlit as st
import os
import re
from agents.roles import Cardiologist, Psychologist, Pulmonologist, MultidisciplinaryTeam

# Utility: Extract patient name from uploaded text
def extract_patient_name(text):
    match = re.search(r"Name:\s*(.*)", text)
    if match:
        return match.group(1).strip().replace(" ", "_")
    return "Unknown_Patient"

# Title
st.title("🩺 Medical Report Analyzer")
st.write("Upload a `.txt` medical report and receive insights from medical specialists.")

# File uploader
uploaded_file = st.file_uploader("Upload medical report (.txt)", type=["txt"])

if uploaded_file is not None:
    medical_report = uploaded_file.read().decode("utf-8")

    # Display original report
    with st.expander("📄 View Uploaded Report"):
        st.text(medical_report)

    if st.button("🧠 Analyze Report"):
        with st.spinner("Analyzing with all specialists..."):

            # Extract patient name
            patient_name = extract_patient_name(medical_report)

            # Run specialist agents
            cardiologist = Cardiologist(medical_report)
            psychologist = Psychologist(medical_report)
            pulmonologist = Pulmonologist(medical_report)

            cardio_result = cardiologist.run()
            psych_result = psychologist.run()
            pulmo_result = pulmonologist.run()

            mdt = MultidisciplinaryTeam(
                cardiologist_report=cardio_result,
                psychologist_report=psych_result,
                pulmonologist_report=pulmo_result
            )
            mdt_result = mdt.run()

            # Save results to results folder
            os.makedirs("results", exist_ok=True)
            output_path = os.path.join("results", f"{patient_name}.txt")
            with open(output_path, "w") as out:
                out.write(f"🔍 Cardiologist Report:\n{cardio_result}\n\n")
                out.write(f"🧠 Psychologist Report:\n{psych_result}\n\n")
                out.write(f"🫁 Pulmonologist Report:\n{pulmo_result}\n\n")
                out.write(f"🧑‍⚕️ Multidisciplinary Team Diagnosis:\n{mdt_result}\n")

        # Display results in UI
        st.success("✅ Analysis complete!")
        st.subheader("🩺 Results")
        st.markdown("### 🔍 Cardiologist Report")
        st.write(cardio_result)

        st.markdown("### 🧠 Psychologist Report")
        st.write(psych_result)

        st.markdown("### 🫁 Pulmonologist Report")
        st.write(pulmo_result)

        st.markdown("### 🧑‍⚕️ Multidisciplinary Team Diagnosis")
        st.write(mdt_result)

        st.info(f"Results saved as: `results/{patient_name}.txt`")
