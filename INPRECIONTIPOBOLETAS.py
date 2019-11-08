print("PROGRAMAS CON INPRECION BOLETAS")
print("ALUMNO:CARLOS RONALDO LIZA DAMIAN")
print("")

#BOLETA NRO 01
#INPUT
nombre=input("CLIENTE:")
mesero=input("MESERO:")

platos_de_cabrito=int(input("CANTIDAD DE PLATOS DE CABRITO:"))
jarras_de_jugo_de_naranja=int(input("CANTIDAD DE JARRAS DE JUGOS DE NARANJA:"))
papa_a_la_huancaina=int(input("CANTIDAD DE PAPAS A LA HUANCAINA:"))

costo_de_platos_cabrito=float(input("PRECIO U. DE PLATOS DE CABRITO:"))
costo_de_jarras_de_jugos_de_naranja=float(input("PRECIO U. DE JARRAS DE JUGO DE NARNJA:"))
costo_de_papa_a_la_huancaina=float(input("PRECIO U. DE PAPAS A LA HUANCAINA:"))

#PROCESSING
total_de_costo_de_platos_de_cabrito=platos_de_cabrito*costo_de_platos_cabrito
total_de_jarradejugonaranja=jarras_de_jugo_de_naranja*costo_de_jarras_de_jugos_de_naranja
total_de_papas_huancaina=papa_a_la_huancaina*costo_de_papa_a_la_huancaina

cosumo=total_de_costo_de_platos_de_cabrito+total_de_jarradejugonaranja+total_de_papas_huancaina
IGV=8.5
total_pagar=cosumo+IGV

#VERIFICADOR
comprador_compulsivo=(total_pagar>150)

#OUTPUT
print("")
print("#############################################################################")
print("#                        RESTAURANTE _ SABROSITO                          ###")
print("#############################################################################")
print("### CLIENTE: ",nombre,"                  MESERO:",mesero,"                ###")
print("#############################################################################")
print(" PRODUCTO            CANTIDAD      P.U.         TOTAL        ")
print("# CABRITO:             ",platos_de_cabrito,"        ",costo_de_platos_cabrito ,"        ",total_de_costo_de_platos_de_cabrito,"$ ")
print("# JUGO DE NARANJA:     ",jarras_de_jugo_de_naranja ,"        ",costo_de_jarras_de_jugos_de_naranja,"        ",total_de_jarradejugonaranja,"$         ")
print("# PAPA A LA HUANCAINA: ",papa_a_la_huancaina,"        ",costo_de_papa_a_la_huancaina,"        ",total_de_papas_huancaina,"$            ")
print("##############################################################################")
print("CONSUMO:          ",cosumo,"$                                                 ")
print("IGV:              ",IGV,"                                                     ")
print("TOTAL A PAGAR:    ",total_pagar,"$                                            ")
print("##############################################################################")
print("COMPRADOR COMPULSIVO?:",comprador_compulsivo)
print("")
print("")

#BOLETA NRO 02
#INPUT
velocidad_inicial=float(input("VELOCIDAD INICIAL:"))
aceleracion=float(input("ACELERACION:"))
tiempo=float(input("TIEMPO:"))

#PROCESSING
velocidad_final=velocidad_inicial+aceleracion*tiempo

#VERIFICADOR
formula_mru_excede=(velocidad_final>50)

#OUTPUT
print("")
print("###########################################")
print("#            FORMULA DE MRUV              #")
print("###########################################")
print("# FORMULA:Vf=Vi+a.t                       #")
print("###########################################")
print("# VELOCIDAD INICIAL: ",velocidad_inicial," ")
print("# ACELERACION:       ",aceleracion,"       ")
print("# TIEMPO:            ",tiempo,"            ")
print("###########################################")
print("# VELOCIDAD FINAL:   ",velocidad_final,"   ")
print("###########################################")
print("FORMULA EXEDE?:",formula_mru_excede)
print("")
print("")

#BOLETA NRO 03
#INPUT
resistencia_inicial=float(input("RESISTENCIA INICIAL:"))
coeficiente_de_T=float(input("COEFICIENTE DE TEMPERATURA:"))
variacion_de_T=float(input("TIEMPO:"))

