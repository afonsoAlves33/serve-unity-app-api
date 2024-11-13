from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()


class AzureStorage():
    def __init__(self):
        self.storage_account_key = os.getenv('storage_account_key')
        self.storage_account_name = os.getenv('storage_account_name')
        self.connection_string = os.getenv('connection_string')
        self.objects3d_container_name = os.getenv('OBJECTS3D_CONTAINER')
        self.videos_container_name = os.getenv('VIDEOS_CONTAINER')
        self.images_container_name = os.getenv('IMAGES_CONTAINER')
        self.component_images_container_name = os.getenv('COMPONENT_IMAGES_CONTAINER')

        # Azure Storage Blob admin
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

    def upload_3d_object(self, file_path: str, file_name: str):
        blob_client = self.blob_service_client.get_blob_client(container=self.objects3d_container_name, blob=file_name)
        try:
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)
        except Exception as e:
            print(f"An error ocurred while trying to upload the file: {str(e)}")
            return "An error ocurred while trying to upload the file"
        return "Upload successful"

    def delete_3d_object(self, file_name: str):
        try:
            obj_container = self.blob_service_client.get_container_client("objects")
            obj_container.delete_blob(file_name)
        except Exception as e:
            print(f"An error ocurred while trying to delete the file: {str(e)}")
            return "An error ocurred while trying to delete the file"
        return f"Deleted {file_name} successful"

    def upload_video(self, file_path: str, file_name: str):
        blob_client = self.blob_service_client.get_blob_client(container=self.videos_container_name, blob=file_name)
        try:
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)
        except Exception as e:
            print(f"An error ocurred while trying to upload the file: {str(e)}")
            return "An error ocurred while trying to upload the file"
        return "Upload successful"

    def delete_video(self, file_name: str):
        try:
            obj_container = self.blob_service_client.get_container_client("videos")
            obj_container.delete_blob(file_name)
        except Exception as e:
            print(f"An error ocurred while trying to delete the file: {str(e)}")
            return "An error ocurred while trying to delete the file"
        return f"Deleted {file_name} successful"


    def upload_image(self, file_path: str, file_name: str):
        blob_client = self.blob_service_client.get_blob_client(container=self.images_container_name, blob=file_name)
        try:
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)
        except Exception as e:
            print(f"An error ocurred while trying to upload the file: {str(e)}")
            return "An error ocurred while trying to upload the file"
        return "Upload successful"

    def delete_image(self, file_name: str):
        try:
            obj_container = self.blob_service_client.get_container_client(self.images_container_name)
            obj_container.delete_blob(file_name)
        except Exception as e:
            print(f"An error ocurred while trying to delete the file: {str(e)}")
            return "An error ocurred while trying to delete the file"
        return f"Deleted {file_name} successful"
    
    def upload_component_image(self, file_path: str, file_name: str):
        blob_client = self.blob_service_client.get_blob_client(container=self.component_images_container_name, blob=file_name)
        try:
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)
        except Exception as e:
            print(f"An error ocurred while trying to upload the file: {str(e)}")
            return "An error ocurred while trying to upload the file"
        return "Upload successful"

    def delete_container(self, container_name):
        try:
            obj_container = self.blob_service_client.get_container_client(container_name)
            obj_container.delete_container()
        except Exception as e:
            print(f"An error ocurred while trying to delete the file: {str(e)}")
            return "An error ocurred while trying to delete the file"
        return f"Deleted successful"


if __name__ == "__main__":
    az = AzureStorage()
    # delete esse container
    namevar = ""
    az.delete_container(namevar)
    print(f"deletou o container {namevar}")

