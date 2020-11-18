materias=['Algebra_lineal','Calculo_diferencial','Fundamentos_de_fisica_teorica','Fundamentos_de_fisica_experimental','Taller_de_matematicas_y_ciencias',
          'Calculo_integral','Calculo_vectorial','Mecanica_Newtoniana','Mediciones_mecanicas','Optativa_formación_integral_y_humanistica',
          'Mediciones_electromagneticas','Electricidad_y_magnetismo','Optativa_programacion_y_metodos_numericos','Optativa_estadistica_basica',
          'Calculo_de_ecuaciones_diferenciales_ordinarias','Optativa','Mecanica_analitica_I','Oscilaciones_y_ondas','Matematicas_especiales_I_para_fisica',
          'Relatividad','Experimentos_de_fisica_moderna','Mecanica_analitica_II','Electrodinamica_I','Matematicas_especiales_II_para_fisica',
          'Optativa_Electronica_e_instrumentacion','Termodinamica_modulo_experimental','Termodinamica_modulo_de_teoria','Electrodinamica_II',
          'Mecanica_Cuantica_I','Optativa_Herramientas_matematicas_y_computacionales','Mediciones_en_optica_y_acustica','Mecanica_estadistica',
          'Temas_de_fisica_contemporanea','Mecanica_cuantica_II','Fluidos_y_optica','Aplicaciones_de_fisica_moderna','Introduccion_al_estado_solido',
          'Introduccion_a_la_investigacion_experimental_o_teorica','Introduccion_a_la_subatomica','Libre_eleccion_II','Libre_eleccion_III','Libre_eleccion_IV',
          'Libre_eleccion_V','Libre_eleccion_VI','Libre_eleccion_VII','Trabajo_de_grado']

#-------------------------------------------------

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
 
   
class pensum(GridLayout):
 
    def __init__(self, **kwargs):
 
        super(pensum, self).__init__(**kwargs)
 
        # 2 columnas
        self.cols = 2

        # Lista dde materias del pensum
        self.materias=['Algebra_lineal','Calculo_diferencial','Fundamentos_de_fisica_teorica','Fundamentos_de_fisica_experimental','Taller_de_matematicas_y_ciencias',
          'Calculo_integral','Calculo_vectorial','Mecanica_Newtoniana','Mediciones_mecanicas','Optativa_formación_integral_y_humanistica',
          'Mediciones_electromagneticas','Electricidad_y_magnetismo','Optativa_programacion_y_metodos_numericos','Optativa_estadistica_basica',
          'Calculo_de_ecuaciones_diferenciales_ordinarias','Optativa','Mecanica_analitica_I','Oscilaciones_y_ondas','Matematicas_especiales_I_para_fisica',
          'Relatividad','Experimentos_de_fisica_moderna','Mecanica_analitica_II','Electrodinamica_I','Matematicas_especiales_II_para_fisica',
          'Optativa_Electronica_e_instrumentacion','Termodinamica_modulo_experimental','Termodinamica_modulo_de_teoria','Electrodinamica_II',
          'Mecanica_Cuantica_I','Optativa_Herramientas_matematicas_y_computacionales','Mediciones_en_optica_y_acustica','Mecanica_estadistica',
          'Temas_de_fisica_contemporanea','Mecanica_cuantica_II','Fluidos_y_optica','Aplicaciones_de_fisica_moderna','Introduccion_al_estado_solido',
          'Introduccion_a_la_investigacion_experimental_o_teorica','Introduccion_a_la_subatomica','Libre_eleccion_II','Libre_eleccion_III','Libre_eleccion_IV',
          'Libre_eleccion_V','Libre_eleccion_VI','Libre_eleccion_VII','Trabajo_de_grado']
       
        #Crea los checkbox
        for i in self.materias:
            self.add_widget(Label(text= i))
            self.active = CheckBox()
            self.add_widget(self.active)
            self.active.bind(active = self.on_checkbox_Active)
           
        #Crea el botón
        self.continuar = Button(text="Continuar", background_color=(155,0,51,53))
        self.continuar.bind(on_press=self.onButtonPress)
        self.add_widget(self.continuar)

          
 #----------------------------------------
 
  # Función que elimina las materias clickeadas de la lista
    def on_checkbox_Active(self, checkboxInstance, isActive): 
        if isActive: 
            self.materias.pop()
        else: 
           pass
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
        self.popup.dismiss()
        print(int(1))
    def onButtonPress2(self,button):
        self.popup.dismiss()
        print(int(2))
    def onButtonPress3(self,button):
        self.popup.dismiss()
        print(int(3))
    def onButtonPress4(self,button):
        self.popup.dismiss()
        print(int(4))
    def onButtonPress5(self,button):
        self.popup.dismiss()
        print(int(5))
    def onButtonPress6(self,button):
        self.popup.dismiss()
        print(int(6))
    def onButtonPress7(self,button):
        self.popup.dismiss()
        print(int(7))
    def onButtonPress8(self,button):
        self.popup.dismiss()
        print(int(8))
    def onButtonPress9(self,button):
        self.popup.dismiss()
        print(int(9))
    def onButtonPress10(self,button):
        self.popup.dismiss()
        print(int(10))
    def onButtonPress11(self,button):
        self.popup.dismiss()
        print(int(11))
    def onButtonPress12(self,button):
        self.popup.dismiss()
        print(int(12))
    def onButtonPress13(self,button):
        self.popup.dismiss()
        print(int(13))
    def onButtonPress14(self,button):
        self.popup.dismiss()
        print(int(14))
    def onButtonPress15(self,button):
        self.popup.dismiss()
        print(int(15))
  
          
