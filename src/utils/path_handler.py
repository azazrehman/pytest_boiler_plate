
from pathlib import Path
import os
from src.utils.logger import logger
from constants.project_level_constants import FileNames

class PathHandler:

    def __get_project_root(self):
        try:
            project_root_path = Path(
                os.path.dirname(os.path.abspath(__file__))).parent.parent.parent
            return project_root_path
        except Exception as e:
            error_message = f"Error occurred while Getting project root --> {e}"
            logger.error(error_message)
            raise Exception(error_message)
        
    def get_base_config_path(self):
        try:
            base_config_path = os.path.join(self.__get_project_root(), FileNames.CONFIG_FILE)
            return base_config_path
        except Exception as e:
            error_message = f"Exception occurred while getting the config path tring for path {self.__get_project_root()}/ {FileNames.CONFIG_FILE} -->{e}"
            logger.error(error_message)
            raise Exception(error_message)
    
    def get_screenshot_folder(self):
        try:
            folder_path = f"{self.__get_project_root()}/{FileNames.SCREEN_SHOT_FOLDER}"
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            return folder_path
        except Exception as e:
            error_message = f"Exception occurred while getting the screenshot folder path {self.__get_project_root()}/ {FileNames.SCREEN_SHOT_FOLDER} -->{e}"
            logger.error(error_message)
            raise Exception(error_message)

    

    
    