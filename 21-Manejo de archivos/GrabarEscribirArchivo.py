try:
  archivo=open('./21-Manejo de archivos/prueba.txt','w', encoding='utf8')
  archivo.write('Hola!!, soy Goku!!! vacación..')
except Exception as e:
  print(f'Se ha producido un error: {e}')
finally:
    archivo.close()
    print('Archivo cerrado!')
    