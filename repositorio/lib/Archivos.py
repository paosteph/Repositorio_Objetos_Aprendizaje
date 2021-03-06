import os
import uuid
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import zipfile
from bs4 import BeautifulSoup

def get_file_path(instance, filename):
	"""
	Método que especifica la codificación para el nombre del archivo que se almacenará en el servidor.
	"""

	"""Se separa la cadena que representa el archivo."""
	ext = filename.split('.')[-1]
	"""
	puedo hacer una combinación para el nombre del archivo como quiera especificarlo... instance.tipo_obj
	Se ha agregado una codificación extra antes de la extensión con el fin de identificar el objeto subido por su nombre
	esta codificación extra está relacionada con el primary key del speclom asociado a la instancia del objeto que se sube.
	"""
	filename="%s_%s.%s" % (uuid.uuid4(), instance.espec_lom.pk, ext) #Se une la nueva codificación del nombre con la extensión.
	return os.path.join('objetos', filename) #Se devuelve el nuevo nombre como un ruta relativa.

def get_file_storage():
	"""
	método que permite especificar el lugar donde serán almacenados los archivos.

	...puede faltar un parámetro denominado base_url que literalmente permite:
	URL that serves the files stored at this location. If omitted, it will default to the value of your MEDIA_URL setting.
	"""
	fs = FileSystemStorage(location='/')
	return fs

def handle_uploaded_file(f):
	with open(settings.MEDIA_ROOT+'\\index\\'+f.name, 'wb') as destination:
		print(f.name)
		for linea in f:
			destination.write(linea)
		destination.close()

def descomprimir(fzip):
	fantasy_zip = zipfile.ZipFile(settings.MEDIA_ROOT+'\\index\\'+fzip.name) #ubicacion del zip
	fantasy_zip.extract('index.html', settings.MEDIA_ROOT+'\\index') #archEspecifico, ubicacionFinal

	fantasy_zip.close()

def extraerMetadatos():
	# abre archivo para leer contenido con beautifulsoup
	metadatos = []
	arch = open(settings.MEDIA_ROOT + '\\index\\' + 'index.html', 'r')
	contenido = arch.read()
	soup = BeautifulSoup(contenido, "html.parser")
	tituloExe = str(soup.title.string)
	metadatos.append(tituloExe)
	idiomaExe = 'sp'
	metadatos.append(idiomaExe)
	autorExe, descripcionExe, licenciaExe = '', '', ''
	for tag in soup.find_all('meta'):
		if tag.get('name') == 'author':
			autorExe = tag.get('content')
			metadatos.append(autorExe)
		elif tag.get('name') == 'description':
			descripcionExe = tag.get('content')
			metadatos.append(descripcionExe)
			break

	if autorExe == '':
		metadatos.append('Autor ExeLearning')
	if descripcionExe == '':
		metadatos.append('No ingreso breve descripcion del objeto de aprendizaje')

	for tag in soup.find_all('div'):
		if tag.get('id') == 'packageLicense':
			licenciaExe = tag.get('class')
			metadatos.append(licenciaExe[1])
			break

	if not licenciaExe:
		metadatos.append('Copyright')

	arch.close()

	return metadatos