#20 VERIFICADORES DE TUS PROGRAMAS PREVIOS
print("VERIFICADORES:")
print("ALUMNO:CARLOS RONALDO LIZA DAMIAN")
print("")

#CALCULADORA NRO01
#ESTA CAlCULADORA REALIZA EL CALCULO DE MOVIMIENTO RECTILINEO UNIFORME(MRU)

#DECLARACION DE VARIABLES
velocidad,tiempo,distancia=0.0,0.0,0.0

#CALCULADORA
velocidad=5000.0
tiempo=15.0
distancia=velocidad*tiempo

#MOSTRAR DATOS
print("velocidad =",velocidad,"m/s")
print("tiempo =",tiempo,"s")
print("distancia =",distancia,"m")

#VERIFICADOR
print("VERIFICADOR:")
formula_excesiva=(distancia>300)
print("ES UNA FORMULA EXCESIVA:",formula_excesiva)
print("")

#CALCULADORA NRO02
#ESTA CAlCULADORA REALIZA EL CALCULO DE MOVIMIENTO RECTILINEO UNIFORMEMENTE VARIADO(MRUV)

#DECLARACION DE VARIABLES
velocidad_inicial,aceleracion,Tiempo,velocidad_final=0.0,0.0,0.0,0.0

#CALCULADORA
velocidad_inicial=20.8
aceleracion=541.1
Tiempo=22.5
velocidad_final=velocidad_inicial+aceleracion*Tiempo

#MOSTRAR DATOS
print("velocidad inicial=",velocidad_inicial,"m/s")
print("aceleracion=",aceleracion,"m/segundo al cuadrado")
print("tiempo=",Tiempo,"s")
print("velocidad final=",velocidad_final,"m/s")

#VERIFICADOR
print("VERIFICADOR:")
Formula_excesiva=(velocidad_final>478511)
print("ES UNA FORMULA EXCESIVA:",Formula_excesiva)
print("")

#CALCULADORA NRO3
#ESTA CAlCULADORA REALIZA EL CALCULO DE VELOCIDAD TANGENCIAL

#DECLARACION DE VARIABLES
velocidad_angular,radio,velocidad_tangencial=0.0,0.0,0.0

#CALCULADORA
velocidad_angular=548.5
radio=23.5
velocidad_tangencial=velocidad_angular*radio

#MOSTRAR DATOS
print("velocidad angular =",velocidad_angular,"w")
print("radio =",radio,"m")
print("velocidad tangencial =",velocidad_tangencial,"m/s")

#VERIFICADOR
print("VERIFICADOR:")
calculo_velocidadtangencial_excesiva=(velocidad_tangencial>5000)
print("LA VELOCIDAD TANGENCIAL ES EXCESIVA:",calculo_velocidadtangencial_excesiva)
print("")

#CALCULADORA NRO4
#ESTA CAlCULADORA REALIZA EL CALCULO DE la FRECUENCIA

#DECLARACION DE VARIABLES
nro_vueltas,tiempo_empleado,freuencia=0,0.0,0.0

#CALCULADORA
nro_vueltas=500.0
tiempo_empleado=30.5
freuencia=nro_vueltas/tiempo_empleado

#MOSTRAR DATOS
print("nro vueltas =",nro_vueltas,)
print("Tiempo empleado =",tiempo_empleado,"s")
print("Frecuencia =",freuencia,"Hz")

#VERIFICADOR
print("VERIFICADOR:")
calculo_de_la_frecuencia_excesiva=(freuencia>7458)
print("ES UNA FORMULA EXCESIVA:",calculo_de_la_frecuencia_excesiva)
print("")

#CALCULADORA NRO05
#ESTA CAlCULADORA REALIZA EL CALCULO DE FUERZA ELASTICA

#DECLARACION DE VARIABLES
constante_rigidez,deformacion,fuerza_elastica=0.0,0.0,0.0

#CALCULADORA
constante_rigidez=50.0
deformacion=52.5
fuerza_elastica=constante_rigidez*deformacion

#MOSTRAR DATOS
print("Constante de rigidez =",constante_rigidez,"N/m")
print("Deformacion =",deformacion,"m")
print("Fuerza elastica =",fuerza_elastica,"Newton")

#VERIFICADOR
print("VERIFICADOR:")
calculo_fuerzaelastica_excesiva=(fuerza_elastica>100)
print("LA FUERZA ELASTICA EXCEDE:",calculo_fuerzaelastica_excesiva)
print("")

#CALCULADORA NRO06
#ESTA CAlCULADORA REALIZA EL CALCULO DE FUERZA DE ROZAMIENTO