#PROCESSING
resistencia_final=resistencia_inicial+resistencia_inicial*coeficiente_de_T*variacion_de_T

#VERIFICADOR
formula_resistenciaelectrica_excede=(resistencia_final>200)

#OUTPUT
print("")
print("#########################################################")
print("#           FORMULA DE RESISTENCIA ELECTRICA            #")
print("#########################################################")
print("# FORMULA:Rf=Ri+Ri.&.T                                  #")
print("#########################################################")
print("# RESISTENCIA INICIAL:        ",resistencia_inicial,"ohm ")
print("# COEFICIENTE DE TEMPERATURA: ",coeficiente_de_T,"       ")
print("# VARIACION DE TEMPERATURA:   ",variacion_de_T,"c        ")
print("#########################################################")
print("# RESISTENCIA FINAL:          ",resistencia_final,"w     ")
print("#########################################################")
print("FORMULA DE LA RESISTENCIA EXCEDE?:",formula_resistenciaelectrica_excede)
print("")
print("")

#BOLETA NRO 04
#INPUT
Base_mayor=float(input("BASE MAYOR:"))
Base_menor=float(input("BASE MENOR:"))
altura=float(input("ALTURA:"))

#PROCESSING
area_trapecio=((Base_mayor+Base_menor)/2*2)

#VERIFICADOR
area_trapecio_excede=(area_trapecio>150)

#OUTPUT
print("")
print("##########################################")
print("#           AREA DEL TRAPECIO            #")
print("##########################################")
print("# FORMULA:A=(B+b/2)*h                    #")
print("##########################################")
print("# BASE MAYOR:    ",Base_mayor,"           ")
print("# BASE MENOR:    ",Base_menor,"           ")
print("# ALTURA:        ",altura,"               ")
print("########################### ##############")
print("# AREA TRAPECIO: ",area_trapecio,"        ")
print("##########################################")
print("AREA DEL TRAPECIO EXCEDE?:",area_trapecio_excede)
print("")
print("")

#BOLETA NRO 05
#INPUT
cliente=input("EL NOMBRE DEL CLIENTE:")
kg=int(input("INGRESE LA CANTIDAD DE KG DE LUCUMA:"))
pu=float(input("INGRESE PRECIO UNITARIO:"))

#PROCESSING
total=kg*pu

#VERIFICADOR
Comprador_compulsivo=(total>200)

#OUTPUT
print("")
print("#################################")
print("#        BOLETA DE VENTA        #")
print("#################################")
print("#                                ")
print("# CLIENTE: ",cliente,"           ")
print("# ITEM:    ",kg,"kg              ")
print("# P.U:     ",pu,"$               ")
print("# TOTAL:   ",total,"$            ")
print("#################################")
print("COMPRADOR COMPULSIVO?:",Comprador_compulsivo)
print("")
print("")

#BOLETA NRO 06
#INPUT
comprador=input("INGRESE EL NOMBRE DEL COMPRADOR:")
vendedor=input("INGRESE EL NOMBRE DEL VENDEDOR:")

cemento=int(input("INGRESE LA CANTIDAD DE BOLSAS DE CEMENTO:"))
yeso=int(input("INGRESE LA CANTIDAD DE BOLSAS DE YESO:"))
tubos=int(input("INGRESE LA CANTIDAD DE TUBOS:"))

precio_cemento=float(input("PRECIO U. DEL CEMENTO:"))
precio_yeso=float(input("PRECIO U. DEL YESO:"))
precio_tubos=float(input("PRECIO U. DE LOS TUBOS:"))

#PROCESSING
pagar=cemento*precio_cemento+yeso*precio_yeso+tubos*precio_tubos

#VERIFICADOR
COMPRADOR_compulsivo=(pagar>180)

