from pathlib import Path


class Utils:
    @staticmethod
    def get_file_extension(file_name: str) -> str:
        last_dot_index = file_name.rfind('.')
        if last_dot_index != -1:
            result = file_name[last_dot_index + 1:].strip()
        else:
            result = file_name
        return result

    @staticmethod
    def get_file_name(file_name: str) -> str:
        last_dot_index = file_name.rfind('.')
        if last_dot_index != -1:
            result = file_name[:last_dot_index].strip()
        else:
            result = file_name.strip()
        return result

    @staticmethod
    def delete_file_locally(file_path: str):
        file_path = Path(file_path)
        try:
            if file_path.exists():
                file_path.unlink()
                return "File deleted"
            else:
                return "File not found"
        except Exception as e:
            return f"Could not delete, exception: {e}"