#DECLARACION DE VARIABLES
coeficiente_rozamiento,normal,fuerza_rozamiento=0.0,0.0,0.0

#CALCULADORA
coeficiente_rozamiento=50.5
normal=200.0
fuerza_rozamiento=coeficiente_rozamiento*normal

#MOSTRAR DATOS
print("coeficiente_rozamiento =",coeficiente_rozamiento)
print("normal =",normal,"m/segundos al cuadrado")
print("Fuerza de Rozamiento =",fuerza_rozamiento,"Newton")

#VERIFICADOR
print("VERIFICADOR:")
fuerza_rozamianto_excesiva=(fuerza_rozamiento>800)
print("LA FORMULA ES ENORME:",fuerza_rozamianto_excesiva)
print("")

#CALCULADORA NRO07
#ESTA CAlCULADORA REALIZA EL CALCULO DEL PESO

#DECLARACION DE VARIABLES
masa,gravedad,peso=0.0,0.0,0.0

#CALCULADORA
masa=880.4
gravedad=10.0
peso=masa*gravedad

#MOSTRAR DATOS
print("masa =",masa,"kg")
print("gravedad =",gravedad,"m/segundos al cuadrado")
print("peso =",peso,"Newton")

#VERIFICADOR
print("VERIFICADOR:")
formula_del_peso_excesiva=(peso>400)
print("LA FORMULA DEL PESO EXCEDE:",formula_del_peso_excesiva)
print("")

#CALCULADORA NRO08
#ESTA CAlCULADORA REALIZA EL CALCULO DE LA LEY DE POUILLET

#DECLARACION DE VARIABLES
longitud_del_conductor,area,resistencia_electrica=0.0,0.0,0.0

#CALCULADORA
longitud_del_conductor=555.0
area=5.4
resistencia_electrica=longitud_del_conductor/area

#MOSTRAR DATOS
print("longitud del conductor =",longitud_del_conductor,"m")
print("area =",area,"metros al cuadrado")
print("resistencia electrica =",resistencia_electrica,"ohm")

#VERIFICADOR
print("VERIFICADOR:")
ley_de_pouillet_excede=(resistencia_electrica>100)
print("LA LEY DE POUILLET EXCEDE:",ley_de_pouillet_excede)
print("")

#CALCULADORA NRO09
#ESTA CAlCULADORA REALIZA EL CALCULO DE LA RESISTENCIA ELECTRICA

#DECLARACION DE VARIABLES
resistencia_inicial,variacion_de_temperatura,coeficiente_de_temperatura,resistencia=0.0,0.0,0.0,0.0

#CALCULADORA
resistencia_inicial=500.5
coeficiente_de_temperatura=5005.0
variacion_de_temperatura=114.5
resistencia=(resistencia_inicial+resistencia*coeficiente_de_temperatura*variacion_de_temperatura)

#MOSTRAR DATOS
print("resistencia inicial =",resistencia_inicial,"ohm")
print("coeficiente de temperatura =",coeficiente_de_temperatura,)
print("variacion de temperatura =",variacion_de_temperatura,"c")
print("resistencia =",resistencia,"w")

#VERIFICADOR
print("VERIFICADOR:")
formula_de_resistenciaelectrica_excesiva=(resistencia>150)
print("LA RESISTENCIA ELECTRICA EXCEDE:",formula_excesiva)
print("")

#CALCULADORA NRO10
#ESTA CAlCULADORA REALIZA EL CALCULO DE LA POTENCIA ELECTRICA

#DECLARACION DE VARIABLES
intencidad_de_corriente,Variacion_de_temperatura,petencia_electrica=0.0,0.0,0.0

#CALCULADORA
intencidad_de_corriente=25.0
variacion_de_temperatura=50.4
petencia_electrica= intencidad_de_corriente*variacion_de_temperatura

#MOSTRAR DATOS
print("intencidad de corriente =",intencidad_de_corriente,"A")
print("variacion de temperatura =",variacion_de_temperatura,"c")
print("Potencia electrica =",petencia_electrica,"voltios")

#VERIFICADOR
print("VERIFICADOR:")
formula_excesiva=(petencia_electrica>200)
print("ES UNA FORMULA EXCESIVA:",formula_excesiva)
print("")

#CALCULADORA NRO11
#ESTA CAlCULADORA REALIZA EL CALCULO DE FORMULA DE LA TERMODINAMICA

