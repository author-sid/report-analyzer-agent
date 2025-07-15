# main.py

import os
import re
from agents.roles import Cardiologist, Psychologist, Pulmonologist, MultidisciplinaryTeam

# Load report from file
REPORT_FILENAME = "michael_johnson.txt"
REPORT_PATH = os.path.join("Medical reports", REPORT_FILENAME)

with open(REPORT_PATH, "r") as file:
    medical_report = file.read()

# Extract patient name using regex
def extract_patient_name(report_text):
    match = re.search(r"Name:\s*(.*)", report_text)
    if match:
        return match.group(1).strip().replace(" ", "_")
    return "Unknown_Patient"

patient_name = extract_patient_name(medical_report)

# Run specialist agents
cardiologist = Cardiologist(medical_report)
psychologist = Psychologist(medical_report)
pulmonologist = Pulmonologist(medical_report)

cardio_result = cardiologist.run()
psych_result = psychologist.run()
pulmo_result = pulmonologist.run()

# MDT
mdt = MultidisciplinaryTeam(
    cardiologist_report=cardio_result,
    psychologist_report=psych_result,
    pulmonologist_report=pulmo_result
)
mdt_result = mdt.run()

# Ensure results folder exists
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# Save output to results/{Patient_Name}.txt
output_path = os.path.join(RESULTS_DIR, f"{patient_name}.txt")
with open(output_path, "w") as out:
    out.write(f"🔍 Cardiologist Report:\n{cardio_result}\n\n")
    out.write(f"🧠 Psychologist Report:\n{psych_result}\n\n")
    out.write(f"🫁 Pulmonologist Report:\n{pulmo_result}\n\n")
    out.write(f"🧑‍⚕️ Multidisciplinary Team Diagnosis:\n{mdt_result}\n")

print(f"\n✅ Analysis complete. Results saved to: {output_path}")
