#! python3.
import os, sys


def createIndex(proyectDir):
    indexFile = open(os.path.join(os.getcwd(),proyectDir,'index.html'),'w')
    indexFile.write('<!DOCTYPE html>')
    indexFile.write('<html lang="en">\n')
    indexFile.write('<head>\n <meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n <meta http-equiv="X-UA-Compatible" content="ie=edge">\n <title>Document</title>\n <link rel="stylesheet" href="style.css"> \n </head>\n')
    indexFile.write("<body> \n <h1>Hi, This is your SlothHtml Template</h1> \n </body>\n")
    indexFile.write("</html>")

    print('creado index.html')

def createCSS(proyectDir):
    cssDir = os.path.join(proyectDir,'css')
    os.makedirs(cssDir)
    cssFile = open(os.path.join(os.getcwd(),cssDir,'styles.css'),'w')
    cssFile.close()
    print('creado directorio css')

def createJS(proyectDir):
    jsDir = os.path.join(proyectDir,'js')
    os.makedirs(jsDir)
    jsFile = open(os.path.join(os.getcwd(),jsDir,'scripts.js'),'w')
    jsFile.close()
    print('creado directorio js')

def createAssets(proyectDir):
    os.makedirs(os.path.join(proyectDir,'assets'))
    print('creado directorio assets')


"creamos la carpeta de proyecto"
proyectName = sys.argv[1]
proyectDir = os.path.join(os.getcwd(), proyectName)

try:
    os.makedirs(proyectDir)
    createCSS(proyectDir)
    createJS(proyectDir)
    createAssets(proyectDir)
    createIndex(proyectDir)
    print('proyecto creado con exito')
except FileExistsError:
    print('no se puede crear el proyecto en:', proyectDir,'ya que existe un directorio con ese nombre')


