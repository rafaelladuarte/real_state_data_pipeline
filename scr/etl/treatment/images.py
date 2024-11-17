from infra.storage.mongo import MongoDB
from infra.storage.driver import GoogleDriver
from infra.security.secrets import get_secret_value

from utility.image import (
    download_image, delete_image
)


def treatment_images():
    print("----------------  IMAGES ----------------")

    mongo = MongoDB(uri=get_secret_value("MONGO_URI"))
    drive = GoogleDriver(
        creds_path=get_secret_value('CRED_PATH'),
        folder_id=get_secret_value('FOLDER_ID')
    )

    b = 0
    while True:
        b += 1

        if b == 3:
            break

        print(f"=> Batch {b}")
        print("Get documents in collection 'imoveis'")
        docs = mongo.get_documents(
            query={
                "images_url": {
                    "$exists": False
                }
            },
            collection="imoveis"
        )

        if len(docs) == 0:
            break

        print("Start treatment images")
        for doc in docs[:2]:
            id = doc["_id"]
            original_image_url = doc["original_imagens"]

            new_images_url = []
            for i, url in enumerate(original_image_url[:2]):
                filename = f'image_{i+1}.webp'
                image_path, image_filename = download_image(url, filename)

                link = drive.upload_image_to_drive(
                    image_path,
                    image_filename,
                    )
                new_images_url.append(link)

                delete_image(image_path)

        print(f"Images imovel {id} with {len(new_images_url)} images")
        mongo.update_documents(
            query={
                "_id": id
            },
            set={
                "$set": {
                    "images_url": new_images_url
                }
            },
            collection="imoveis",
        )


if __name__ == '__main__':
    treatment_images()
