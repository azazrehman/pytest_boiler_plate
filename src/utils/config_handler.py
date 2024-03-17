import yaml
from src.utils.command_line_utils import CommandLineUtils
from src.utils.path_handler import PathHandler
from src.utils.logger import logger


class ConfigHandler:

    config_content = None
    command_line = CommandLineUtils()
    BASE_CONFIG_FILE_PATH = 'base_config.yml'
    ENV_KEY = 'environment_to_execute'
    AUTOMATION_TOOL_KEY = 'automation_tool'
    BROWSER_KEY = 'browser'
    DRIVER_PATH = 'driver_path'
    BROWSER_URL = 'url'
    WAITS = 'waits'
    
    def __init__(self):
        
        base_config_file_path  = PathHandler().get_base_config_path()
        with open(base_config_file_path, 'r') as base_file:
            base_config = yaml.safe_load(base_file)
        env_name = self.get_env_name(base_config)
        self.read_config(base_config, env_name)

    def get_value(self, key):
        try:
            command_line_value = self.command_line.get_value_from_key(key)
            if command_line_value is None:
                logger.debug(f"Fetching value of {key} from the base config as not getting value from environment "
                             f"variable")
                return self.config_content[key]
            else:
                logger.debug(f"Fetching value of {key} from the environment variables, because that's have a priority")
                return command_line_value
        except KeyError:
            logger.error(f"KeyError: '{key}' not found in configuration")
            raise
        except Exception as e:
            logger.error(f"Error while getting value for '{key}': {e}")
            raise

    def read_config(self,base_config_file_content, env_name):
        try:
            # Load environment-specific config
            config_folder_path  = f"{PathHandler().get_base_config_path(folder_only=True)}"
            env_config_file = f"{config_folder_path}/{env_name}_config.yml"

            with open(env_config_file, 'r') as env_file:
                env_config = yaml.safe_load(env_file)

            # Merge base config with environment-specific config

            self.config_content =  {**base_config_file_content, **env_config}
        except Exception as e:
            error_message = f"Error while reading configuration {e}"
            logger.error(error_message)
            raise Exception(error_message)
    
    def get_env_name(self, base_config):
        try:
            command_line_value = self.command_line.get_value_from_key('environment_to_execute')
            if command_line_value is None:
                logger.debug(f"Fetching value of environment_to_execute from the base config as not getting value "
                             f"from environment variable")
                return base_config['environment_to_execute']
            else:
                logger.debug(f"Fetching value of environment_to_execute from the environment variabels, becasue thats "
                             f"have a priority")
                return command_line_value
        except Exception as e:
            error_message = f"Error while getting enviroment name {e}"
            logger.error(error_message)
            raise Exception(error_message)
    
    def get_automation_tool(self):
        return self.get_value(self.AUTOMATION_TOOL_KEY)

    def get_browser_name(self):
        return self.get_value(self.BROWSER_KEY)
    
    def get_browser_driver_path(self):
        return self.get_value(self.DRIVER_PATH)

    def get_base_url_browser(self):
        return self.get_value(self.BROWSER_URL)

    def get_waits(self):
        return self.get_value(self.WAITS)
    