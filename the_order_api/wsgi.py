"""
WSGI config for the_order_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Configurar la variable de entorno para los ajustes de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_order_api.settings')

application = get_wsgi_application()

# Añadir WhiteNoise al objeto aplicación WSGI
application = WhiteNoise(application, root=os.path.join(os.environ.get('BASE_DIR', ''), 'staticfiles'))

# Opcional: si tienes otros directorios estáticos puedes agregarlos así:
# application.add_files('/path/to/other/static/files', prefix='more-files/')

