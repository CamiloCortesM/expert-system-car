import tkinter as tk
from tkinter import ttk
from experta import *

class Diagnostico(Fact):
    problema_principal = Field(str, mandatory=True)
    problemas_secundarios = Field(list, mandatory=True)

class SistemaExperto(KnowledgeEngine):
    @Rule(Fact(motor_ruidoso="si"))
    def regla_motor_ruidoso(self):
        self.declare(Diagnostico(problema_principal="Ruidos en el motor", problemas_secundarios=["Posible problema con el sistema de escape"]))
        print("Regla 1")

    @Rule(Fact(frenos_ineficientes="si"))
    def regla_frenos_ineficientes(self):
        self.declare(Diagnostico(problema_principal="Frenos ineficientes", problemas_secundarios=["Pastillas desgastadas", "Posible fuga en el sistema de frenos"]))

    @Rule(Fact(luces_fallando="si"))
    def regla_luces_fallando(self):
        self.declare(Diagnostico(problema_principal="Luces fallando", problemas_secundarios=["Fusibles quemados", "Bombillas fundidas"]))

    @Rule(Fact(problemas_combustible="si"))
    def regla_problemas_combustible(self):
        self.declare(Diagnostico(problema_principal="Problemas con el suministro de combustible", problemas_secundarios=["Filtro de combustible obstruido", "Problemas con la bomba de combustible"]))

    @Rule(Fact(problemas_arranque="si"))
    def regla_problemas_arranque(self):
        self.declare(Diagnostico(problema_principal="Problemas en el sistema de arranque", problemas_secundarios=["Batería descargada", "Problemas con el motor de arranque"]))

class Interfaz(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Sistema Experto Automotriz")
        self.geometry("400x300")

        self.label = tk.Label(self, text="Seleccione los problemas del automóvil:")
        self.label.pack(pady=10)

        self.comboboxes = {}
        problemas = ["motor_ruidoso", "frenos_ineficientes", "luces_fallando", "problemas_combustible", "problemas_arranque"]
        for problema in problemas:
            frame = tk.Frame(self)
            frame.pack(pady=5)
            label = tk.Label(frame, text=f"{problema.capitalize().replace('_', ' ')}:")
            label.pack(side=tk.LEFT)
            combobox = ttk.Combobox(frame, values=["no", "si"], state="readonly")
            combobox.pack(side=tk.RIGHT)
            self.comboboxes[problema] = combobox

        self.diagnostico_label = tk.Label(self, text="")
        self.diagnostico_label.pack(pady=10)

        self.diagnosticar_button = tk.Button(self, text="Diagnosticar", command=self.diagnosticar)
        self.diagnosticar_button.pack(pady=10)

    def diagnosticar(self):
        problemas_seleccionados = {problema: self.comboboxes[problema].get().lower() for problema in self.comboboxes}
        engine = SistemaExperto()

        for problema, respuesta in problemas_seleccionados.items():
            engine.declare(Fact(**{problema: respuesta}))

        engine.run()

        print(engine.facts)
        hecho_diagnostico = next(reversed(engine.facts.values()), None)

        try:
            if engine.facts and hecho_diagnostico and isinstance(hecho_diagnostico, Diagnostico):
                problema_principal = hecho_diagnostico['problema_principal']
                problemas_secundarios = "\n".join(hecho_diagnostico['problemas_secundarios'])
                diagnostico = f"{problema_principal}: {problemas_secundarios}"
            else:
                diagnostico = "No se pudo diagnosticar el problema."
        except KeyError:
            diagnostico = "No se pudo diagnosticar el problema."

        self.diagnostico_label.config(text=f"Diagnóstico:\n{diagnostico}")

if __name__ == "__main__":
    app = Interfaz()
    app.mainloop()
