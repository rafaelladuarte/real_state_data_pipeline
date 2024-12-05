from infra.storage.driver import GoogleDriver
from infra.security.secrets import get_secret_value

from utility.image import (
    download_image, delete_image
)


def treatment_images(original_images):

    drive = GoogleDriver(
        creds_path=get_secret_value('CRED_PATH'),
        folder_id=get_secret_value('FOLDER_ID')
    )

    new_images_url = []
    for i, url in enumerate(original_images[:2]):
        filename = f'image_{i+1}.webp'
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
