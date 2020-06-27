# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    tabla1=BuscarTotal()
    tabla2=BuscarTotal2()
    return dict(tabla=tabla1,tabla3=tabla2)
def BuscarTotal():
    tabla=db.executesql('SELECT Servicios.id,Servicios.NombreServicio, Clientes.NombreCliente, Servicios.Costo,(Servicios.Costo-Clientes.BonoCliente) as Total                        FROM Servicios inner join Clientes on Clientes.id = Servicios.Cliente')
    return tabla
def BuscarTotal2():
    tabla=db(db.Clientes.id==db.Servicios.Cliente).select(db.Servicios.id,db.Servicios.NombreServicio, db.Clientes.NombreCliente, db.Servicios.Costo)
    return dict(tabla=tabla)
