materias=['Mediciones_electromagneticas','Electricidad_y_magnetismo','Optativa_programacion_y_metodos_numericos','Optativa_estadistica_basica',
          'Calculo_de_ecuaciones_diferenciales_ordinarias','Optativa','Mecanica_analitica_I','Oscilaciones_y_ondas','Matematicas_especiales_I_para_fisica',
          'Relatividad','Experimentos_de_fisica_moderna','Mecanica_analitica_II','Electrodinamica_I','Matematicas_especiales_II_para_fisica',
          'Optativa_Electronica_e_instrumentacion','Termodinamica_modulo_experimental','Termodinamica_modulo_de_teoria','Electrodinamica_II',
          'Mecanica_Cuantica_I','Optativa_Herramientas_matematicas_y_computacionales','Mediciones_en_optica_y_acustica','Mecanica_estadistica',
          'Temas_de_fisica_contemporanea','Mecanica_cuantica_II','Fluidos_y_optica','Aplicaciones_de_fisica_moderna','Introduccion_al_estado_solido',
          'Introduccion_a_la_investigacion_experimental_o_teorica','Introduccion_a_la_subatomica','Libre_eleccion_II','Libre_eleccion_III','Libre_eleccion_IV',
          'Libre_eleccion_V','Libre_eleccion_VI','Libre_eleccion_VII','Trabajo_de_grado']



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


#SEMESTRE VII
Mediciones_en_optica_y_acustica=(3,['Oscilaciones_y_ondas'])
Mecanica_estadistica=(3,['Mecanica_cuantica_I','Termodinamica_modulo_de_teoria'])
Temas_de_fisica_contemporanea=(1,['Experimentos_en_fisica_moderna'])
Mecanica_cuantica_II=(3,['Mecanica_cuantica_I'])
Fluidos_y_optica=(3,['Oscilaciones_y_ondas','Calculo_vectorial'])

#SEMESTRE VIII
Aplicaciones_de_fisica_moderna=(3,,['Introduccion_al_estado_solido'])
Introduccion_al_estado_solido=(3,['Mecanica_estadistica'])
Introduccion_a_la_subatomica=(3,['Mecanica_cuantica_II'])
Libre_eleccion_II=(4,[''])
Libre_eleccion_III=(4,[''])

#SEMESTRE IX	
Introduccion_a_la_investigacion_experimental_o_teorica=subject(3,[])	
Libre_eleccion_IV=subject(4,[])	
Libre_eleccion_V=subject(4,[])	
Libre_eleccion_VI=subject(4,[])	
Libre_eleccion_VII=subject(4,[])	

#SEMESTRE X	
Trabajo_de_grado=subject(8.[])
Libre_eleccion_VII=subject(4,[])