#OUTPUT
print("")
print("#######################################################")
print("#               FERRETERIA DON JOSE                   #")
print("#######################################################")
print("# COMPRADOR:",comprador,"   VENDEDOR:",vendedor,"     #")
print("#######################################################")
print("# PRODUCTO      CANTIDAD     P.U                       ")
print("# CEMENTO:       ",cemento,"        ",precio_cemento," ")
print("# YESO:          ",yeso,"        ",precio_yeso,"       ")
print("# TUBOS:         ",tubos,"        ",precio_tubos,"     ")
print("#######################################################")
print("# TOTAL A PAGAR: ",pagar,"$                            ")
print("#######################################################")
print("COMPRADOR COMPULSIVO?:",COMPRADOR_compulsivo)
print("")
print("")

#BOLETA NRO 07
#INPUT
densidad_liquido=float(input("DENSIDAD DEL LIQUIDO:"))
gravedad=float(input("GRAVEDAD:"))
Altura=float(input("ALTURA:"))

#PROCESSING
precion_hidrostatica=densidad_liquido*gravedad*Altura

#VERIFICADOR
formula_precionhidrostatica_excede=(precion_hidrostatica>200)

#OUTPUT
print("")
print("#####################################################")
print("#        FORMULA DE LA PRECION HIDROSTATICA         #")
print("#####################################################")
print("# FORMULA:Ph=Di.g.h                                 #")
print("#####################################################")
print("# DENSIDAD DEL LIQUIDO: ",densidad_liquido,"kg/m.m.m ")
print("# GRAVEDAD:             ",gravedad,"m/s.s            ")
print("# ALTURA:               ",Altura,"m                  ")
print("#####################################################")
print("# PRECION HIDROSTATICA: ",precion_hidrostatica,"     ")
print("#####################################################")
print("PRECION HIDROSTATICA EXCEDE?:",formula_precionhidrostatica_excede)
print("")
print("")

#BOLETA NRO 08
#INPUT
COMPRADOR=input("INGRESE EL NOMBRE DEL COMPRADOR:")
vendedora=input("INGRESE EL NOMBRE DEL VENDEDORA:")

televisor=int(input("INGRESE LA CANTIDAD DE TELEVISORES:"))
dvd=int(input("INGRESE LA CANTIDAD DE DVD:"))
refrigeradora=int(input("INGRESE LA CANTIDAD DE REFRIGERADORAS:"))

precio_televisor=float(input("PRECIO U. DEL TELEVISOR:"))
precio_dvd=float(input("PRECIO U. DEL DVD:"))
precio_refrigeradoras=float(input("PRECIO U. DE REFRIGERADORAS:"))

#PROCESSING
PAGAR=televisor*precio_televisor+dvd*precio_dvd+refrigeradora*precio_refrigeradoras

#VERIFICADOR
COMPRADOR_COMPULSIVO=(PAGAR>50000)

#OUTPUT
print("")
print("###############################################################")
print("#                         LA CURACAO                          #")
print("###############################################################")
print("# COMPRADOR:",COMPRADOR,"   VENDEDOR:",vendedora,"            #")
print("###############################################################")
print("# PRODUCTO      CANTIDAD     P.U                               ")
print("# TELEVISORES:    ",televisor,"       ",precio_televisor,"      ")
print("# DVD:            ",dvd,"       ",precio_dvd,"            ")
print("# REFRIGERADORAS: ",refrigeradora,"       ",precio_refrigeradoras," ")
print("###############################################################")
print("# TOTAL A PAGAR:  ",PAGAR,"$                                   ")
print("###############################################################")
print("COMPRADOR COMPULSIVO?:",COMPRADOR_COMPULSIVO)
print("")
print("")

#BOLETA NRO 09
#INPUT
masa=float(input("MASA:"))
Gravedad=float(input("GRAVEDAD:"))
ALTURA=float(input("ALTURA:"))

#PROCESSING
energia_potencial_G=masa*Gravedad*ALTURA

#VERIFICADOR
energia_potencial_excede=(energia_potencial_G>180)

