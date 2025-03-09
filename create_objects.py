# Establece el entorno Django si aún no lo has hecho
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'album.settings')
django.setup()

from apps.fotos.models import Mifoto  # Ajusta la ruta de importación según tu estructura de proyecto

# 1. Estadio Atanasio Girardot (Medellín) - Sede de Atlético Nacional e Independiente Medellín
Mifoto.objects.create(
    nombre="Estadio Atanasio Girardot",
    descripcion="Estadio emblemático de Medellín, utilizado por Atlético Nacional e Independiente Medellín.",
    imageurl="https://imagenes.eltiempo.com/files/image_1200_600/uploads/2021/03/27/605f7d27b76ac.jpeg",
    ciudad="Medellín",
    capacidad=48700
)

# 2. Estadio Metropolitano Roberto Meléndez (Barranquilla) - Casa del Junior
Mifoto.objects.create(
    nombre="Estadio Metropolitano Roberto Meléndez",
    descripcion="Casa del Junior de Barranquilla, reconocido por su ambiente vibrante.",
    imageurl="https://www.barranquilla.gov.co/wp-content/uploads/2018/05/barranquilla_01488-e1526962960257.jpg",
    ciudad="Barranquilla",
    capacidad=50000
)

# 3. Estadio Nemesio Camacho El Campín (Bogotá) - Sede de Millonarios e Independiente Santa Fe
Mifoto.objects.create(
    nombre="Estadio Nemesio Camacho El Campín",
    descripcion="Sede de Millonarios e Independiente Santa Fe en Bogotá, con gran tradición futbolística.",
    imageurl="https://files.visitbogota.co/drpl/sites/default/files/2024-04/estadio-nemesio-camacho-campin-05.jpg",
    ciudad="Bogotá",
    capacidad=39512
)

# 4. Estadio Olímpico Pascual Guerrero (Cali) - Hogar del América de Cali
Mifoto.objects.create(
    nombre="Estadio Olímpico Pascual Guerrero",
    descripcion="Estadio histórico en Cali, hogar del América de Cali, con modernas instalaciones.",
    imageurl="https://www.visitcali.travel/wp-content/uploads/2022/11/Estadio-Olimpico-Pascual-Guerrero.jpg",
    ciudad="Cali",
    capacidad=35405
)

# 5. Estadio Deportivo Cali (Palmira) - Sede del Deportivo Cali
Mifoto.objects.create(
    nombre="Estadio Deportivo Cali",
    descripcion="Sede del Deportivo Cali, ubicado en Palmira, con gran pasión por el fútbol.",
    imageurl="https://staticprd.minuto30.com/wp-content/uploads/2024/10/6-Cali.jpg",
    ciudad="Palmira",
    capacidad=58000
)

# 6. Estadio Libertad (Pasto) - Casa del Deportivo Pasto
Mifoto.objects.create(
    nombre="Estadio Libertad",
    descripcion="Estadio en Pasto, casa del Deportivo Pasto, conocido por su ambiente único en altitud.",
    imageurl="https://upload.wikimedia.org/wikipedia/commons/f/fa/Estadio_Departamental_Libertad.jpg",
    ciudad="Pasto",
    capacidad=19000
)

# 7. Estadio Alfonso López (Bucaramanga) - Sede del Atlético Bucaramanga
Mifoto.objects.create(
    nombre="Estadio Alfonso López",
    descripcion="Sede del Atlético Bucaramanga, con una rica historia en el fútbol regional.",
    imageurl="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQ1sWFfJAaZOWEhhH194AbGp1k-eYroi-81WhbJTkq973fGaTBXC9v_FilRJnVgaRtTAE&usqp=CAU",
    ciudad="Bucaramanga",
    capacidad=17600
)

# 8. Estadio Palogrande (Manizales) - Hogar del Once Caldas
Mifoto.objects.create(
    nombre="Estadio Palogrande",
    descripcion="Estadio icónico en Manizales, hogar del Once Caldas, reconocido por su ambiente festivo.",
    imageurl="https://nacionalespasion.com.co/wp-content/uploads/2024/05/20240527_133812.jpg",
    ciudad="Manizales",
    capacidad=32000
)

