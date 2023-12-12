from experta import *

class Diagnosis(Fact):
    problem = Field(str, mandatory=True)
    possible_causes = Field(list, mandatory=True)
    possible_solutions = Field(list, mandatory=True)
    
class ExpertSystem(KnowledgeEngine):
    @Rule(Fact(motor_ruidoso="si"),
      Fact(frenos_ineficientes="si"),
      Fact(luces_fallando="si"),
      Fact(problemas_combustible="si"),
      NOT(Fact(problemas_arranque="si")),
      NOT(Fact(vibraciones_al_frenar="si")),
      NOT(Fact(pérdida_de_potencia_del_motor="si")),
      NOT(Fact(temperatura_del_motor_elevada="si")),
      NOT(Fact(ruidos_anormales_al_girar_la_dirección="si")),
      NOT(Fact(consumo_excesivo_de_combustible="si")),
      NOT(Fact(fugas_de_líquidos_bajo_el_vehículo="si")),
      NOT(Fact(desgaste_desigual_de_los_neumáticos="si")))
    def regla_diagnostico_22(self):
        self.declare(Diagnosis(
            problem="Problemas Multifuncionales",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas eléctricos", "Problemas con el suministro de combustible"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico", "Reemplazar el filtro de combustible"]
        ))

    # Regla para problemas con el motor, las luces, el combustible y el arranque
    @Rule(Fact(motor_ruidoso="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="si"),
        Fact(problemas_arranque="si"),
        NOT(Fact(frenos_ineficientes="si")),
        NOT(Fact(vibraciones_al_frenar="si")),
        NOT(Fact(pérdida_de_potencia_del_motor="si")),
        NOT(Fact(temperatura_del_motor_elevada="si")),
        NOT(Fact(ruidos_anormales_al_girar_la_dirección="si")),
        NOT(Fact(consumo_excesivo_de_combustible="si")),
        NOT(Fact(fugas_de_líquidos_bajo_el_vehículo="si")),
        NOT(Fact(desgaste_desigual_de_los_neumáticos="si")))
    def regla_diagnostico_23(self):
        self.declare(Diagnosis(
            problem="Problemas Multifuncionales",
            possible_causes=["Desgaste del motor", "Problemas eléctricos", "Problemas con el suministro de combustible", "Problemas de arranque"],
            possible_solutions=["Realizar cambios regulares de aceite", "Verificar y reparar el sistema eléctrico", "Reemplazar el filtro de combustible", "Recargar o reemplazar la batería"]
        ))

    # Regla para problemas con el motor, frenos, combustible y arranque
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(problemas_combustible="si"),
        Fact(problemas_arranque="si"),
        NOT(Fact(luces_fallando="si")),
        NOT(Fact(vibraciones_al_frenar="si")),
        NOT(Fact(pérdida_de_potencia_del_motor="si")),
        NOT(Fact(temperatura_del_motor_elevada="si")),
        NOT(Fact(ruidos_anormales_al_girar_la_dirección="si")),
        NOT(Fact(consumo_excesivo_de_combustible="si")),
        NOT(Fact(fugas_de_líquidos_bajo_el_vehículo="si")),
        NOT(Fact(desgaste_desigual_de_los_neumáticos="si")))
    def regla_diagnostico_24(self):
        self.declare(Diagnosis(
            problem="Problemas Multifuncionales",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas con el suministro de combustible", "Problemas de arranque"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Reemplazar el filtro de combustible", "Recargar o reemplazar la batería"]
        ))

    # Regla para problemas con el motor, frenos, luces y dirección
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(ruidos_anormales_al_girar_la_dirección="si"),
        NOT(Fact(problemas_combustible="si")),
        NOT(Fact(problemas_arranque="si")),
        NOT(Fact(vibraciones_al_frenar="si")),
        NOT(Fact(pérdida_de_potencia_del_motor="si")),
        NOT(Fact(temperatura_del_motor_elevada="si")),
        NOT(Fact(consumo_excesivo_de_combustible="si")),
        NOT(Fact(fugas_de_líquidos_bajo_el_vehículo="si")),
        NOT(Fact(desgaste_desigual_de_los_neumáticos="si")))
    def regla_diagnostico_25(self):
        self.declare(Diagnosis(
            problem="Problemas Multifuncionales",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas eléctricos", "Problemas en la dirección"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico", "Reparar la dirección asistida"]
        ))

    # Regla para problemas con el motor, las luces, el arranque y los neumáticos
    @Rule(Fact(motor_ruidoso="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_arranque="si"),
        Fact(desgaste_desigual_de_los_neumáticos="si"),
        NOT(Fact(frenos_ineficientes="si")),
        NOT(Fact(problemas_combustible="si")),
        NOT(Fact(vibraciones_al_frenar="si")),
        NOT(Fact(pérdida_de_potencia_del_motor="si")),
        NOT(Fact(temperatura_del_motor_elevada="si")),
        NOT(Fact(ruidos_anormales_al_girar_la_dirección="si")),
        NOT(Fact(consumo_excesivo_de_combustible="si")),
        NOT(Fact(fugas_de_líquidos_bajo_el_vehículo="si")))
    def regla_diagnostico_26(self):
        self.declare(Diagnosis(
            problem="Problemas Multifuncionales",
            possible_causes=["Desgaste del motor", "Problemas eléctricos", "Problemas de arranque", "Desgaste desigual de neumáticos"],
            possible_solutions=["Realizar cambios regulares de aceite", "Verificar y reparar el sistema eléctrico", "Recargar o reemplazar la batería", "Corregir la alineación"]
        ))

    # Regla para problemas con el motor, frenos, luces y escape
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_escape="si"),
        NOT(Fact(problemas_combustible="si")),
        NOT(Fact(problemas_arranque="si")),
        NOT(Fact(vibraciones_al_frenar="si")),
        NOT(Fact(pérdida_de_potencia_del_motor="si")),
        NOT(Fact(temperatura_del_motor_elevada="si")),
        NOT(Fact(ruidos_anormales_al_girar_la_dirección="si")),
        NOT(Fact(consumo_excesivo_de_combustible="si")),
        NOT(Fact(fugas_de_líquidos_bajo_el_vehículo="si")),
        NOT(Fact(desgaste_desigual_de_los_neumáticos="si")))
    def regla_diagnostico_27(self):
        self.declare(Diagnosis(
            problem="Problemas Multifuncionales",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas eléctricos", "Problemas en el sistema de escape"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico", "Reparar o reemplazar el sistema de escape"]
        ))

    # Regla para problemas con el motor, las luces, el arranque y la dirección
    @Rule(Fact(motor_ruidoso="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_arranque="si"),
        Fact(ruidos_anormales_al_girar_la_dirección="si"),
        NOT(Fact(frenos_ineficientes="si")),
        NOT(Fact(problemas_combustible="si")),
        NOT(Fact(vibraciones_al_frenar="si")),
        NOT(Fact(pérdida_de_potencia_del_motor="si")),
        NOT(Fact(temperatura_del_motor_elevada="si")),
        NOT(Fact(consumo_excesivo_de_combustible="si")),
        NOT(Fact(fugas_de_líquidos_bajo_el_vehículo="si")),
        NOT(Fact(desgaste_desigual_de_los_neumáticos="si")))
    def regla_diagnostico_28(self):
        self.declare(Diagnosis(
            problem="Problemas Multifuncionales",
            possible_causes=["Desgaste del motor", "Problemas eléctricos", "Problemas de arranque", "Problemas en la dirección"],
            possible_solutions=["Realizar cambios regulares de aceite", "Verificar y reparar el sistema eléctrico", "Recargar o reemplazar la batería", "Reparar la dirección asistida"]
        ))

    # Regla para problemas con el motor, los frenos, el arranque y los neumáticos
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(problemas_arranque="si"),
        Fact(desgaste_desigual_de_los_neumáticos="si"),
        NOT(Fact(luces_fallando="si")),
        NOT(Fact(problemas_combustible="si")),
        NOT(Fact(vibraciones_al_frenar="si")),
        NOT(Fact(pérdida_de_potencia_del_motor="si")),
        NOT(Fact(temperatura_del_motor_elevada="si")),
        NOT(Fact(ruidos_anormales_al_girar_la_dirección="si")),
        NOT(Fact(consumo_excesivo_de_combustible="si")),
        NOT(Fact(fugas_de_líquidos_bajo_el_vehículo="si")))
    def regla_diagnostico_29(self):
        self.declare(Diagnosis(
            problem="Problemas Multifuncionales",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas de arranque", "Desgaste desigual de neumáticos"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Recargar o reemplazar la batería", "Corregir la alineación"]
        ))
        
    @Rule(Fact(motor_ruidoso="no"),
          Fact(frenos_ineficientes="no"),
          Fact(luces_fallando="no"),
          Fact(problemas_combustible="no"),
          Fact(problemas_arranque="no"),
          Fact(vibraciones_al_frenar="si"),
          Fact(pérdida_de_potencia_del_motor="no"),
          Fact(temperatura_del_motor_elevada="no"),
          Fact(ruidos_anormales_al_girar_la_dirección="no"),
          Fact(consumo_excesivo_de_combustible="no"),
          Fact(fugas_de_líquidos_bajo_el_vehículo="no"),
          Fact(desgaste_desigual_de_los_neumáticos="no"))
    def regla_diagnostico_6(self):
        self.declare(Diagnosis(
            problem="Problemas en los Frenos",
            possible_causes=["Discos de freno desgastados", "Pastillas de freno gastadas"],
            possible_solutions=["Reemplazar discos de freno", "Reemplazar pastillas de freno"]
        ))
        
    @Rule(Fact(motor_ruidoso="no"),
          Fact(frenos_ineficientes="no"),
          Fact(luces_fallando="no"),
          Fact(problemas_combustible="no"),
          Fact(problemas_arranque="no"),
          Fact(vibraciones_al_frenar="no"),
          Fact(pérdida_de_potencia_del_motor="si"),
          Fact(temperatura_del_motor_elevada="no"),
          Fact(ruidos_anormales_al_girar_la_dirección="no"),
          Fact(consumo_excesivo_de_combustible="no"),
          Fact(fugas_de_líquidos_bajo_el_vehículo="no"),
          Fact(desgaste_desigual_de_los_neumáticos="no"))
    def regla_diagnostico_7(self):
        self.declare(Diagnosis(
            problem="Pérdida de Potencia del Motor",
            possible_causes=["Filtro de aire obstruido", "Problemas en el sistema de admisión de aire"],
            possible_solutions=["Reemplazar el filtro de aire", "Reparar el sistema de admisión de aire"]
        ))

    @Rule(Fact(motor_ruidoso="no"),
          Fact(frenos_ineficientes="no"),
          Fact(luces_fallando="no"),
          Fact(problemas_combustible="no"),
          Fact(problemas_arranque="no"),
          Fact(vibraciones_al_frenar="no"),
          Fact(pérdida_de_potencia_del_motor="no"),
          Fact(temperatura_del_motor_elevada="si"),
          Fact(ruidos_anormales_al_girar_la_dirección="no"),
          Fact(consumo_excesivo_de_combustible="no"),
          Fact(fugas_de_líquidos_bajo_el_vehículo="no"),
          Fact(desgaste_desigual_de_los_neumáticos="no"))
    def regla_diagnostico_8(self):
        self.declare(Diagnosis(
            problem="Temperatura del Motor Elevada",
            possible_causes=["Problemas en el sistema de enfriamiento", "Baja cantidad de refrigerante"],
            possible_solutions=["Reparar el sistema de enfriamiento", "Reemplazar o rellenar el refrigerante"]
        ))

    @Rule(Fact(motor_ruidoso="no"),
          Fact(frenos_ineficientes="no"),
          Fact(luces_fallando="no"),
          Fact(problemas_combustible="no"),
          Fact(problemas_arranque="no"),
          Fact(vibraciones_al_frenar="no"),
          Fact(pérdida_de_potencia_del_motor="no"),
          Fact(temperatura_del_motor_elevada="no"),
          Fact(ruidos_anormales_al_girar_la_dirección="si"),
          Fact(consumo_excesivo_de_combustible="no"),
          Fact(fugas_de_líquidos_bajo_el_vehículo="no"),
          Fact(desgaste_desigual_de_los_neumáticos="no"))
    def regla_diagnostico_9(self):
        self.declare(Diagnosis(
            problem="Problemas en la Dirección",
            possible_causes=["Fallos en la dirección asistida", "Problemas en la bomba de dirección"],
            possible_solutions=["Reparar la dirección asistida", "Reemplazar la bomba de dirección"]
        ))
    
    @Rule(Fact(motor_ruidoso="no"),
          Fact(frenos_ineficientes="no"),
          Fact(luces_fallando="no"),
          Fact(problemas_combustible="no"),
          Fact(problemas_arranque="no"),
          Fact(vibraciones_al_frenar="no"),
          Fact(pérdida_de_potencia_del_motor="no"),
          Fact(temperatura_del_motor_elevada="no"),
          Fact(ruidos_anormales_al_girar_la_dirección="no"),
          Fact(consumo_excesivo_de_combustible="si"),
          Fact(fugas_de_líquidos_bajo_el_vehículo="no"),
          Fact(desgaste_desigual_de_los_neumáticos="no"))
    def regla_diagnostico_10(self):
        self.declare(Diagnosis(
            problem="Consumo Excesivo de Combustible",
            possible_causes=["Filtro de aire sucio", "Sonda de oxígeno defectuosa"],
            possible_solutions=["Reemplazar el filtro de aire", "Reemplazar la sonda de oxígeno"]
        ))

    @Rule(Fact(motor_ruidoso="no"),
          Fact(frenos_ineficientes="no"),
          Fact(luces_fallando="no"),
          Fact(problemas_combustible="no"),
          Fact(problemas_arranque="no"),
          Fact(vibraciones_al_frenar="no"),
          Fact(pérdida_de_potencia_del_motor="no"),
          Fact(temperatura_del_motor_elevada="no"),
          Fact(ruidos_anormales_al_girar_la_dirección="no"),
          Fact(consumo_excesivo_de_combustible="no"),
          Fact(fugas_de_líquidos_bajo_el_vehículo="si"),
          Fact(desgaste_desigual_de_los_neumáticos="no"))
    def regla_diagnostico_11(self):
        self.declare(Diagnosis(
            problem="Fugas de Líquidos",
            possible_causes=["Fugas en el sistema de refrigeración", "Fugas en el sistema de frenos"],
            possible_solutions=["Reparar las fugas en el sistema de refrigeración", "Reparar las fugas en el sistema de frenos"]
        ))

    @Rule(Fact(motor_ruidoso="no"),
          Fact(frenos_ineficientes="no"),
          Fact(luces_fallando="no"),
          Fact(problemas_combustible="no"),
          Fact(problemas_arranque="no"),
          Fact(vibraciones_al_frenar="no"),
          Fact(pérdida_de_potencia_del_motor="no"),
          Fact(temperatura_del_motor_elevada="no"),
          Fact(ruidos_anormales_al_girar_la_dirección="no"),
          Fact(consumo_excesivo_de_combustible="no"),
          Fact(fugas_de_líquidos_bajo_el_vehículo="no"),
          Fact(desgaste_desigual_de_los_neumáticos="si"))
    def regla_diagnostico_12(self):
        self.declare(Diagnosis(
            problem="Desgaste Desigual de Neumáticos",
            possible_causes=["Problemas de alineación", "Presión incorrecta de los neumáticos"],
            possible_solutions=["Corregir la alineación", "Ajustar la presión de los neumáticos"]
        ))
     
        # Regla para problemas con el motor, frenos y luces
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="no"))
    def regla_diagnostico_31(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas eléctricos"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico"]
        ))

    # Regla para problemas con el motor, luces y combustible
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="no"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="si"))
    def regla_diagnostico_32(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Problemas eléctricos", "Problemas con el suministro de combustible"],
            possible_solutions=["Realizar cambios regulares de aceite", "Verificar y reparar el sistema eléctrico", "Reemplazar el filtro de combustible"]
        ))

    # Regla para problemas con el motor, frenos y combustible
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="no"),
        Fact(problemas_combustible="si"))
    def regla_diagnostico_33(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas con el suministro de combustible"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Reemplazar el filtro de combustible"]
        ))

    # Regla para problemas con el motor, luces y arranque
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="no"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="no"))
    def regla_diagnostico_34(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Problemas eléctricos", "Problemas de arranque"],
            possible_solutions=["Realizar cambios regulares de aceite", "Verificar y reparar el sistema eléctrico", "Recargar o reemplazar la batería"]
        ))

    # Regla para problemas con el motor, combustible y arranque
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="no"),
        Fact(luces_fallando="no"),
        Fact(problemas_combustible="si"))
    def regla_diagnostico_35(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Problemas con el suministro de combustible", "Problemas de arranque"],
            possible_solutions=["Realizar cambios regulares de aceite", "Reemplazar el filtro de combustible", "Recargar o reemplazar la batería"]
        ))

    # Regla para problemas con los frenos, luces y combustible
    @Rule(Fact(motor_ruidoso="no"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="si"))
    def regla_diagnostico_36(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste de las pastillas de freno", "Problemas eléctricos", "Problemas con el suministro de combustible"],
            possible_solutions=["Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico", "Reemplazar el filtro de combustible"]
        ))

    # Regla para problemas con los frenos, luces y arranque
    @Rule(Fact(motor_ruidoso="no"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="no"))
    def regla_diagnostico_37(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste de las pastillas de freno", "Problemas eléctricos", "Problemas de arranque"],
            possible_solutions=["Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico", "Recargar o reemplazar la batería"]
        ))

    # Regla para problemas con los frenos, combustible y arranque
    @Rule(Fact(motor_ruidoso="no"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="no"),
        Fact(problemas_combustible="si"))
    def regla_diagnostico_38(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste de las pastillas de freno", "Problemas con el suministro de combustible", "Problemas de arranque"],
            possible_solutions=["Evitar frenados bruscos", "Reemplazar el filtro de combustible", "Recargar o reemplazar la batería"]
        ))

    # Regla para problemas con las luces, combustible y arranque
    @Rule(Fact(motor_ruidoso="no"),
        Fact(frenos_ineficientes="no"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="si"))
    def regla_diagnostico_39(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Problemas eléctricos", "Problemas con el suministro de combustible", "Problemas de arranque"],
            possible_solutions=["Verificar y reparar el sistema eléctrico", "Reemplazar el filtro de combustible", "Recargar o reemplazar la batería"]
        ))

    # Regla para problemas con los frenos, luces y dirección
    @Rule(Fact(motor_ruidoso="no"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(ruidos_anormales_al_girar_la_dirección="si"))
    def regla_diagnostico_40(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste de las pastillas de freno", "Problemas eléctricos", "Fallos en la dirección asistida"],
            possible_solutions=["Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico", "Reparar la dirección asistida"]
        ))   
        # Regla para problemas en el motor, frenos, luces, combustible y arranque
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="si"),
        Fact(problemas_arranque="si"))
    def regla_diagnostico_13(self):
        self.declare(Diagnosis(
            problem="Problemas Multifuncionales",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas eléctricos", "Problemas con el suministro de combustible", "Problemas de arranque"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico", "Reemplazar fusibles defectuosos", "Reparar o reemplazar la bomba de combustible", "Recargar o reemplazar la batería"]
        ))

    # Regla para problemas con el suministro de combustible, arranque, dirección, escape y neumáticos
    @Rule(Fact(problemas_combustible="si"),
        Fact(problemas_arranque="si"),
        Fact(ruidos_anormales_al_girar_la_dirección="si"),
        Fact(problemas_escape="si"),
        Fact(desgaste_desigual_de_los_neumáticos="si"))
    def regla_diagnostico_14(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Problemas con el suministro de combustible", "Problemas de arranque", "Problemas en la dirección", "Problemas en el sistema de escape", "Desgaste desigual de neumáticos"],
            possible_solutions=["Reemplazar el filtro de combustible", "Reparar o reemplazar la bomba de combustible", "Recargar o reemplazar la batería", "Reparar la dirección asistida", "Reparar o reemplazar el sistema de escape", "Corregir la alineación"]
        ))

    # Regla para problemas con el motor, las luces, la dirección, el escape y los neumáticos
    @Rule(Fact(motor_ruidoso="si"),
        Fact(luces_fallando="si"),
        Fact(ruidos_anormales_al_girar_la_dirección="si"),
        Fact(problemas_escape="si"),
        Fact(desgaste_desigual_de_los_neumáticos="si"))
    def regla_diagnostico_15(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Problemas eléctricos", "Problemas en la dirección", "Problemas en el sistema de escape", "Desgaste desigual de neumáticos"],
            possible_solutions=["Realizar cambios regulares de aceite", "Verificar y reparar el sistema eléctrico", "Reparar la dirección asistida", "Reparar o reemplazar el sistema de escape", "Corregir la alineación"]
        ))

    # Regla para problemas con el motor, frenos, luces, escape y neumáticos
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_escape="si"),
        Fact(desgaste_desigual_de_los_neumáticos="si"))
    def regla_diagnostico_16(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas eléctricos", "Problemas en el sistema de escape", "Desgaste desigual de neumáticos"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico", "Reparar o reemplazar el sistema de escape", "Corregir la alineación"]
        ))

    # Regla para problemas con el motor, las luces, el combustible, la dirección y los neumáticos
    @Rule(Fact(motor_ruidoso="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="si"),
        Fact(ruidos_anormales_al_girar_la_dirección="si"),
        Fact(desgaste_desigual_de_los_neumáticos="si"))
    def regla_diagnostico_17(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Problemas eléctricos", "Problemas con el suministro de combustible", "Problemas en la dirección", "Desgaste desigual de neumáticos"],
            possible_solutions=["Realizar cambios regulares de aceite", "Verificar y reparar el sistema eléctrico", "Reemplazar el filtro de combustible", "Reparar la dirección asistida", "Corregir la alineación"]
        ))

    # Regla para problemas con el motor, los frenos, las luces, el combustible y los neumáticos
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="si"),
        Fact(desgaste_desigual_de_los_neumáticos="si"))
    def regla_diagnostico_18(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas eléctricos", "Problemas con el suministro de combustible", "Desgaste desigual de neumáticos"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico", "Reemplazar el filtro de combustible", "Corregir la alineación"]
        ))

    # Regla para problemas con el motor, los frenos, la dirección, el arranque y los neumáticos
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(ruidos_anormales_al_girar_la_dirección="si"),
        Fact(problemas_arranque="si"),
        Fact(desgaste_desigual_de_los_neumáticos="si"))
    def regla_diagnostico_19(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas en la dirección", "Problemas de arranque", "Desgaste desigual de neumáticos"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Reparar la dirección asistida", "Recargar o reemplazar la batería", "Corregir la alineación"]
        ))

    # Regla para problemas con el motor, los frenos, las luces, el arranque y los neumáticos
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_arranque="si"),
        Fact(desgaste_desigual_de_los_neumáticos="si"))
    def regla_diagnostico_20(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas eléctricos", "Problemas de arranque", "Desgaste desigual de neumáticos"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico", "Recargar o reemplazar la batería", "Corregir la alineación"]
        ))

    # Regla para problemas con el motor, los frenos, las luces, el escape y el arranque
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_escape="si"),
        Fact(problemas_arranque="si"))
    def regla_diagnostico_21(self):
        self.declare(Diagnosis(
            problem="Problemas Múltiples",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno", "Problemas eléctricos", "Problemas en el sistema de escape", "Problemas de arranque"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico", "Reparar o reemplazar el sistema de escape", "Recargar o reemplazar la batería"]
        ))
        
    @Rule(Fact(motor_ruidoso="si"),
          Fact(frenos_ineficientes="no"),
          Fact(luces_fallando="no"),
          Fact(problemas_combustible="no"),
          Fact(problemas_arranque="no"))
    def regla_motor_ruidoso(self):
        self.declare(Diagnosis(
            problem="Desgaste del Motor",
            possible_causes=["Falta de cambio regular de aceite", "Uso excesivo"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar condiciones de manejo extremas"]
        ))

    @Rule(Fact(motor_ruidoso="no"),
          Fact(frenos_ineficientes="si"),
          Fact(luces_fallando="no"),
          Fact(problemas_combustible="no"),
          Fact(problemas_arranque="no"))
    def regla_diagnostico_2(self):
        self.declare(Diagnosis(
            problem="Desgaste de las Pastillas de Freno",
            possible_causes=["Frenado brusco frecuente", "Uso excesivo"],
            possible_solutions=["Evitar frenados bruscos", "Utilizar pastillas de freno de alta calidad"]
        ))


    @Rule(Fact(motor_ruidoso="no"),
          Fact(frenos_ineficientes="no"),
          Fact(luces_fallando="si"),
          Fact(problemas_combustible="no"),
          Fact(problemas_arranque="no"))
    def regla_diagnostico_3(self):
        self.declare(Diagnosis(
            problem="Problemas Eléctricos",
            possible_causes=["Problemas en el sistema eléctrico", "Fusibles quemados"],
            possible_solutions=["Verificar y reparar el sistema eléctrico", "Reemplazar fusibles defectuosos"]
        ))

    @Rule(Fact(motor_ruidoso="no"),
          Fact(frenos_ineficientes="no"),
          Fact(luces_fallando="no"),
          Fact(problemas_combustible="si"),
          Fact(problemas_arranque="no"))
    def regla_diagnostico_4(self):
        self.declare(Diagnosis(
            problem="Problemas con el Suministro de Combustible",
            possible_causes=["Filtro de combustible obstruido", "Problemas con la bomba de combustible"],
            possible_solutions=["Reemplazar el filtro de combustible", "Reparar o reemplazar la bomba de combustible"]
        ))
        
    @Rule(Fact(motor_ruidoso="no"),
          Fact(frenos_ineficientes="no"),
          Fact(luces_fallando="no"),
          Fact(problemas_combustible="no"),
          Fact(problemas_arranque="si"))
    def regla_diagnostico_5(self):
        self.declare(Diagnosis(
            problem="Problemas de Arranque",
            possible_causes=["Batería descargada", "Problemas con el motor de arranque"],
            possible_solutions=["Recargar o reemplazar la batería", "Reparar o reemplazar el motor de arranque"]
        ))
    
        # Regla para problemas con el motor y los frenos
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="no"),
        Fact(problemas_combustible="no"))
    def regla_diagnostico_41(self):
        self.declare(Diagnosis(
            problem="Problemas Duales",
            possible_causes=["Desgaste del motor", "Desgaste de las pastillas de freno"],
            possible_solutions=["Realizar cambios regulares de aceite", "Evitar frenados bruscos"]
        ))

    # Regla para problemas con el motor y las luces
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="no"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="no"))
    def regla_diagnostico_42(self):
        self.declare(Diagnosis(
            problem="Problemas Duales",
            possible_causes=["Desgaste del motor", "Problemas eléctricos"],
            possible_solutions=["Realizar cambios regulares de aceite", "Verificar y reparar el sistema eléctrico"]
        ))

    # Regla para problemas con el motor y el combustible
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="no"),
        Fact(luces_fallando="no"),
        Fact(problemas_combustible="si"))
    def regla_diagnostico_43(self):
        self.declare(Diagnosis(
            problem="Problemas Duales",
            possible_causes=["Desgaste del motor", "Problemas con el suministro de combustible"],
            possible_solutions=["Realizar cambios regulares de aceite", "Reemplazar el filtro de combustible"]
        ))

    # Regla para problemas con el motor y el arranque
    @Rule(Fact(motor_ruidoso="si"),
        Fact(frenos_ineficientes="no"),
        Fact(luces_fallando="no"),
        Fact(problemas_combustible="no"),
        Fact(problemas_arranque="si"))
    def regla_diagnostico_44(self):
        self.declare(Diagnosis(
            problem="Problemas Duales",
            possible_causes=["Desgaste del motor", "Problemas de arranque"],
            possible_solutions=["Realizar cambios regulares de aceite", "Recargar o reemplazar la batería"]
        ))

    # Regla para problemas con los frenos y las luces
    @Rule(Fact(motor_ruidoso="no"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="no"))
    def regla_diagnostico_45(self):
        self.declare(Diagnosis(
            problem="Problemas Duales",
            possible_causes=["Desgaste de las pastillas de freno", "Problemas eléctricos"],
            possible_solutions=["Evitar frenados bruscos", "Verificar y reparar el sistema eléctrico"]
        ))

    # Regla para problemas con los frenos y el combustible
    @Rule(Fact(motor_ruidoso="no"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="no"),
        Fact(problemas_combustible="si"))
    def regla_diagnostico_46(self):
        self.declare(Diagnosis(
            problem="Problemas Duales",
            possible_causes=["Desgaste de las pastillas de freno", "Problemas con el suministro de combustible"],
            possible_solutions=["Evitar frenados bruscos", "Reemplazar el filtro de combustible"]
        ))

    # Regla para problemas con los frenos y el arranque
    @Rule(Fact(motor_ruidoso="no"),
        Fact(frenos_ineficientes="si"),
        Fact(luces_fallando="no"),
        Fact(problemas_combustible="no"),
        Fact(problemas_arranque="si"))
    def regla_diagnostico_47(self):
        self.declare(Diagnosis(
            problem="Problemas Duales",
            possible_causes=["Desgaste de las pastillas de freno", "Problemas de arranque"],
            possible_solutions=["Evitar frenados bruscos", "Recargar o reemplazar la batería"]
        ))

    # Regla para problemas con las luces y el combustible
    @Rule(Fact(motor_ruidoso="no"),
        Fact(frenos_ineficientes="no"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="si"))
    def regla_diagnostico_48(self):
        self.declare(Diagnosis(
            problem="Problemas Duales",
            possible_causes=["Problemas eléctricos", "Problemas con el suministro de combustible"],
            possible_solutions=["Verificar y reparar el sistema eléctrico", "Reemplazar el filtro de combustible"]
        ))

    # Regla para problemas con las luces y el arranque
    @Rule(Fact(motor_ruidoso="no"),
        Fact(frenos_ineficientes="no"),
        Fact(luces_fallando="si"),
        Fact(problemas_combustible="no"),
        Fact(problemas_arranque="si"))
    def regla_diagnostico_49(self):
        self.declare(Diagnosis(
            problem="Problemas Duales",
            possible_causes=["Problemas eléctricos", "Problemas de arranque"],
            possible_solutions=["Verificar y reparar el sistema eléctrico", "Recargar o reemplazar la batería"]
        ))

    # Regla para problemas con el combustible y el arranque
    @Rule(Fact(motor_ruidoso="no"),
        Fact(frenos_ineficientes="no"),
        Fact(luces_fallando="no"),
        Fact(problemas_combustible="si"),
        Fact(problemas_arranque="si"))
    def regla_diagnostico_50(self):
        self.declare(Diagnosis(
            problem="Problemas Duales",
            possible_causes=["Problemas con el suministro de combustible", "Problemas de arranque"],
            possible_solutions=["Reemplazar el filtro de combustible", "Recargar o reemplazar la batería"]
        ))
