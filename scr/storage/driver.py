from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

from utility.image import (
    delete_image, download_image
)


class GoogleDriver:
    def __init__(self, creds_path: str):
        self._cred_path = creds_path

    def share_file_with_user(self, file_id):
        creds = Credentials.from_service_account_file(self._cred_path)
        service = build('drive', 'v3', credentials=creds)

        permission = {
            'type': 'user',
            'role': 'reader',
            'emailAddress': "udimeuimovel@gmail.com"
        }

        try:
            service.permissions().create(
                fileId=file_id,
                body=permission,
                fields='id'
            ).execute()
            print("Arquivo ou pasta compartilhado.")
        except Exception as e:
            print(f"Erro ao compartilhar arquivo: {e}")

    def create_public_folder(self, folder_name):
        creds = Credentials.from_service_account_file(self._cred_path)
        service = build('drive', 'v3', credentials=creds)

        folder_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = service.files().create(
            body=folder_metadata, fields='id, webViewLink'
        ).execute()

        folder_id = folder.get('id')

        permission = {
            'type': 'anyone',
            'role': 'reader'
        }

        service.permissions().create(
            fileId=folder_id,
            body=permission
        ).execute()

        return folder_id

    def upload_image_to_drive(self, image_path, image_name, folder_id):
        creds = Credentials.from_service_account_file(self.cred_path)
        service = build('drive', 'v3', credentials=creds)

        file_metadata = {
            'name': image_name,
            'parents': [folder_id]
        }

        media = MediaFileUpload(image_path, mimetype='image/webp')

        file = service.files().create(
            body=file_metadata, media_body=media, fields='id'
        ).execute()

        permission = {
            'type': 'anyone',
            'role': 'reader'
        }

        service.permissions().create(
            fileId=file.get('id'), body=permission
        ).execute()

        public_link = f"https://drive.google.com/uc?id={file.get('id')}"
        return public_link

    def list_files_in_drive(self, service):
        creds = Credentials.from_service_account_file(self.cred_path)
        service = build('drive', 'v3', credentials=creds)

        results = service.files().list(
            pageSize=100, fields="nextPageToken, files(id, name, mimeType)"
        ).execute()

        items = results.get('files', [])

        if not items:
            print('Nenhum arquivo ou pasta encontrado.')
        else:
            print('Arquivos e pastas encontrados:')
            for item in items:
                print(f"{item['name']} ({item['id']}) - {item['mimeType']}")


if __name__ == '__main__':

    drive = GoogleDriver('client_secrets.json')
    folder_id = "1htDOVvWcdVkUcETw-sOGUqkmux_MkGWc"

    base = "https://resizedimgs.zapimoveis.com.br/fit-in/870x707/vr.images.sp/"
    image_urls = [
        '5abc8dba84fc3c919ab2620b609d5a27.webp',
        'fd4e0c11fcc1f4cfc81a2fc0c0dc61d9.webp'
    ]
    for i, url in enumerate(image_urls):
        filename = f'image_{i+1}.webp'
        image_path, image_filename = download_image(base + url, filename)

        link = drive.upload_image_to_drive(
            image_path,
            image_filename,
            folder_id
            )
        print(link)

        delete_image(image_path)