class NombreTentativo(App):
    def build(self):
        return pensum()
 
##Ejecutar kivy
if __name__ == '__main__':
    NombreTentativo().run()
-----------------------------------------------------------------------------------

#Función para leer prerrequisitos
materias2=[]    
materias3=[]
LineasCampo=[]
class materias:
    def __init__(self,nom,cre=3,pre=[],co=[],criterio=0,Linea=0):
        self.nombre=nom
        self.creditos=cre
        self.prerrequisitos=pre
        self.correquisitos=co
        self.criterio=criterio
        self.linea=linea
        LineasCampo.append(self.linea_val())
        materias3.append(self.criterio_val())
        self.__str__()
        self.orden()
    def criterio_val(self):
        return self.criterio
    def linea_val(self):
        return self.linea
    def __str__(self):
        cadena=self.nombre
        if cadena not in materias2:
            materias2.append(cadena)
    def orden(self):
          if len(self.prerrequisito)==0:
            self.linea==len(LineasCampo)+1
          else:
                  for n in materias2:
                      for i in range(len(self.prerrequisitos)):
                          if n == self.prerrequisitos[i]: #si en la lista materias hay un prerrequisito
                              self.criterio=self.criterio+materias3[materias2.index(n)]+1
                              materias3[-1]=self.criterio_val()
                              self.linea=LineasCampo[materias2.index(n)]
                              LineasCampo[-1]=self.linea_val()
                    
    def __gt__(self, otro): #para utilizar el sorted(materias)
        return self.criterio > otro.criterio  #El criterio es lo que se utilizará para armar la matriz
#Función para repartir los créditos por semestre
 def onButtonPress1(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 1, a
    def onButtonPress2(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 2, round(float(a/2))
    def onButtonPress3(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 3, round(float(a/3))
    def onButtonPress4(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 4, round(float(a/4))
    def onButtonPress5(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 5, round(float(a/5))
    def onButtonPress6(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 6, round(float(a/6))
    def onButtonPress7(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 7, round(float(a/7))
    def onButtonPress8(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 8, round(float(a/8))
    def onButtonPress9(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 9, round(float(a/9))
    def onButtonPress10(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 10, round(float(a/10))
    def onButtonPress11(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 11, round(float(a/11))
    def onButtonPress12(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 12, round(float(a/12))
    def onButtonPress13(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 13, round(float(a/13))
    def onButtonPress14(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 14, round(float(a/14))
    def onButtonPress15(self,button):
        a = 0
        self.popup.dismiss()
        for x in self.materias:
            a = a + x.__dict__.get('creditos')
        return 15, round(float(a/15))

#SEMESTRE I
Algebra_lineal=subject(4, [])
Calculo_diferencial=subject(4, [])
Fundamentos_de_fisica_teorica=subject(3, [])
Fundamentos_de_fisica_experimental=subject(3, [])
Taller_de_matematicas_y_ciencias=subject(3, [])

#SEMESTRE II
Calculo_integral=subject(4, ['Calculo_diferencial'])
Calculo_vectorial=subject(4, [], ['Calculo_integral'])
Mecanica_Newtoniana=subject(4, ['Fundamentos_de_fisica_teorica'])
Mediciones_mecanicas=subject(3, ['Fundamentos_de_fisica_experimental'])
Optativa_formación_integral_y_humanistica=subject(3, [])

#SEMESTRE III
Mediciones_electromagneticas=subject(3,[],['Fundamentos_de_fisica_experimental'])
Electricidad_y_magnetismo=subject(3,[],['Calculo_integral', 'Calculo_vectorial'])
Optativa_programacion_y_metodos_numericos=subject(3,[],['Algebra_lineal'])
Optativa_estadistica_basica=subject(3,['Calculo_diferencial'])
Calculo_de_ecuaciones_diferenciales_ordinarias=subject(4,['Calculo_integral'])

#SEMESTRE IV
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
Aplicaciones_de_fisica_moderna=(3,['Introduccion_al_estado_solido'])
Introduccion_al_estado_solido=(3,['Mecanica_estadistica'])
Introduccion_a_la_subatomica=(3,['Mecanica_cuantica_II'])
Libre_eleccion_II=(4,[])
Libre_eleccion_III=(4,[])

#SEMESTRE IX	
Introduccion_a_la_investigacion_experimental_o_teorica=subject(3,[])	
Libre_eleccion_IV=subject(4,[])	
Libre_eleccion_V=subject(4,[])	
Libre_eleccion_VI=subject(4,[])	
Libre_eleccion_VII=subject(4,[])	

#SEMESTRE X	
Trabajo_de_grado=subject(8,[])
Libre_eleccion_VII=subject(4,[])
