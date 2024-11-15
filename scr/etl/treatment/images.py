from infra.storage.mongo import MongoDB
from infra.storage.driver import GoogleDriver
from infra.security.secrets import get_secret_value

from utility.image import (
    download_image, delete_image
)

mongo = MongoDB(uri=get_secret_value("MONGO_URI"))
drive = GoogleDriver(
    get_secret_value=get_secret_value('CRED_PATH'),
    folder_id=get_secret_value('FOLDER_ID')
)

while True:
    docs = mongo.get_documents_flag(
        flag="images_url",
        database="raw",
        collection="imoveis"
    )

    if len(docs) > 0:
        break

    for doc in docs:
        id = doc["_id"]
        original_image_url = doc[""]

        new_images_url = []
        for i, url in enumerate(original_image_url[:5]):
            filename = f'image_{i+1}.webp'
            image_path, image_filename = download_image(url, filename)

            link = drive.upload_image_to_drive(
                image_path,
                image_filename,
                )
            new_images_url.append(link)

            delete_image(image_path)

    mongo.update_document_set(
        id=id,
        set={
            "$set": {
                "images_url": new_images_url
            }
        },
        database="raw",
        collection="imoveis",
    )
