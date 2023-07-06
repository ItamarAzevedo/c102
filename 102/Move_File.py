import os
import shutil

from_dir="C:/Users/junin"
to_dir="C:/Users/junin/OneDrive/Documentos/BYJU's"

listOfFiles=os.listdir(from_dir)
print(listOfFiles)

for fileName in listOfFiles:
    name,extension=os.path.splitext(fileName)
    
    if extension=="":
        continue
    if extension in ['.txt', '.pdf', '.doc', '.docx']:
        path1 = from_dir + '/' + file_name # Exemplo path1 : Downloads/nomeImagem1.jpg 
        path2 = to_dir + '/' + "Arquivos_Documentos" # Exemplo path2 : D:/Meus Arquivos/Arquivos_Imagem
        path3 = to_dir + '/' + "Arquivos_Documentos" + '/' + file_name # Exemplo path3 : D:/Meus Arquivos/Arquivos_Imagem/nomeImagem1.jpg #print("path1 " , path1) #print("path3 ", path3) # Verifique se o caminho da pasta/diretório existe antes de mover # Caso contrário, crie uma NOVA pasta/diretório, e então mova 
        if os.path.exists(path2):
            print("Movendo " + file_name + ".....") # Mover de path1 ---> path3 
            shutil.move(path1, path3) 
        else:
            os.makedirs(path2)
            print("Movendo " + file_name + ".....") 
            shutil.move(path1, path3)