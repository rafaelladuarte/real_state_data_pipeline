from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

# from scripts.utility.image import (
#     delete_image, download_image
# )
from scripts.infra.security.secrets import get_secret_value


class GoogleDriver:
    def __init__(self, creds_path: str, folder_id: str):
        self._cred_path = creds_path
        self._folder_id = folder_id

    def share_file_with_user(self, file_id: str) -> None:
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

    def create_public_folder(self, folder_name: str) -> str:
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

    def upload_image_to_drive(
        self,
        image_path: str,
        image_name: str,
        folder_id: str = None
    ) -> str:
        if not folder_id:
            folder_id = self._folder_id

        creds = Credentials.from_service_account_file(self._cred_path)
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

    def list_folder_in_drive(self) -> list[dict] | None:
        creds = Credentials.from_service_account_file(self._cred_path)
        service = build('drive', 'v3', credentials=creds)

        results = service.files().list(
            q="mimeType='application/vnd.google-apps.folder'",
            pageSize=1000,
            fields="nextPageToken, files(id, name)"
        ).execute()

        items = results.get('files', [])

        if not items:
            print('Nenhum arquivo ou pasta encontrado.')
            return None
        else:
            print(f'Arquivos e pastas encontrados: {len(items)}')

            return items

    def delete_folder(
        self,
        folder_id: str = None
    ) -> None:
        if not folder_id:
            folder_id = self._folder_id

        creds = Credentials.from_service_account_file(self._cred_path)
        service = build('drive', 'v3', credentials=creds)

        try:
            service.files().delete(fileId=folder_id).execute()
            print(f"Pasta com ID {folder_id} foi apagada.")
        except Exception as e:
            print(f"Erro ao apagar a pasta: {e}")


if __name__ == '__main__':

    drive = GoogleDriver(
        creds_path=get_secret_value('CRED_PATH'),
        folder_id=get_secret_value('FOLDER_ID')
    )

    # drive.create_public_folder("real_state_data_pipeline_images")

    items = drive.list_folder_in_drive()

    for item in items:
        print(f"{item['name']} ({item['id']})")
        if item["name"] == "image_test":
            folder_id = item['id']

    # drive.delete_folder(folder_id)

    # base = "https://resizedimgs.zapimoveis.com.br/fit-in/870x707/"
    # image_urls = [
    #     'vr.images.sp/5abc8dba84fc3c919ab2620b609d5a27.webp',
    #     'vr.images.sp/fd4e0c11fcc1f4cfc81a2fc0c0dc61d9.webp'
    # ]
    # for i, url in enumerate(image_urls):
    #     filename = f'image_{i+1}.webp'
    #     image_path, image_filename = download_image(base + url, filename)

    #     link = drive.upload_image_to_drive(
    #         image_path,
    #         image_filename,
    #         )
    #     print(link)

    #     delete_image(image_path)
