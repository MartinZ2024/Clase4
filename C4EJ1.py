ges_tareas=[{"nombre":["Induccion"],"descripcion":["Presentar presentar procesos"],"estado":["Pendiente"]},
         {"nombre":["Modificar"],"descripcion":["Hoja 2 de procesos"],"estado":["Terminado"]} 
]
#print(ges_tareas)
ges_tareas.insert(2,{"nombre":["Verificar"],"descripcion":["Impresion procesos"],"estado":["Pendiente"]})
ges_tareas.insert(3,{"nombre":["Validar"],"descripcion":["Instrucciones"],"estado":["En proceso"]})
ges_tareas.insert(4,{"nombre":["Desarrollar"],"descripcion":["Proceso puesto 5"],"estado":["En proceso"]})
#print(ges_tareas)
ges_tareas.pop(3)
print("tareas restantes:")
l=len(ges_tareas)
print(ges_tareas[0:l])