#OUTPUT
print("")
print("##############################################################")
print("#       FORMULA DE LA ENERGIA POTENCIAL GRAVITACIONAL        #")
print("##############################################################")
print("# FORMULA:Eg=m*g*h                                           #")
print("##############################################################")
print("# MASA:        ",masa,"kg                                     ")
print("# GRAVEDAD:    ",Gravedad,"m/s.s                              ")
print("# ALTURA:      ",ALTURA,"m                                    ")
print("##############################################################")
print("# ENERGIA POTENCIAL GRAVITACIONAL:",energia_potencial_G,"Joule")
print("##############################################################")
print("ENERGIA POTENCIAL GRAVITACIONAL EXCEDE?:",energia_potencial_excede)
print("")
print("")

#BOLETA NRO 10
#INPUT
coeficiente_dilatacion_cubica=float(input("DILATACION CUBICA:"))
volumen_inicial=float(input("VOLUMEN INICIAL:"))
VARIACION_temperatura=float(input("VARIACION DE TEMPERATURA:"))

#PROCESSING
variacion_volumen=coeficiente_dilatacion_cubica*volumen_inicial*VARIACION_temperatura

#VERIFICADOR
dilatacion_cubica_excede=(variacion_volumen>50)

#OUTPUT
print("")
print("#########################################################################")
print("#                   FORMULA DE LA DILATACION CUBICA                     #")
print("#########################################################################")
print("# FORMULA:vV=&*Vi*vT                                                    #")
print("#########################################################################")
print("# COEFICIENTE DE DILATACION CUBICA(3&):",coeficiente_dilatacion_cubica," ")
print("# VOLUMEN INICIAL:                    ",volumen_inicial,"m.m.m           ")
print("# VARIACION DE TEMPERATURA:           ",VARIACION_temperatura,"c°        ")
print("#########################################################################")
print("# VARIACION DE VOLUMEN:",variacion_volumen,"                             ")
print("#########################################################################")
print("VARIACION DE VOLUMEN EXCEDE?:",dilatacion_cubica_excede)
print("")
print("FIN DE PROGRAMA")
print("")
print("")

print("ALUMNO:JHONATON ROJAS CUBAS")
print("")

#calculadora nro1
#esta calculadora realiza el calculo de área del trapecio(en metros cuadrados)

#declaracion de variables
Base_mayor,altura,base_menor,area_trapecio,relacion_area=0.0,0.0,0.0,0.0,False

#input
Base_mayor=float(input("ingrese base mayor:"))
base_menor=float(input("ingrese base menor:"))
altura=float(input("ingrese altura:"))

#processing
area_trapecio=((Base_mayor+base_menor)/2)*altura

#verificador
relacion_area=(area_trapecio>100)

#Output
print("*************************************************")
print("*                ÁREA DEL TRPECIO               *")
print("*************************************************")
print("*la Base mayor:",Base_mayor,"                            *")
print("*la base menor:",base_menor,"                            *")
print("*la altura:",altura,"                                *")
print("*el area del Trapecio:",area_trapecio,"                     *")
print("*El Area supera los 100 mtrs cuadrados ?:",relacion_area,"  *")
print("*************************************************")
print("")
print("")


#calculadora nro2
#esta calculadora realiza el calculo de el promedio de tres notas

#declaracion de variables
nota1,nota2,nota3,promedio,relacion_promedio=0.0,0.0,0.0,0.0,False

#input
nota1=float(input("ingrese Nota1:"))
nota2=float(input("ingrese Nota2:"))
nota3=float(input("ingrese Nota3:"))

#procesing
promedio=(nota1+nota2+nota3)/3

#verificador
relacion_promedio=(11.5<promedio)

#Output
print("***************************************************")
print("*     PROMEDIO FINAL DEL CURSO DE HISTORIA        *")
print("***************************************************")
print("*la nota1 es:",nota1,"                             *")
print("*la nota2 es:",nota2,"                             *")
print("*la nota3 es:",nota3,"                            *")
print("*el promedio final es:",promedio,"               *")
print("*el promedio es aprobatorio ?:",relacion_promedio,"  *")
print("***************************************************")
print("")


#calculadora nro3
#esta calculadora realiza el calculo de el volumen en (metros cúbicos) de un prisma cuadrangular

