# agents/base_agent.py

from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama


class Agent:
    def __init__(self, medical_report=None, role=None, extra_info=None):
        self.medical_report = medical_report
        self.role = role
        self.extra_info = extra_info
        self.prompt_template = self.create_prompt_template()
        self.model = ChatOllama(model="llama3")

    def create_prompt_template(self):
        if self.role == "MultidisciplinaryTeam":
            template = """
                Act like a multidisciplinary team of healthcare professionals.
                You will receive a medical report of a patient visited by a Cardiologist, Psychologist, and Pulmonologist.
                Task: Review the patient's medical report from the Cardiologist, Psychologist, and Pulmonologist, analyze them and come up with a list of 3 possible health issues of the patient.
                Just return a list of bullet points of 3 possible health issues of the patient and for each issue provide the reason.

                Cardiologist Report: {cardiologist_report}
                Psychologist Report: {psychologist_report}
                Pulmonologist Report: {pulmonologist_report}
            """
            return PromptTemplate.from_template(template)
        else:
            templates = {
                "Cardiologist": """
                    Act like a cardiologist. You will receive a medical report of a patient.
                    Task: Review the patient's cardiac workup, including ECG, blood tests, Holter monitor results, and echocardiogram.
                    Focus: Determine if there are any subtle signs of cardiac issues that could explain the patient’s symptoms. Rule out any underlying heart conditions.
                    Recommendation: Provide guidance on any further cardiac testing or monitoring needed and suggest management strategies.
                    Medical Report: {medical_report}
                """,
                "Psychologist": """
                    Act like a psychologist. You will receive a patient's report.
                    Task: Review the patient's report and provide a psychological assessment.
                    Focus: Identify potential mental health issues such as anxiety or trauma.
                    Recommendation: Provide guidance on therapy or other mental health interventions.
                    Report: {medical_report}
                """,
                "Pulmonologist": """
                    Act like a pulmonologist. You will receive a patient's report.
                    Task: Review the patient's report and provide a pulmonary assessment.
                    Focus: Identify respiratory issues such as asthma or infections.
                    Recommendation: Suggest pulmonary tests or treatments.
                    Report: {medical_report}
                """
            }
            return PromptTemplate.from_template(templates[self.role])

    def run(self):
        print(f"{self.role} is analyzing the report...")
        try:
            if self.role == "MultidisciplinaryTeam":
                prompt = self.prompt_template.format(**self.extra_info)
            else:
                prompt = self.prompt_template.format(medical_report=self.medical_report)

            response = self.model.invoke(prompt)
            return response.content
        except Exception as e:
            print("Error:", e)
            return None
