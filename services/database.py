

class DatabaseManagement():
    def __init__(self, database: classmethod) -> None:
        self.database = database()

    def upload_3d_object(self, file_path, file_name):
        self.database.upload_3d_object(file_path, file_name)

    def upload_video(self, file_path, file_name):
        self.database.upload_video(file_path, file_name)
