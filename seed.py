from app import create_app, db
from app.models import Almacen


app = create_app()


with app.app_context():

    existe_gdl = Almacen.query.filter_by(nombre="Almacen Guadalajara").first()#Estamos haciendo una consulta tipo query para saber si existe "Almacen Guadalajara"

    if not existe_gdl:#Lo busca, si no existe, lo creamos 


        almacen_gdl = Almacen(nombre= "Almacen Guadalajara",
                              ciudad= "Guadalajara")
        db.session.add(almacen_gdl)



    existe_cdmx = Almacen.query.filter_by(nombre="Almacen CDMX").first()#Estamos haciendo una consulta tipo query para saber si existe "Almacen CDMX"

    if not existe_cdmx:#Lo busca, si no existe, lo creamos

        almacen_cdmx = Almacen(nombre= "Almacen CDMX",
                               ciudad= "CDMX")

        
        db.session.add(almacen_cdmx)

        
    db.session.commit()          