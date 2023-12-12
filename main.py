import tkinter as tk
from tkinter import ttk
from experta import *
from rules import ExpertSystem, Diagnosis

class Interface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Sistema Experto Automotriz")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Seleccione los problemas del automóvil:")
        self.label.pack(pady=10)

        self.comboboxes = {}
        symptoms = ["motor_ruidoso", "frenos_ineficientes", "luces_fallando", "problemas_combustible", "problemas_arranque", "vibraciones_al_frenar", "pérdida_de_potencia_del_motor", "temperatura_del_motor_elevada", "ruidos_anormales_al_girar_la_dirección", "consumo_excesivo_de_combustible", "fugas_de_líquidos_bajo_el_vehículo", "desgaste_desigual_de_los_neumáticos"]
        for symptom in symptoms:
            frame = tk.Frame(self)
            frame.pack(pady=5)
            label = tk.Label(frame, text=f"{symptom.capitalize().replace('_', ' ')}:")
            label.pack(side=tk.LEFT)
            combobox = ttk.Combobox(frame, values=["no", "si"], state="readonly")
            combobox.pack(side=tk.RIGHT)
            self.comboboxes[symptom] = combobox

        self.diagnosis_label = tk.Label(self, text="")
        self.diagnosis_label.pack(pady=10)

        self.diagnose_button = tk.Button(self, text="Diagnosticar", command=self.diagnose)
        self.diagnose_button.pack(pady=10)

    def diagnose(self):
        selected_symptoms = {symptom: self.comboboxes[symptom].get().lower() for symptom in self.comboboxes}
        engine = ExpertSystem()

        for symptom, response in selected_symptoms.items():
            engine.declare(Fact(**{symptom: response}))

        engine.run()

        diagnosis_fact = next(reversed(engine.facts.values()), None)

        try:
            if engine.facts and diagnosis_fact and isinstance(diagnosis_fact, Diagnosis):
                issue = diagnosis_fact['problem']
                possible_causes = "\n".join(diagnosis_fact['possible_causes'])
                possible_solutions = "\n".join(diagnosis_fact['possible_solutions'])
                diagnosis_result = f"{issue}:\nPosibles Causas: {possible_causes}\nPosibles Soluciones: {possible_solutions}"
            else:
                diagnosis_result = "No se pudo diagnosticar el problema."
        except KeyError:
            diagnosis_result = "No se pudo diagnosticar el problema."

        self.diagnosis_label.config(text=f"Diagnóstico:\n{diagnosis_result}")

if __name__ == "__main__":
    app = Interface()
    app.mainloop()