#declaracion de variables
Area_de_la_base,altura,Volumen,relacion_volumen=0.0,0.0,0.0,False

#input
Area_de_la_base=float(input("ingrese Area_de_la_base:"))
altura=float(input("ingrese altura:"))

#procesing
Volumen=Area_de_la_base*altura

#verificador
relacion_volumen=(50<Volumen)

#Output
print("***************************************************")
print("*       VOLUMEN DE UN PRISMA CUADRANGULAR         *")
print("***************************************************")
print("*el área de la base es:",Area_de_la_base,"         *")
print("*la altura es:",altura,"                           *")
print("*el Volumen del prima es:",Volumen,"metros cúbicos","*")
print("*el volumen supera los 50 metros cúbicos ?:",relacion_volumen,"*")
print("**************************************************************")
print("")

#calculadora nro4
#esta calculadora realiza el calculo de la Densidad en (kilogramos por metro cúbico) de una sustancia

#declaracion de variables
masa,Volumen,Densidad,relacion_densidad=0.0,0.0,0.0,False

#input
masa=float(input("ingrese masa:"))
Volumen=float(input("ingrese volumen:"))

#procesing
Densidad=masa/Volumen

#verificador
relacion_densidad=(35>Densidad)

#output
print("***************************************************")
print("*            DENSIDAD DE UNA SUSTANCIA            *")
print("***************************************************")
print("*la masa es:",masa,"Kgramo","                       *")
print("*el volumen es:,",Volumen,"metros cúbico","          *")
print("*la Densidad de la sustancia es:",Densidad,"Kgramos/metro cúbico"," *")
print("*la densidad no supera los 35 Kgramos/metro cúbico ?:",relacion_densidad,"*")
print("**********************************************************************")

print("")
#calculadora nro5
#esta calculadora realiza el calculo de el peso de una carga

#declaracion de variables
masa,gravedad_terrestre,peso,relacion_peso=0.0,0.0,0.0,False

#input
masa=float(input("ingrese masa:"))
gravedad_terrestre=float(input("ingrese gravedad:"))

#procesing
peso=masa*gravedad_terrestre

#verificador
relacion_peso=(1000<peso)

#output
print("***************************************************")
print("*               PESO DE UNA CARGA                 *")
print("***************************************************")
print("*la masa de la carga es:",masa,"Kgramo","     *")
print("*la gravedad terrestre es:",gravedad_terrestre,"   *")
print("*el peso de la carga es:",peso,"Newton","                   *")
print("*el peso supera los 1000 Newton ?:",relacion_peso,"       *")
print("**************************************************")

print("")
#calculadora nro6
#esta calculadora realiza el calculo de el valor de una caja se galletas

#declaracion de variables
nro_galletas,costo_galleta,valor_caja_galleta,relacion_valor_caja_galletass=0,0.0,0.0,False

#input
nro_galletas=int(input("ingrese nro de galletas:"))
costo_galleta=float(input("ingrese costo de galleta:"))

#procesing
valor_caja_galletas=nro_galletas*costo_galleta

#verificador
relacion_valor_caja_galletass=(40>valor_caja_galleta)

#output
print("***************************************************")
print("*          VALOR DE CAJA DE GALLETAS              *")
print("***************************************************")
print("*el numero de galletas es:",nro_galletas,"          *")
print("*el costo de cada galleta es:",costo_galleta,"centimos","  *")
print("*el valor de la caja de galletas es:",valor_caja_galletas,"soles","   *")
print("*el costo de la caja de galletas  no supera los S/40 ?:",relacion_valor_caja_galletass,"*")
print("**********************************************************************************************")


print("")
#calculadora nro7
#esta calculadora realiza el calculo de el pago del consumo de agua

#declaracion de variables
nro_litros,costo_cada_litro,pago_por_consumo,relacion_pago_por_consumo=0.0,0.0,0.0,False

#input
nro_litros=float(input("ingrese nro litros:"))
costo_cada_litro=float(input("ingrese costo_cada_litro:"))

#processing
pago_por_consumo=nro_litros*costo_cada_litro

