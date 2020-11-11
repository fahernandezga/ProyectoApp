materias=['Mediciones_electromagneticas','Electricidad_y_magnetismo','Optativa_programacion_y_metodos_numericos','Optativa_estadistica_basica',
          'Calculo_de_ecuaciones_diferenciales_ordinarias','Optativa','Mecanica_analitica_I','Oscilaciones_y_ondas','Matematicas_especiales_I_para_fisica',
          'Relatividad','Experimentos_de_fisica_moderna','Mecanica_analitica_II','Electrodinamica_I','Matematicas_especiales_II_para_fisica',
          'Optativa_Electronica_e_instrumentacion','Termodinamica_modulo_experimental','Termodinamica_modulo_de_teoria','Electrodinamica_II',
          'Mecanica_Cuantica_I','Optativa_Herramientas_matematicas_y_computacionales','Introduccion_a_la_investigación_experimental_o_teorica',
          'Libre_elección_I','Libre_elección_II','Libre_elección_III','Libre_elección_IV','Libre_elección_V','Libre_elección_VII','Libre_elección_VII',
          'Libre_elección_VIII','Trabajo_de_grado']



#SEMESTRE III
Mediciones_electromagneticas=subject(3,[],['Fundamentos_de_fisica_experimental'])
Electricidad_y_magnetismo=subject(3,[],['Calculo_integral', 'Calculo_vectorial'])
Optativa_programacion_y_metodos_numericos=subject(3,[],['Algebra_lineal'])
Optativa_estadistica_basica=subject(3,['Calculo_diferencial'])
Calculo_de_ecuaciones_diferenciales_ordinarias=subject(4,['Calculo_integral'])

#SEMESTRE VI
Optativa=subject(3,[])
Mecanica_analitica_I=subject(3,['Mecanica_newtoniana'])
Oscilaciones_y_ondas=subject(3,['Mecanica_newtoniana'])
Matematicas_especiales_I_para_fisica=subject(3,['Calculo_de_ecuaciones_diferenciales_ordinarias'])
Relatividad=subject(3,['Electricidad_y_magnetismo'])

#SEMESTRE V
Experimentos_de_fisica_moderna=subject(3,['Fundamentos_de_fisica_experimental'],['Oscilaciones_y_ondas'])
Mecanica_analitica_II=subject(3,['Mecanica_Analitica I'])
Electrodinamica_I=subject(3,['Matematicas_especiales_I_para_fisica','Electricidad_y_magnetismo'])
Matematicas_especiales_II_para_fisica=subject(3,['Calculo_de_ecuaciones_diferenciales_ordinarias','Matematicas_especiales_I_para_fisica'])
Optativa_Electronica_e_instrumentacion=subject(3,['Mediciones_electromagneticas'])

#SEMESTRE VI
Termodinamica_modulo_experimental=subject(2,['Mediciones_electromagneticas'],['Termodinamica_modulo_de_teoria'])
Termodinamica_modulo_de_teoria=subject(2,['Electricidad_y_magnetismo'])
Electrodinamica_II=subject(3,['Electrodinamica_I'])
Mecanica_cuantica_I=subject(4,['Mecanica_analitica_I','Matematicas_especiales_I_para_fisica','Experimentos_de_fisica_moderna'])
Optativa_herramientas_matematicas_y_computacionales=subject(3,['Optativa_Programacion_y_metodos_numericos','Matematicas_especiales_I_para_fisica'])

#SEMESTRE IX
Introduccion_a_la_investigación_experimental_o_teorica=subject(3,[])
Libre_elección_IV=subject(4,[])
Libre_elección_V=subject(4,[])
Libre_elección_VI=subject(4,[])
Libre_elección_VII=subject(4,[])

#SEMESTRE X
Trabajo_de_grado=subject(8.[])
Libre_elección_VII=subject(4,[])
