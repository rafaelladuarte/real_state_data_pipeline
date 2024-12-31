from scripts.infra.storage.driver import GoogleDriver
from scripts.infra.security.secrets import get_secret_value

from scripts.utility.image import (
    download_image, delete_image
)


def treatment_images(original_images, hash):

    drive = GoogleDriver(
        creds_path=get_secret_value('CRED_PATH'),
        folder_id=get_secret_value('FOLDER_ID')
    )

    new_images_url = []
    for i, url in enumerate(original_images[:10]):
        filename = f'{hash}_{i+1}.webp'
        image_path, image_filename = download_image(url, filename)

        link = drive.upload_image_to_drive(
            image_path,
            image_filename,
            )
        new_images_url.append(link)

        delete_image(image_path)

    return new_images_url


if __name__ == '__main__':
    treatment_images()
