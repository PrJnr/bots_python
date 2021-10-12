import os
import shutil

#diretorio atual
current_dir = os.getcwd() 

# Agrupando arquivos do mesmo tipo.
for f in os.listdir(current_dir):
    filename, file_ext = os.path.splitext(f)

    try:
        if not file_ext:
            pass

        elif file_ext in ('.jpg', '.png', '.gif', '.jpeg', '.psd', '.svg'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Image files' ,f'{filename}{file_ext}')
            )
        elif file_ext in ('.wmv', '.mp4', '.avi', '.mpeg', '.mov'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Video files' ,f'{filename}{file_ext}')
            )
        elif file_ext in ('.doc', '.txt', '.xls', '.xlsx', '.xd', '.pdf', '.docx', ''):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Documents files' ,f'{filename}{file_ext}')
            )
        else :
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Other files' ,f'{filename}{file_ext}')
            )
    

    except (FileNotFoundError, PermissionError):
        pass