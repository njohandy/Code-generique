import sys
import shutil
import os
from datetime import datetime

from pathlib import Path

# Récupère la lettre de la clé USB passée en argument
usb_drive = "D:"

# Chemin vers Mes Documents
user_docs = os.path.expanduser("C:/Users/Andy Njoh/Documents/")

# Dossier RECUPERATION
backup_folder = os.path.join(user_docs, "/Andy Njoh/Documents//RECUPERATION")

# Crée le dossier RECUPERATION s’il n’existe pas
os.makedirs(backup_folder, exist_ok=True)

# Dossier horodaté
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
destination = backup_folder
os.makedirs(destination, exist_ok=True)

gdrive_folder = os.path.expanduser("C:/Users/Andy Njoh/Google Drive/USB_BACKUP")
os.makedirs(gdrive_folder, exist_ok=True)

# Fonction de copie avec gestion des erreurs
def copy_content(src, dst):
    for root, dirs, files in os.walk(src):
        # Ignore les dossiers protégés comme "System Volume Information"
        if "System Volume Information" in root or "$RECYCLE.BIN" in root:
            continue

        rel_path = os.path.relpath(root, src)
        dest_dir = os.path.join(dst, rel_path)
        os.makedirs(dest_dir, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dest_dir, file)
            try:
                shutil.copy2(src_file, dst_file)
                print(f"✅ Copié : {src_file}")
            except PermissionError:
                print(f"⚠️  Accès refusé (ignoré) : {src_file}")
            except Exception as e:
                print(f"❌ Erreur pour {src_file} : {e}")

# Exécute la copie
copy_content(usb_drive, destination)
copy_content(usb_drive, gdrive_folder)

print(f"\n📁 Copie terminée dans : {destination}")
print(f"☁️ Copie vers Google Drive terminée dans : {gdrive_folder}")

