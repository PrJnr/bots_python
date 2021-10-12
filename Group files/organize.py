import os
import shutil

downloads_dir = r"C:\Users\Paulo\Downloads"
current_dir = downloads_dir 

all_files = os.listdir(current_dir)
all_fext = []

#Dividir as extensões de arquivos do diretorio
for f in all_files:
	_, fext = os.path.splitext(f)
	if fext not in all_fext:
		all_fext.append(fext)


#Criar todos os diretórios
for ext in all_fext:
	if ext:
		os.mkdir(os.path.join(current_dir, ext))

#Mover todos os arquivos para os diretorios
for f in all_files:
	_, ext = os.path.splitext(f)
	old_path = os.path.join(current_dir, f)
	new_path = os.path.join(current_dir, ext, f)
	os.rename(old_path, new_path)