#DECLARACION DE VARIABLES
precion,volumen,cantidad_de_sustancia,costante_universal,tempetatura_absoluta=0.0,0.0,0.0,0.0,0.0

#CALCULADORA
Precion=450.5
volumen=23.4
cantidad_de_sustancia=34.5
costante_universal=8.31
tempetatura_absoluta=100.0
precion=cantidad_de_sustancia*costante_universal*tempetatura_absoluta/volumen

#MOSTRAR DATOS
print("precion =",Precion,"pa")
print("volumen =",volumen,"metros cubicos")
print("cantidad de sustancia =",cantidad_de_sustancia,"mol")
print("costante universal =",costante_universal,"J/mol.k")
print("temperatura absoluta =",tempetatura_absoluta,"k")
print("precion =",precion,"pa")

#VERIFICADOR
print("VERIFICADOR:")
formula_excesiva_de_termodinamica=(precion>1000)
print("LA FORMULA DE LA TERMODINAMICA ES EXCESIVA:",formula_excesiva_de_termodinamica)
print("")

#CALCULADORA NRO12
#ESTA CAlCULADORA REALIZA EL CALCULO DE LA PRIMERA LEY DE LA TERMODINAMICA

#DECLARACION DE VARIABLES
calor,trabajo_efectuado,cambio_de_energia=0.0,0.0,0.0

#CALCULADORA
calor=52.2
trabajo_efectuado=50.5
cambio_de_energia= calor-trabajo_efectuado

#MOSTRAR DATOS
print("calor =",calor,"N.m")
print("trabajo efectuado =",trabajo_efectuado,"N.m")
print("cambio de energia =",cambio_de_energia,"Joule")

#VERIFICADOR
print("VERIFICADOR:")
formula_excesiva_primera_leytermodinamica=(cambio_de_energia>200)
print("LA FORMULA DE LA PRIMERA LEY DE LA TERMODINAMICA ES EXCESIVA:",formula_excesiva_primera_leytermodinamica)
print("")

#CALCULADORA NRO13
#ESTA CAlCULADORA REALIZA EL CALCULO DEL AREA DEL TRAPECIO

#DECLARACION DE VARIABLES
base_mayor,base_menor,altura,area_trapecio=0.0,0.0,0.0,0.0

#CALCULADORA
base_mayor=10.5
base_menor=154.0
altura=500.0
area_trapecio=((base_mayor+base_menor/2))*altura

#MOSTRAR DATOS
print("base mayor =",base_mayor)
print("base menor =",base_menor)
print("altura =",altura)
print("area del trapecio =",area_trapecio)

#VERIFICADOR
print("VERIFICADOR:")
calculo_del_areatrapecio_excede=(area_trapecio>150)
print("CALCULO DEL AREA DEL TRAPECIO EXCEDE:",calculo_del_areatrapecio_excede)
print("")

#CALCULADORA NRO14
#ESTA CAlCULADORA REALIZA EL CALCULO DE LA DENSIDAD

#DECLARACION DE VARIABLES
Masa,Volumen,Densidad=0.0,0.0,0.0

#CALCULADORA
Masa=5504.0
Volumen=50.2
Densidad=Masa/Volumen

#MOSTRAR DATOS
print("masa =",Masa,"kg")
print("volumen =",Volumen,"metros cubicos")
print("Densidad =",Densidad,"kg/metros cubicos")

#VERIFICADOR
print("VERIFICADOR:")
formula_excesiva_de_la_densidad=(Densidad>100)
print("ES UNA FORMULA EXCESIVA DE LA DENSIDAD:",formula_excesiva)
print("")

#CALCULADORA NRO15
#ESTA CAlCULADORA REALIZA EL CALCULO DE PRECION HIDROSTATICA

#DECLARACION DE VARIABLES
densidad_del_liquido,gravedad,Altura,precion_hidrostatica=0.0,0.0,0.0,0.0

#CALCULADORA
densidad_del_liquido=50.2
gravedad=10.0
altura=5145.0
precion_hidrostatica=densidad_del_liquido*gravedad*altura

#MOSTRAR DATOS
print("densidad del liquido =",densidad_del_liquido,"kg/metros cubicos")
print("gravedad =",gravedad,"m/segundos al cuadrado")
print("altura =",altura,"m")
print("Precion hidrostatica =",precion_hidrostatica,"pa")

#VERIFICADOR
print("VERIFICADOR:")
formula_excesiva_de_la_preciohidrostatica=(precion_hidrostatica>300)
print("LA FORMULA DE LA PRECION HIDROSTATICA ES EXCESIVA:",formula_excesiva_primera_leytermodinamica)
print("")

