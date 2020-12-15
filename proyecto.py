materias=['Fundamentos_de_fisica_experimental','Fundamentos_de_fisica_teorica','Calculo_diferencial_en_una_variable','Taller_de_matematicas_y_ciencias','Algebra_lineal_basica',
          'Libre_eleccion_I','Mediciones_mecanicas','Mecanica_newtoniana','Calculo_integral_en_una_variable','Calculo_vectorial','Optativa_formación_integral_y_humanistica',
          'Mediciones_electromagneticas','Electricidad_y_magnetismo','Optativa_programacion_y_metodos_numericos','Optativa_estadistica_basica',
          'Calculo_de_ecuaciones_diferenciales_ordinarias','Optativa_formacion_integral_y_humanistica','Mecanica_analitica_I','Oscilaciones_y_ondas','Matematicas_especiales_I_para_fisica',
          'Relatividad','Experimentos_de_fisica_moderna','Mecanica_analitica_II','Electrodinamica_I','Matematicas_especiales_II_para_fisica',
          'Optativa_Electronica_e_instrumentacion','Termodinamica_modulo_experimental','Termodinamica_modulo_de_teoria','Electrodinamica_II',
          'Mecanica_cuantica_I','Optativa_Herramientas_matematicas_y_computacionales','Mediciones_en_optica_y_acustica','Mecanica_estadistica',
          'Temas_de_fisica_contemporanea','Mecanica_cuantica_II','Fluidos_y_optica','Aplicaciones_de_fisica_moderna','Introduccion_al_estado_solido',
          'Introduccion_a_la_investigacion_experimental_o_teorica','Introduccion_a_la_subatomica','Libre_eleccion_II','Libre_eleccion_III','Libre_eleccion_IV',
          'Libre_eleccion_V','Libre_eleccion_VI','Libre_eleccion_VII','Trabajo_de_grado','Libre_eleccion_VIII']

class subject:
    def __init__(self, creditos, lista_de_prerrequisitos, lista_de_correquisitos=[]):
        self.creditos=creditos
        self.lista1=lista_de_prerrequisitos
        self.lista2=lista_de_correquisitos


#SEMESTRE I
Calculo_diferencial_en_una_variable=subject("Calculo_diferencial_en_una_variable",4)
Fundamentos_de_fisica_teorica=subject("Fundamentos_de_fisica_teorica",3)
Algebra_lineal_basica=subject("Algebra_lineal_basica",4)
Taller_de_matematicas_y_ciencias=subject("Taller_de_matematicas_y_ciencias",3)
Fundamentos_de_fisica_experimental=subject("Fundamentos_de_fisica_experimental",3)
Libre_eleccion_I=subject("Libre_eleccion_I",4)

#SEMESTRE II
Mediciones_mecanicas=subject("Mediciones_mecanicas",3, ['Fundamentos_de_fisica_experimental'])
Mecanica_newtoniana=subject("Mecanica_newtoniana",4, ['Fundamentos_de_fisica_teorica'])
Calculo_integral_en_una_variable=subject("Calculo_integral_en_una_variable",4, ['Calculo_diferencial_en_una_variable'])
Calculo_vectorial=subject("Calculo_vectorial",4, ['Calculo_integral_en_una_variable'])
Optativa_formación_integral_y_humanistica=subject("Optativa_formación_integral_y_humanistica",3)

#SEMESTRE III
Mediciones_electromagneticas=subject("Mediciones_electromagneticas",3,['Fundamentos_de_fisica_experimental'])
Electricidad_y_magnetismo=subject("Electricidad_y_magnetismo",3,['Calculo_integral_en_una_variable', 'Calculo_vectorial'])
Optativa_programacion_y_metodos_numericos=subject("Optativa_programacion_y_metodos_numericos",3,[],['Algebra_lineal_basica'])
Optativa_estadistica_basica=subject("Optativa_estadistica_basica",3,['Calculo_diferencial_en_una_variable'])
Calculo_de_ecuaciones_diferenciales_ordinarias=subject("Calculo_de_ecuaciones_diferenciales_ordinarias",4,['Calculo_integral_en_una_variable'])

#SEMESTRE IV
Optativa_formacion_integral_y_humanistica=subject("Optativa_formacion_integral_y_humanistica",3,[])
Mecanica_analitica_I=subject("Mecanica_analitica_I",3,['Mecanica_newtoniana'])
Oscilaciones_y_ondas=subject("Oscilaciones_y_ondas",3,['Mecanica_newtoniana'])
Matematicas_especiales_I_para_fisica=subject("Matematicas_especiales_I_para_fisica",3,['Calculo_de_ecuaciones_diferenciales_ordinarias'])
Relatividad=subject("Relatividad",3,['Electricidad_y_magnetismo'])

