from abc import ABC, abstractmethod
class Database(ABC):

    @abstractmethod
    def upload_3d_object(self, file_path: str, file_name: str):
        pass

    @abstractmethod
    def upload_video(self, file_path: str, file_name: str):
        pass