#CALCULADORA NRO16
#ESTA CAlCULADORA REALIZA EL CALCULO DEL AREA TOTAL DE UN PRISMA

#DECLARACION DE VARIABLES
area_lateral,area_de_su_base,area_total=0.0,0.0,0.0

#CALCULADORA
area_lateral=54.7
area_de_su_base=100.7
area_total=(area_lateral+2*area_de_su_base)

#MOSTRAR DATOS
print("area lateral =",area_lateral)
print("are de su base =",area_de_su_base)
print("area total de un prisma =",area_total)

#VERIFICADOR
print("VERIFICADOR:")
area_del_prisma_exede=(area_total>150)
print("EL AREA DEL PRISMA EXEDE:",area_del_prisma_exede)
print("")

#CALCULADORA NRO17
#ESTA CAlCULADORA REALIZA EL CALCULO DEL VOLUMEN DE UNA PIRAMIDE

#DECLARACION DE VARIABLES
Area_de_su_base,ALtura,volumen_de_piramide=0.0,0.0,0.0

#CALCULADORA
Area_de_su_base=5247.5
ALtura=87.5
volumen_de_piramide=((Area_de_su_base*altura)/3)

#MOSTRAR DATOS
print("Area de su base =",Area_de_su_base)
print("ALtura =",ALtura)
print("Volumen de Piramide =",volumen_de_piramide)

#VERIFICADOR
print("VERIFICADOR:")
volumen_de_un_prima_exede=(volumen_de_piramide>200)
print("EL VOLUMEN DEL PRISMA EXCEDE:",volumen_de_un_prima_exede)
print("")

#CALCULADORA NRO18
#ESTA CAlCULADORA REALIZA EL CALCULO DEL TRABAJO

#DECLARACION DE VARIABLES
Fuerza,Distancia,Trabajo=0.0,0.0,0.0

#CALCULADORA
Fuerza=5442.4
Distancia=7845.0
Trabajo=Fuerza*Distancia

#MOSTRAR DATOS
print("Fuerza =",Fuerza,"m/segundos al cuadrado")
print("Distancia =",Distancia,"m")
print("Trabajo =",Trabajo,"Joule")

#VERIFICADOR
print("VERIFICADOR:")
calculo_del_trabajo_exede=(Trabajo>600)
print("EL CALCULO DEL TRABJO EXCEDE:",calculo_del_trabajo_exede)
print("")

#CALCULADORA NRO19
#ESTA CAlCULADORA REALIZA EL CALCULO DE LA ENERGIA CINETICA

#DECLARACION DE VARIABLES
MAsa,Velocidad,Energia_cinetica=0.0,0.0,0.0

#CALCULADORA
MAsa=547.1
Velocidad=754.4
Energia_cinetica=1/2*MAsa*(Velocidad**2)

#MOSTRAR DATOS
print("masa =",MAsa,"kg")
print("velocidad =",Velocidad,"m/s")
print("Energia Cinetica =",Energia_cinetica,"Joule")

#VERIFICADOR
print("VERIFICADOR:")
formula_excesiva_de_la_energiacinetica=(Energia_cinetica>200)
print("EL CALCULO DE LA ENERGIA CINETICA EXCEDE:",formula_excesiva_de_la_energiacinetica)
print("")

#CALCULADORA NRO20
#ESTA CAlCULADORA REALIZA EL CALCULO DE LA ENERGIA POTENCIAL GRAVITACIONAL

#DECLARACION DE VARIABLES
MASA,GRAVEDAD,ALTURA,ENERGIA_POTENCIAL_GRAVITACIONAL=0.0,0.0,0.0,0.0

#CALCULADORA
MASA=78.4
GRAVEDAD=10.0
ALTURA=100.0
ENERGIA_POTENCIAL_GRAVITACIONAL=MASA*GRAVEDAD*ALTURA

#MOSTRAR DATOS
print("MASA =",MASA,"kg")
print("GRAVEDAD =",GRAVEDAD,"m/segundos al cuadrados")
print("ALTURA =",ALTURA,"m")
print("ENERGIA_POTENCIAL_GRAVITACIONAL =",ENERGIA_POTENCIAL_GRAVITACIONAL,"Joule")

#VERIFICADOR
print("VERIFICADOR:")
formula_potenciagravitatoria_excede_=(ENERGIA_POTENCIAL_GRAVITACIONAL>500)
print("LA ENERGIA POTENCIAL EXCEDE:",formula_excesiva)
print("")
print("FIN DE PROGRAMA")
