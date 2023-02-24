import requests
import os 
from PIL import Image
from IPython.display import IFrame

# descargar el archvios Example1.txt desde la "url" y lo guarda en la carpeta principal como "example1.txt"
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
path=os.path.join(os.getcwd(),'example1.txt')
r=requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
    