#SEMESTRE V
Experimentos_de_fisica_moderna=subject("Experimentos_de_fisica_moderna",3,['Fundamentos_de_fisica_experimental','Oscilaciones_y_ondas'])
Mecanica_analitica_II=subject("Mecanica_analitica_II",3,['Mecanica_analitica_I'])
Electrodinamica_I=subject("Electrodinamica_I",3,['Matematicas_especiales_I_para_fisica','Electricidad_y_magnetismo'])
Matematicas_especiales_II_para_fisica=subject("Matematicas_especiales_II_para_fisica",3,['Calculo_de_ecuaciones_diferenciales_ordinarias','Matematicas_especiales_I_para_fisica'])
Optativa_Electronica_e_instrumentacion=subject("Optativa_Electronica_e_instrumentacion",3,['Mediciones_electromagneticas'])

#SEMESTRE VI
Termodinamica_modulo_de_teoria=subject("Termodinamica_modulo_de_teoria",2,['Electricidad_y_magnetismo'])
Termodinamica_modulo_experimental=subject("Termodinamica_modulo_experimental",2,['Mediciones_electromagneticas','Termodinamica_modulo_de_teoria'])
Electrodinamica_II=subject("Electrodinamica_II",3,['Electrodinamica_I'])
Mecanica_cuantica_I=subject("Mecanica_cuantica_I",4,['Mecanica_analitica_I','Matematicas_especiales_I_para_fisica','Experimentos_de_fisica_moderna'])
Optativa_Herramientas_matematicas_y_computacionales=subject("Optativa_Herramientas_matematicas_y_computacionales",3,['Optativa_programacion_y_metodos_numericos','Matematicas_especiales_I_para_fisica'])

#SEMESTRE VII
Mediciones_en_optica_y_acustica=subject("Mediciones_en_optica_y_acustica",3,['Oscilaciones_y_ondas'])
Mecanica_estadistica=subject("Mecanica_estadistica",3,['Mecanica_cuantica_I','Termodinamica_modulo_de_teoria'])
Temas_de_fisica_contemporanea=subject("Temas_de_fisica_contemporanea",1,['Experimentos_de_fisica_moderna'])
Mecanica_cuantica_II=subject("Mecanica_cuantica_II",3,['Mecanica_cuantica_I'])
Fluidos_y_optica=subject("Fluidos_y_optica",3,['Oscilaciones_y_ondas','Calculo_vectorial'])

#SEMESTRE VIII

Introduccion_al_estado_solido=subject("Introduccion_al_estado_solido",3,['Mecanica_estadistica'])
Aplicaciones_de_fisica_moderna=subject("Aplicaciones_de_fisica_moderna",3,['Introduccion_al_estado_solido'])
Introduccion_a_la_subatomica=subject("Introduccion_a_la_subatomica",3,['Mecanica_cuantica_II'])
Libre_eleccion_II=subject("Libre_eleccion_II",4,[])
Libre_eleccion_III=subject("Libre_eleccion_III",4,[])

#SEMESTRE IX	
Introduccion_a_la_investigacion_experimental_o_teorica=subject("Introduccion_a_la_investigacion_experimental_o_teorica",3,[])	
Libre_eleccion_IV=subject("Libre_eleccion_IV",4,[])	
Libre_eleccion_V=subject("Libre_eleccion_V",4,[])	
Libre_eleccion_VI=subject("Libre_eleccion_VI",4,[])	
Libre_eleccion_VII=subject("Libre_eleccion_VII",4,[])	

#SEMESTRE X	
Trabajo_de_grado=subject("Trabajo_de_grado",8,[])
Libre_eleccion_VIII=subject("Libre_eleccion_VIII",4,[])

#-------------------------------------------------

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.storage.jsonstore import JsonStore
from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock


Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Mi pensum'
            on_press: root.manager.current = 'pensum'
            background_color:(100,53,0,0)
        Button:
            text: 'Salud Mental'
            on_press: root.manager.current = 'saludmental'
            background_color:(100,53,0,20)
            
<Pensum>:
    BoxLayout:
       
        Button:
            text: 'Devolver'
            on_press: root.manager.current = 'menu'
            pos_hint: {'x': 2, 'y': 0}
            background_color: (155,0,51,53)
            
<SaludMental>:
    BoxLayout:
       
        Button:
            text: 'Devolver'
            on_press: root.manager.current = 'menu'
            pos_hint: {'x': 2, 'y': 0}
            background_color: (155,0,51,53)
            size_hint: (None, None)
            size: (100, 50)
