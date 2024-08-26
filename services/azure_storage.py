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
        self.object3d_filepath = "C:\\Users\\ct67ca\\Documents\\dev\\tcc\\API\\01-08\\serve-unity-app-api\\files\\fbx_objects\\3.fbx"
        self.video_filepath = "C:\\Users\\ct67ca\\Documents\\dev\\tcc\\API\\01-08\\serve-unity-app-api\\files\\tutorial_videos\\3.mp4"

        # Azure Storage Blob admin
        self.blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)

    def upload_3d_object(self, file_path: str, file_name: str):
        blob_client = self.blob_service_client.get_blob_client(container=self.objects3d_container_name, blob=file_name)
        try:
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
        except Exception as e:
            print(f"An error ocurred while trying to upload the file: {e}")
            return "An error ocurred while trying to upload the file"
        else:
            return "Upload successful"

    def delete_3d_object(self, file_name: str):
        try:
            obj_container = self.blob_service_client.get_container_client("objects")
            obj_container.delete_blob(file_name)
        except Exception as e:
            print(f"An error ocurred while trying to delete the file: {e}")
            return "An error ocurred while trying to delete the file"
        return f"Deleted {file_name} successful"

    def upload_video(self, file_path: str, file_name: str):
        blob_client = self.blob_service_client.get_blob_client(container=self.videos_container_name, blob=file_name)
        try:
            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)
        except Exception as e:
            print(f"An error ocurred while trying to upload the file: {e}")
            return "An error ocurred while trying to upload the file"
        else:
            return "Upload successful"

    def delete_video(self, file_name: str):
        try:
            obj_container = self.blob_service_client.get_container_client("videos")
            obj_container.delete_blob(file_name)
        except Exception as e:
            print(f"An error ocurred while trying to delete the file: {e}")
            return "An error ocurred while trying to delete the file"
        else:
            return f"Deleted {file_name} successful"


if __name__ == "__main__":
    azure_db = AzureStorage()
    azure_db.upload_3d_object(azure_db.object3d_filepath, "3.fbx")
    azure_db.upload_video(azure_db.video_filepath, "3.mp4")