#verificador
relacion_pago_por_consumo=(pago_por_consumo>30)

#otput
print("***************************************************")
print("*           PAGO POR CONSUMO DE AGUA              *")
print("***************************************************")
print("*el numero de litros es:",nro_litros,"            *")
print("*el costo de cada litro es:",costo_cada_litro,"soles","  *")
print("*el pago total por el consumo es: S/",pago_por_consumo,"   *")
print("*el pago total es mayor a S/30 ?:",relacion_pago_por_consumo," *")
print("************************************************************")

print("")
#calculadora nro8
#esta calculadora realiza el calculo de distancia que a rrecorrido un auto que realizo(M.R.U.V)

#declaracion de variables
velocidad_inicial,tiempo,aceleracion,distancia,relacion_distancia=0.0,0.0,0.0,0.0,False

#input
velocidad_inicial=float(input("ingrese velocidad inicial:"))
tiempo=float(input("ingrese tiempo:"))
aceleracion=float(input("ingrese aceleracion:"))

#processing
distancia=(velocidad_inicial*tiempo)+(aceleracion*tiempo**2)/2

#verificador
relacion_distancia=(70<distancia)

#otput
print("***************************************************")
print("*    DISTANCIA DE UN AUTO EN UN MOVIMIENTO(M.R.U.V)            *")
print("***************************************************")
print("*la velocidad inicial es:",velocidad_inicial,"metros por segundo","   * *")
print("*el tiempo en segundos es:",tiempo,"      *")
print("*la aceleracion es:",aceleracion,"metros/segundo al cuadrado","        *")
print("*la distancia que rrecorrio el auto es:",distancia,"metros","              *")
print("*la distancia es mayor que 70m ?:",relacion_distancia,"        *")
print("**********************************************************************")

print("")

print("")
#calculadora nro9
#esta calculadora realiza el calculo de la hipotenusa de un triangulo rectangulo en (centímetros)

#declarar variables
cateto1,cateto2,hipotenusa,relacion_hipotenusa=0.0,0.0,0.0,False

#input
cateto1=float(input("ingrese cateto1:"))
cateto2=float(input("ingrese cateto2:"))

#processing
hipotenusa=(cateto1**2+cateto2**2)**1/2

#verificador
relacion_hipotenusa=(10==hipotenusa)

#output
print("***************************************************")
print("*                  HIPOTENUSA                     *")
print("***************************************************")
print("*el cateto1 es:",cateto1,"                       *")
print("*el cateto2 es:",cateto2,"                      *")
print("*el valor de la hipotenusa es:",hipotenusa,"centímetros","*")
print("*la hipotenusa es igual a 5 ?:",relacion_hipotenusa,"  *")
print("**********************************************************")

print("")
#calculadora nro10

#esta calculadora realiza el calculo de convercion de temperaturas "desde una temperatura que esta en celcius(c) hacia kelvin(k) y luego a faringe(f)"

#declarar variables
temperatura_C,temperatura_K,temperatura_F,relacion_K,relacion_F=0.0,0.0,0.0,False,False

#input
temperatura_C=float(input("ingrese temperatura C:"))

#processing
temperatura_K=temperatura_C+273                  #formula: C=K-273
temperatura_F=(9*(temperatura_K)-2457+160)/5      #formula: F=(9K-2457+160)/5

#verificador
relacion_K=(313==temperatura_K)
relacion_F=(212==temperatura_F)

#output
print("***************************************************")
print("*         RELACION DE TEMPERATURAS                *")
print("***************************************************")
print("*la temperatura en grados celcius es:"+str(temperatura_C)+"°"+"   *")
print("*la temperatura en grados Kelvin es:"+str(temperatura_K)+"°"+"   *")
print("*la temperatura en grados Faringe es:"+str(temperatura_F)+"°"+"   *")
print("*la temperatura Kelvin es igual a 313° ?:",relacion_K,"    *")
print("*la temperatura Faringe es igual a 212° ?:",relacion_F,"   *")
print("*******************************************************************")
print("")
print("TRABAJO TERMINADO")
