import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as st 
from experta import *
from PIL import Image, ImageTk
from rules import ExpertSystem, Diagnosis

class Interface(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.check_vars = {}
        self.backgroundcolor = "#fdefb0"
        self.configure(bg=self.backgroundcolor)
               
        self.title("Sistema Experto Automotriz")
        self.geometry("350x730")

        self.label = tk.Label(self, text="Seleccione los problemas del automóvil",font=("Arial", 12), bg=self.backgroundcolor)
        self.label.grid(pady=10,columnspan=2)

        self.checkboxes={}
        symptoms = ["motor_ruidoso", "frenos_ineficientes", "luces_fallando", "problemas_combustible", "problemas_arranque", "vibraciones_al_frenar", "pérdida_de_potencia_del_motor", "temperatura_del_motor_elevada", "ruidos_anormales_al_girar_la_dirección", "consumo_excesivo_de_combustible", "fugas_de_líquidos_bajo_el_vehículo", "desgaste_desigual_de_los_neumáticos"]

        style = ttk.Style(self)
        style.configure("TCheckbutton", background=self.backgroundcolor)

        for i, symptom in enumerate(symptoms, start=2):
            self.checkboxes[symptom] = tk.BooleanVar()
            
            checkbox = ttk.Checkbutton(
                self, 
                text=symptom.replace('_', ' '), 
                variable=self.checkboxes[symptom],
                style="TCheckbutton",
                takefocus=0
            )
            checkbox.grid(row=i, column=0, padx=10, pady=2, sticky=tk.W)
       
        self.text_area = st.ScrolledText(self, 
                            width = 45,  
                            height = 8,  
                            font = ("Arial", 
                                    9),
                            background=self.backgroundcolor, borderwidth=0) 
        self.text_area.grid(row=i+2, column=0, columnspan=2, pady=5)
        self.text_area.insert(tk.END, f"Resultados del diagnóstico...")
        

        self.diagnose_button = tk.Button(
            self, 
            text="Diagnosticar", 
            command=self.diagnose, 
            bg="#ff6745", 
            fg="black",   
        )
        self.diagnose_button.grid(row=i+1, column=0, columnspan=2, pady=10)
        
        
        image = Image.open("./taller-mecanica.jpg") 
        image = image.resize((350, 200))
        banner_image = ImageTk.PhotoImage(image)

        self.banner_label = tk.Label(self, image=banner_image, bg=self.backgroundcolor)
        self.banner_label.image = banner_image
        self.banner_label.grid(row=17, column=0, columnspan=2, pady=10)
                
    def diagnose(self):
        selected_symptoms_booleans = {symptom: self.checkboxes[symptom].get() for symptom in self.checkboxes}
        
        selected_symptoms = {clave: 'si' if valor else 'no' for clave, valor in selected_symptoms_booleans.items()}
        engine = ExpertSystem()
        
        for symptom, response in selected_symptoms.items():
            engine.declare(Fact(**{symptom: response}))

        engine.run()

        diagnosis_fact = next(reversed(engine.facts.values()), None)

        try:
            if engine.facts and diagnosis_fact and isinstance(diagnosis_fact, Diagnosis):
                issue = diagnosis_fact['problem']
                possible_causes = "\n - ".join(diagnosis_fact['possible_causes'])
                possible_solutions = "\n - ".join(diagnosis_fact['possible_solutions'])
                diagnosis_result = f"{issue}\nPosibles Causas: \n - {possible_causes}\n\n Posibles Soluciones:\n - {possible_solutions}"
            else:
                diagnosis_result = "No se pudo diagnosticar el problema."
        except KeyError:
            diagnosis_result = "No se pudo diagnosticar el problema."

        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, f"Resumen del diagnóstico \n{diagnosis_result}")
        

if __name__ == "__main__":
    app = Interface()
    app.mainloop()
