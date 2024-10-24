class StorageManager:
    def __init__(self, database) -> None:
        """
        Receive a Database Implementation to work with.
        Currently, using AZURE.
        """
        self.database = database()

    def upload_3d_object(self, file_path: str, file_name: str) -> str:
        """
        Upload a local file to Azure, requires the file's path and the wanted name.
        """
        try:
            upload = self.database.upload_3d_object(file_path, file_name)
        except Exception as e:
            print("Unable to run 'upload_3d_object' method:", e)
            return "Unable to upload file"
        if upload == "Upload successful":
            return "Upload successful"
        return "Unable to upload file"


    def upload_video(self, file_path: str, file_name: str) -> str:
        """
        Upload a local video to Azure, requires the file's path and the wanted name.
        """
        try:
            upload = self.database.upload_video(file_path, file_name)
        except Exception as e:
            print("Unable to run 'upload_video' method: ", e)
            return "Unable to upload video"
        if upload == "Upload successful":
            return "Upload successful"
        return "Unable to upload video"

    
    def upload_image(self, file_path: str, file_name: str) -> str:
        """
        Upload a local image to Azure, requires the file's path and the wanted name.
        """
        try:
            upload = self.database.upload_image(file_path, file_name)
        except Exception as e:
            print("Unable to run 'upload_video' method: ", e)
            return "Unable to upload video"
        if upload == "Upload successful":
            return "Upload successful"
        return "Unable to upload video"