""") 

class SaludMental(GridLayout, Screen):
    def __init__(self, **kwargs): 
        # super function can be used to gain access  
        # to inherited methods from a parent or sibling class  
        # that has been overwritten in a class object.  
        super(SaludMental, self).__init__(**kwargs) 
        self.cols = 1
        
        self.seleccione = Label(text = "¿Sobre qué categoría le gustaría informarse?")
        self.add_widget(self.seleccione)
        
        self.Metodosdeestudio = Button(text="Métodos de estudio", background_color=(0,155,0,53))
        self.Metodosdeestudio.bind(on_press=self.btnestudio)
        self.add_widget(self.Metodosdeestudio)
        
        self.Ejerciciofisico = Button(text="Ejercicio Físico", background_color=(0,155,0,53))
        self.Ejerciciofisico.bind(on_press=self.btnejercicio)
        self.add_widget(self.Ejerciciofisico)
        
        self.Alimentacion = Button(text="Alimentacion", background_color=(0,155,0,53))
        self.Alimentacion.bind(on_press=self.btnalimentacion)
        self.add_widget(self.Alimentacion)
        
        self.Relacionessociales = Button(text="Relaciones Sociales", background_color=(0,155,0,53))
        self.Relacionessociales.bind(on_press=self.btnrelaciones)
        self.add_widget(self.Relacionessociales)
        
        self.Relajacion = Button(text="Relajación", background_color=(0,155,0,53))
        self.Relajacion.bind(on_press=self.btnrelajacion)
        self.add_widget(self.Relajacion)
        
        self.Sueño = Button(text="Sueño", background_color=(0,155,0,53))
        self.Sueño.bind(on_press=self.btnSueño)
        self.add_widget(self.Sueño)
          
        self.RegistrodeAnimo = Button(text="Registro de Animo", background_color=(0,155,0,53))
        self.RegistrodeAnimo.bind(on_press=self.btnAnimo)
        self.add_widget(self.RegistrodeAnimo)
        
    def btnestudio(self, button): 
          
        layout = GridLayout(cols = 1) 
        self.consejos= Label(text = "Puede parecer bastante obvio, pero mucha gente no sabe que cuidando nuestra salud física también estamos cuidando nuestra salud mental y por tanto, emocional.", text_size=(6,2))
        self.closeButton = Button(text = "Volver a la ventana anterior", size_hint=(None, None), size=(200,50))  
        layout.add_widget(self.consejos)
        layout.add_widget(self.closeButton) 
        self.popup = Popup(title ='Métodos de estudio', 
                      content = layout,
                      size_hint=(None, None), size=(400, 400))   
        self.popup.open()    
        self.closeButton.bind(on_press = self.popup.dismiss)  
        
    def btnejercicio(self, button): 
          
        layout = GridLayout(cols = 1) 
        self.consejos= Label(text = "Puede parecer bastante obvio,\n pero mucha gente no sabe que cuidando\n nuestra salud física también estamos cuidando\n nuestra salud mental y por tanto, emocional. Cuando\n hacemos ejercicio no sólo mejoramos aspectos\n como nuestra presión sanguínea, sino que también aumentan\n nuestros niveles de energía. Pero lo más importante es que las actividades \nfísicas inciden sobre lo que llamamos “hormonas\n de la felicidad”, y por tanto")
        self.closeButton = Button(text = "Volver a la ventana anterior", size_hint=(None, None), size=(200,50)) 
        layout.add_widget(self.consejos)
        layout.add_widget(self.closeButton) 
        self.popup = Popup(title ='Ejercicio Físico', 
                      content = layout,
                      size_hint=(None, None), size=(400, 400))   
        self.popup.open()    
        self.closeButton.bind(on_press = self.popup.dismiss)  
    
    def btnalimentacion(self, button): 
          
        layout = GridLayout(cols = 1) 
        self.consejos= Label(text = "Puede parecer bastante obvio,\n pero mucha gente no sabe que cuidando\n nuestra salud física también estamos cuidando\n nuestra salud mental y por tanto, emocional. Cuando\n hacemos ejercicio no sólo mejoramos aspectos\n como nuestra presión sanguínea, sino que también aumentan\n nuestros niveles de energía. Pero lo más importante es que las actividades \nfísicas inciden sobre lo que llamamos “hormonas\n de la felicidad”, y por tanto")
        self.closeButton = Button(text = "Volver a la ventana anterior", size_hint=(None, None), size=(200,50)) 
        layout.add_widget(self.consejos)
        layout.add_widget(self.closeButton) 
        self.popup = Popup(title ='Alimentación', 
                      content = layout,
                      size_hint=(None, None), size=(400, 400))   
        self.popup.open()    
        self.closeButton.bind(on_press = self.popup.dismiss)  
        
    def btnrelaciones(self, button): 
          
        layout = GridLayout(cols = 1) 
        self.consejos= Label(text = "Puede parecer bastante obvio,\n pero mucha gente no sabe que cuidando\n nuestra salud física también estamos cuidando\n nuestra salud mental y por tanto, emocional. Cuando\n hacemos ejercicio no sólo mejoramos aspectos\n como nuestra presión sanguínea, sino que también aumentan\n nuestros niveles de energía. Pero lo más importante es que las actividades \nfísicas inciden sobre lo que llamamos “hormonas\n de la felicidad”, y por tanto")
        self.closeButton = Button(text = "Volver a la ventana anterior", size_hint=(None, None), size=(200,50)) 
        layout.add_widget(self.consejos)
        layout.add_widget(self.closeButton) 
        self.popup = Popup(title ='Relaciones Sanas', 
                      content = layout,
                      size_hint=(None, None), size=(400, 400))   
        self.popup.open()    
        self.closeButton.bind(on_press = self.popup.dismiss)  
        
    def btnrelajacion(self, button): 
          
        layout = GridLayout(cols = 1) 
        self.consejos= Label(text = "Puede parecer bastante obvio,\n pero mucha gente no sabe que cuidando\n nuestra salud física también estamos cuidando\n nuestra salud mental y por tanto, emocional. Cuando\n hacemos ejercicio no sólo mejoramos aspectos\n como nuestra presión sanguínea, sino que también aumentan\n nuestros niveles de energía. Pero lo más importante es que las actividades \nfísicas inciden sobre lo que llamamos “hormonas\n de la felicidad”, y por tanto")
        self.closeButton = Button(text = "Volver a la ventana anterior", size_hint=(None, None), size=(200,50)) 
        layout.add_widget(self.consejos)
        layout.add_widget(self.closeButton) 
        self.popup = Popup(title ='Relajación', 
                      content = layout,
                      size_hint=(None, None), size=(400, 400))   
        self.popup.open()    
        self.closeButton.bind(on_press = self.popup.dismiss)  
        
    def btnSueño(self, button): 
          
        layout = GridLayout(cols = 1) 
        self.consejos= Label(text = "Puede parecer bastante obvio,\n pero mucha gente no sabe que cuidando\n nuestra salud física también estamos cuidando\n nuestra salud mental y por tanto, emocional. Cuando\n hacemos ejercicio no sólo mejoramos aspectos\n como nuestra presión sanguínea, sino que también aumentan\n nuestros niveles de energía. Pero lo más importante es que las actividades \nfísicas inciden sobre lo que llamamos “hormonas\n de la felicidad”, y por tanto")
        self.closeButton = Button(text = "Volver a la ventana anterior", size_hint=(None, None), size=(200,50)) 
        layout.add_widget(self.consejos)
        layout.add_widget(self.closeButton) 
        self.popup = Popup(title ='Sueño', 
                      content = layout,
                      size_hint=(None, None), size=(400, 400))   
        self.popup.open()    
        self.closeButton.bind(on_press = self.popup.dismiss)
                              
    def btnAnimo(self, button): 
          
        layout = GridLayout(cols = 1) 
        self.closeButton = Button(text = "Volver a la ventana anterior", size_hint=(None, None), size=(200,50)) 
        layout.add_widget(self.closeButton) 
        self.popup = Popup(title ='Registro de Animo', 
                      content = layout,
                      size_hint=(None, None), size=(400, 400))   
        self.popup.open()    
        self.closeButton.bind(on_press = self.popup.dismiss)
  
        self.popupLabel = Label(text = "¿Cuál ha sido tu estado de ánimo el día de hoy?")
        
        self.botona1 = Button(text = "Feliz",background_color=(155,0,51,53))
        self.botona2 = Button(text = "Cansado",background_color=(100,0,30,53))
        self.botona3 = Button(text = "Triste",background_color=(155,0,10,53))
        self.botona4 = Button(text = "Abrumado")
        self.botona5 = Button(text = "Enojado",background_color=(155,0,0,53))
        
        
        self.closeButton = Button(text = "Volver a la ventana anterior")
        
        layout.add_widget(self.popupLabel) 
        layout.add_widget(self.botona1)
        layout.add_widget(self.botona2)
        layout.add_widget(self.botona3)
        layout.add_widget(self.botona4)
        layout.add_widget(self.botona5)
        
class Pensum(GridLayout, Screen):
 
    def __init__(self, **kwargs):
 
        super(Pensum, self).__init__(**kwargs)
 
        # 2 columnas
        self.cols = 2

        # Lista dde materias del pensum
        self.materias=['Fundamentos_de_fisica_experimental','Fundamentos_de_fisica_teorica','Calculo_diferencial_en_una_variable','Taller_de_matematicas_y_ciencias','Algebra_lineal_basica',
          'Libre_eleccion_I','Mediciones_mecanicas','Mecanica_newtoniana','Calculo_integral_en_una_variable','Calculo_vectorial','Optativa_formación_integral_y_humanistica',
          'Mediciones_electromagneticas','Electricidad_y_magnetismo','Optativa_programacion_y_metodos_numericos','Optativa_estadistica_basica',
          'Calculo_de_ecuaciones_diferenciales_ordinarias','Optativa_formacion_integral_y_humanistica','Mecanica_analitica_I','Oscilaciones_y_ondas','Matematicas_especiales_I_para_fisica',
          'Relatividad','Experimentos_de_fisica_moderna','Mecanica_analitica_II','Electrodinamica_I','Matematicas_especiales_II_para_fisica',
          'Optativa_Electronica_e_instrumentacion','Termodinamica_modulo_experimental','Termodinamica_modulo_de_teoria','Electrodinamica_II',
          'Mecanica_cuantica_I','Optativa_Herramientas_matematicas_y_computacionales','Mediciones_en_optica_y_acustica','Mecanica_estadistica',
          'Temas_de_fisica_contemporanea','Mecanica_cuantica_II','Fluidos_y_optica','Aplicaciones_de_fisica_moderna','Introduccion_al_estado_solido',
          'Introduccion_a_la_investigacion_experimental_o_teorica','Introduccion_a_la_subatomica','Libre_eleccion_II','Libre_eleccion_III','Libre_eleccion_IV',
          'Libre_eleccion_V','Libre_eleccion_VI','Libre_eleccion_VII','Trabajo_de_grado','Libre_eleccion_VIII']
       
        #Crea los checkbox
        for i in self.materias:
            self.add_widget(Label(text= i))
            self.active = CheckBox()
            self.add_widget(self.active)
            self.active.bind(active = self.on_checkbox_Active)
                    
        i=96
        for self.active in self.children:        
            self.active.id=int(i/2)
            i=i-1                     
           
        #Crea el botón
        self.continuar = Button(text="Continuar", background_color=(155,0,51,53))
        self.continuar.bind(on_press=self.onButtonPress)
        self.add_widget(self.continuar)

          
 #----------------------------------------
 
  # Función que elimina las materias clickeadas de la lista
    def on_checkbox_Active(self, checkbox, value):
        materias=['Fundamentos_de_fisica_experimental','Fundamentos_de_fisica_teorica','Calculo_diferencial_en_una_variable','Taller_de_matematicas_y_ciencias','Algebra_lineal_basica',
          'Libre_eleccion_I','Mediciones_mecanicas','Mecanica_newtoniana','Calculo_integral_en_una_variable','Calculo_vectorial','Optativa_formación_integral_y_humanistica',
          'Mediciones_electromagneticas','Electricidad_y_magnetismo','Optativa_programacion_y_metodos_numericos','Optativa_estadistica_basica',
          'Calculo_de_ecuaciones_diferenciales_ordinarias','Optativa_formacion_integral_y_humanistica','Mecanica_analitica_I','Oscilaciones_y_ondas','Matematicas_especiales_I_para_fisica',
          'Relatividad','Experimentos_de_fisica_moderna','Mecanica_analitica_II','Electrodinamica_I','Matematicas_especiales_II_para_fisica',
          'Optativa_Electronica_e_instrumentacion','Termodinamica_modulo_experimental','Termodinamica_modulo_de_teoria','Electrodinamica_II',
          'Mecanica_cuantica_I','Optativa_Herramientas_matematicas_y_computacionales','Mediciones_en_optica_y_acustica','Mecanica_estadistica',
          'Temas_de_fisica_contemporanea','Mecanica_cuantica_II','Fluidos_y_optica','Aplicaciones_de_fisica_moderna','Introduccion_al_estado_solido',
          'Introduccion_a_la_investigacion_experimental_o_teorica','Introduccion_a_la_subatomica','Libre_eleccion_II','Libre_eleccion_III','Libre_eleccion_IV',
          'Libre_eleccion_V','Libre_eleccion_VI','Libre_eleccion_VII','Trabajo_de_grado','Libre_eleccion_VIII']
        if value:
            self.materias.remove(materias[checkbox.id])
        else: 
            self.materias.insert(checkbox.id, materias[checkbox.id])
        print(self.materias)
             
     #Cuando se oprima el botón 'siguiente', muestra un popup para escoger los semestres
    def onButtonPress(self, button): 
          
        layout = GridLayout(cols = 1) 
  
        self.popupLabel = Label(text = "Seleccione la cantidad de semestres que quiere cursar")
        
        self.boton1 = Button(text = "1")
        self.boton2 = Button(text = "2")
        self.boton3 = Button(text = "3")
        self.boton4 = Button(text = "4")
        self.boton5 = Button(text = "5")
        self.boton6 = Button(text = "6")
        self.boton7 = Button(text = "7")
        self.boton8 = Button(text = "8")
        self.boton9 = Button(text = "9")
        self.boton10 = Button(text = "10")
        self.boton11 = Button(text = "11")
        self.boton12 = Button(text = "12")
        self.boton13 = Button(text = "13")
        self.boton14 = Button(text = "14")
        self.boton15 = Button(text = "15")

        
        
        self.closeButton = Button(text = "Volver a la ventana anterior") 
         

  
        layout.add_widget(self.popupLabel) 
        layout.add_widget(self.boton1)
        layout.add_widget(self.boton2)
        layout.add_widget(self.boton3)
        layout.add_widget(self.boton4)
        layout.add_widget(self.boton5)
        layout.add_widget(self.boton6)
        layout.add_widget(self.boton7)
        layout.add_widget(self.boton8)
        layout.add_widget(self.boton9)
        layout.add_widget(self.boton10)
        layout.add_widget(self.boton11)
        layout.add_widget(self.boton12)
        layout.add_widget(self.boton13)
        layout.add_widget(self.boton14)
        layout.add_widget(self.boton15)
        
        layout.add_widget(self.closeButton)  
        
        
        self.popup = Popup(title ='Cantidad de semestres', 
                      content = layout,
                      size_hint=(None, None), size=(400, 400))   
        self.popup.open()    
 
        self.closeButton.bind(on_press = self.popup.dismiss)  
        self.boton1.bind(on_press= self.onButtonPress1)
        self.boton2.bind(on_press= self.onButtonPress2)
        self.boton3.bind(on_press= self.onButtonPress3)
        self.boton4.bind(on_press= self.onButtonPress4)
        self.boton5.bind(on_press= self.onButtonPress5)
        self.boton6.bind(on_press= self.onButtonPress6)
        self.boton7.bind(on_press= self.onButtonPress7)
        self.boton8.bind(on_press= self.onButtonPress8)
        self.boton9.bind(on_press= self.onButtonPress9)
        self.boton10.bind(on_press= self.onButtonPress10)
        self.boton11.bind(on_press= self.onButtonPress11)
        self.boton12.bind(on_press= self.onButtonPress12)
        self.boton13.bind(on_press= self.onButtonPress13)
        self.boton14.bind(on_press= self.onButtonPress14)
        self.boton15.bind(on_press= self.onButtonPress15)
        
        
    def onButtonPress1(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(1, a)
    def onButtonPress2(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(2, round(float(a/2)))
    def onButtonPress3(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(3, round(float(a/3)))
    def onButtonPress4(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(4, round(float(a/4)))
    def onButtonPress5(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(5, round(float(a/5)))
    def onButtonPress6(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(6, round(float(a/6)))
    def onButtonPress7(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(7, round(float(a/7)))
    def onButtonPress8(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(8, round(float(a/8)))
    def onButtonPress9(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(9, round(float(a/9)))
    def onButtonPress10(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(10, round(float(a/10)))
    def onButtonPress11(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(11, round(float(a/11)))
    def onButtonPress12(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(12, round(float(a/12)))
    def onButtonPress13(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(13, round(float(a/13)))
    def onButtonPress14(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(14, round(float(a/14)))
    def onButtonPress15(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + eval(x).__dict__.get('creditos')
        print(15, round(float(a/15)))
  

class MenuScreen(Screen):
    pass
  
   
# Crea screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Pensum(name='pensum'))
sm.add_widget(SaludMental(name='saludmental'))
   
  
class NombreTentativo(App): 
    def build(self): 
        return sm
  

if __name__ == '__main__': 
    NombreTentativo().run()



#---------------------TO DO LIST
#texto agregado
class AgregarTexto(Widget):
    texto_ingresado = ObjectProperty(None)
    input = StringProperty('')
    store = JsonStore("data.json")

    def subir_input(self):
        self.input = self.texto_ingresado.text
        print("Assign input: {}".format(self.input))
        self.guardar()
        self.input =''

    def guardar(self):
        self.store.put(self.input)


######falta corregir
class EliminarTarea(GridLayout, Screen):
    def __init__(self, **kwargs):
        super(VistaPantalla, self).__init__(**kwargs)
        self.eliminar_datos()
        Clock.schedule_interval(self.eliminar_datos, 1)
        
        for i in self.materias:
            self.add_widget(Label(text= i))
            self.active = CheckBox()
            self.add_widget(self.active)
            self.active.bind(active = self.on_checkbox_Active)
            
    def eliminar_datos(self, checkboxInstance, value):
        store = JsonStore("data.json")
        if value:
            for i in store: 
                store.pop(i)
                break 
            self.store.pop()
        else:
           pass
        print(self.store)
##########falta corregir

#organizar la lista
class Menu(BoxLayout):
    manager = ObjectProperty(None)


#vista de la pantalla
class VistaPantalla(RecycleView):
    def __init__(self, **kwargs):
        super(VistaPantalla, self).__init__(**kwargs)
        self.leer_datos()
        Clock.schedule_interval(self.leer_datos, 1)

#mostrar la informacion recibida
    def leer_datos(self, *args):
        store = JsonStore("data.json")
        lista_datos = []
        for i in store:
            lista_datos.append({'text': i})

        self.data = lista_datos


# configuración pantalla dispositivo
class PantallaPrincipal(Screen):
    pass


class PantallaAdicional(Screen):
    def __init__(self, **kwargs):
        super(PantallaAdicional, self).__init__(**kwargs)
        self.addNewForm = AgregarTexto()
        self.add_widget(self.addNewForm)


#permite ver varias pantallas
class Pantallas(ScreenManager):
    pantalla_principal = ObjectProperty(None)
    pantalla_adicional = ObjectProperty(None)

#----------------TO DO LIST

#Calendario aún en proceso u.u
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import NumericProperty
from kivy.uix.gridlayout import GridLayout
import calendar


class Calendar(Popup):
    day = NumericProperty()
    month = NumericProperty()
    year = NumericProperty()
    root = BoxLayout(orientation = "vertical")
    
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(Popup, self).__init__(**kwargs)

        self.add_widget(self.root)
        self.crearcalendario()

    def crearcalendario(self):
        self.day_str = [ 'L', 'M', 'Mc', 'J', 'V', 'S', 'D' ]
        self.month_str = [ 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre' ]
    
        self.dy = calendar.monthcalendar(self.year, self.month)
        self.title = (self.month_str[self.month-1] + ", " + str(self.year) )        
        
        layout = GridLayout(cols=7)  
        
        # Poner nombres de días
        #      
        for d in self.day_str:
            b = Label(text = '[b]'+d+'[/b]' , markup=True )
            layout.add_widget(b)
         
        # Llenar el calendario con calendar.monthcalendar
        #    
        for wk in range(len(self.dy)):
            for d in range(0,7):    
                dateOfWeek = self.dy[wk][d]
                if not dateOfWeek == 0:
                    b = Button(text = str(dateOfWeek))
                    b.bind(on_release = self.fecha)
                else:
                    b = Label(text = '' )
                layout.add_widget(b)
                
        if self.root:
            self.root.clear_widgets()
        self.root.add_widget(layout)
        botonesabajo = BoxLayout(orientation = "horizontal", size_hint = (1,None), height = 40)
        botonesabajo.add_widget(Button(text = '<', on_release = self.cambiarmes))
        botonesabajo.add_widget(Button(text = '>', on_release = self.cambiarmes))
        self.root.add_widget(botonesabajo)
        
    def cambiarmes(self, event):
        if event.text == '>':
            if self.month == 12:
                self.month = 1
                self.year = self.year + 1
            else:
                self.month = self.month + 1
        elif event.text == '<':
            if self.month == 1:
                self.month = 12
                self.year = self.year - 1
            else:
                self.month = self.month - 1
        
    def fecha(self, event):
        self.day = int(event.text)
        self.dismiss()



class MyCalendar(App):
    def build(self):
        # Target Month and Year to display
        #
        self.popup = Calendar(month = 11, year = 2020,
            size_hint=(None, None), size=(500, 400))
        self.popup.bind(on_dismiss = self.on_dismiss)
        return Button(text = "Show calendar", on_release = self.mostrar)
    
    def mostrar(self, event):
        # Create Popup
        #                 
        self.popup.open()

    def on_dismiss(self, arg):
        # Do something on close of popup
        print ("Fecha: ", str(self.popup.day) + '/' + str(self.popup.month) + '/' + str(self.popup.year) )

if __name__ == "__main__":
    MyCalendar().run()   
# configuración pantalla dispositivo
class HomeScreen(Screen):
    pass
---------------------------


#Función para organizar las materias

def ordenarcriterio1(x,y,z):
    for i in range(len(x)-1):
      for j in range(i+1,len(x)):
        if x[i] > x[j]:
          x[i],x[j] = x[j],x[i]
          y[i],y[j] = y[j],y[i]
          z[i],z[j] = z[j],z[i]
    return x,y,z
li,li2,li3=ordenarcriterio1(materias3,materias2,LineasCampo)
def mallacurricular(x,a,b,c):
    m_organize=[]
    c_organize=[]
    l_organize=[]
    materiaslist=a*1
    criterio1=b*1
    lincamp=c*1
    n=0
    v=len(materiaslist)
    while len(m_organize)<v:
        #print(m_organize)
        i=materiaslist[0]
        while n<x:
            if c_organize==[] or criterio1[0]==criterio1[-1]:
                 m_organize.append(i)
                 l_organize.append(materiaslist.index(i))
                 c_organize.append(materiaslist.index(i))
                 n+=1      
                 criterio1.pop(materiaslist.index(i))
                 lincamp.pop(materiaslist.index(i))
                 materiaslist.remove(i)
            elif c_organize[-1]<=criterio1[materiaslist.index(i)]:
                if lincamp[materiaslist.index(i)] not in l_organize[len(l_organize)-n:]:
                    m_organize.append(i)
                    l_organize.append(materiaslist.index(i))
                    c_organize.append(materiaslist.index(i))
                    criterio1.pop(materiaslist.index(i))
                    lincamp.pop(materiaslist.index(i))
                    materiaslist.remove(i)
                    n+=1
            else:
                materiaslist.append(i)
                criterio1.append(materiaslist.index(i))
                lincamp.append(materiaslist.index(i))
                criterio1.pop(materiaslist.index(i))
                lincamp.pop(materiaslist.index(i))  
                materiaslist.remove(i)
            if criterio1==[]:
                break
            else:
               i=materiaslist[0]
        n=0
    return m_organize



-----------------------------------------------------------------------------------
#Función para eliminar materias-corregida:

class Pensum(GridLayout, Screen):
 
    def __init__(self, **kwargs):
 
        super(Pensum, self).__init__(**kwargs)
 
        # 2 columnas
        self.cols = 2

        # Lista dde materias del pensum
        self.materias=['Fundamentos_de_fisica_experimental','Fundamentos_de_fisica_teorica','Calculo_diferencial_en_una_variable','Taller_de_matematicas_y_ciencias','Algebra_lineal_basica',
          'Libre_eleccion_I','Mediciones_mecanicas','Mecanica_newtoniana','Calculo_integral_en_una_variable','Calculo_vectorial','Optativa_formación_integral_y_humanistica',
          'Mediciones_electromagneticas','Electricidad_y_magnetismo','Optativa_programacion_y_metodos_numericos','Optativa_estadistica_basica',
          'Calculo_de_ecuaciones_diferenciales_ordinarias','Optativa_formacion_integral_y_humanistica','Mecanica_analitica_I','Oscilaciones_y_ondas','Matematicas_especiales_I_para_fisica',
          'Relatividad','Experimentos_de_fisica_moderna','Mecanica_analitica_II','Electrodinamica_I','Matematicas_especiales_II_para_fisica',
          'Optativa_Electronica_e_instrumentacion','Termodinamica_modulo_experimental','Termodinamica_modulo_de_teoria','Electrodinamica_II',
          'Mecanica_cuantica_I','Optativa_Herramientas_matematicas_y_computacionales','Mediciones_en_optica_y_acustica','Mecanica_estadistica',
          'Temas_de_fisica_contemporanea','Mecanica_cuantica_II','Fluidos_y_optica','Aplicaciones_de_fisica_moderna','Introduccion_al_estado_solido',
          'Introduccion_a_la_investigacion_experimental_o_teorica','Introduccion_a_la_subatomica','Libre_eleccion_II','Libre_eleccion_III','Libre_eleccion_IV',
          'Libre_eleccion_V','Libre_eleccion_VI','Libre_eleccion_VII','Trabajo_de_grado','Libre_eleccion_VIII']
       
        #Crea los checkbox
        for i in self.materias:
            self.add_widget(Label(text= i))
            active = CheckBox()
            self.add_widget(active)
            active.bind(active = self.on_checkbox_Active)
                                                             
        i=0
        for self.active in self.children:        
            self.active.id=int(i/2)
            i=i+1            
           
        #Crea el botón
        self.continuar = Button(text="Continuar", background_color=(155,0,51,53))
        self.continuar.bind(on_press=self.onButtonPress)
        self.add_widget(self.continuar)
         
 #----------------------------------------
 
  # Función que elimina las materias clickeadas de la lista
    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive: 
            self.materias.pop(self.active.id)
        else: 
           pass
        print(self.materias)