# 9. Estadio Manuel Murillo Toro (Ibagué) - Sede del Deportes Tolima
Mifoto.objects.create(
    nombre="Estadio Manuel Murillo Toro",
    descripcion="Estadio en Ibagué, sede del Deportes Tolima, conocido por su infraestructura moderna.",
    imageurl="https://upload.wikimedia.org/wikipedia/commons/2/25/Estadio_Murillo_Toro.jpg",
    ciudad="Ibagué",
    capacidad=28100
)

# 10. Estadio Guillermo Plazas Alcid (Neiva) - Sede del Atlético Huila
Mifoto.objects.create(
    nombre="Estadio Guillermo Plazas Alcid",
    descripcion="Sede del Atlético Huila, ubicado en Neiva, con pasión futbolera en cada partido.",
    imageurl="https://footballtripper.com/wp-content/uploads/estadio-guillermo-plazas-alcid.jpg",
    ciudad="Neiva",
    capacidad=15000
)

# 11. Estadio Centenario (Armenia) - Sede del Deportes Quindío
Mifoto.objects.create(
    nombre="Estadio Centenario",
    descripcion="Estadio en Armenia, sede del Deportes Quindío, reconocido por su atmósfera vibrante.",
    imageurl="https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/Estadio_Centenario_%28vista_a%C3%A9rea%29.jpg/1280px-Estadio_Centenario_%28vista_a%C3%A9rea%29.jpg",
    ciudad="Armenia",
    capacidad=23500
)

# 12. Estadio La Comba (Barrancabermeja) - Casa del Alianza Petrolera
Mifoto.objects.create(
    nombre="Estadio La Comba",
    descripcion="Estadio en Barrancabermeja, casa del Alianza Petrolera, pequeño pero con gran energía.",
    imageurl="https://pbs.twimg.com/media/E-i5KBaWUAQUBWQ.jpg",  # URL de imagen de ejemplo o placeholder
    ciudad="Barrancabermeja",
    capacidad=9000
)

# 13. Estadio Hernán Ramírez Villegas (Pereira) - Hogar del Deportivo Pereira
Mifoto.objects.create(
    nombre="Estadio Hernán Ramírez Villegas",
    descripcion="Estadio en Pereira, hogar del Deportivo Pereira, reconocido por su ambiente acogedor.",
    imageurl="https://olimpicocol.co/web/wp-content/uploads/2022/07/Estadio.jpeg",
    ciudad="Pereira",
    capacidad=30297
)

# 14. Estadio Cívico de Tunja (Tunja) - Sede del Patriotas Boyacá
Mifoto.objects.create(
    nombre="Estadio Cívico de Tunja",
    descripcion="Estadio en Tunja, sede del Patriotas Boyacá, con un diseño moderno y vibrante.",
    imageurl="https://www.boyacaleinforma.com/wp-content/uploads/2024/10/uhn.jpg",
    ciudad="Tunja",
    capacidad=14000
)

# 15. Estadio Jaime Morón León (Santa Marta) - Hogar del Unión Magdalena
Mifoto.objects.create(
    nombre="Estadio Jaime Morón León",
    descripcion="Estadio en Santa Marta, hogar del Unión Magdalena, reconocido por su historia y pasión.",
    imageurl="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6SmlrE1ZC5RzilWd3TV099NTBL99D4v65NQ&s",
    ciudad="Santa Marta",
    capacidad=16000
)

# 16. Estadio Cacique (Montería) - Sede de Jaguares de Córdoba
Mifoto.objects.create(
    nombre="Estadio Cacique",
    descripcion="Estadio en Montería, sede de Jaguares de Córdoba, que destaca por su ambiente caribeño.",
    imageurl="https://estadiosfc.com/wp-content/uploads/2023/06/Estadio-Cacique-Diriangen.webp",
    ciudad="Montería",
    capacidad=18000
)
