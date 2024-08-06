from abc import ABC, abstractmethod
class Database():

    @abstractmethod
    def upload_3d_object(self, file_path, file_name):
        pass

    @abstractmethod
    def upload_video(self, file_path, file_name):
        pass