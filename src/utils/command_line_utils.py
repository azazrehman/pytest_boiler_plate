import os
import sys

from src.utils.logger import logger


class CommandLineUtils:
    """
    This class provides utility functions for working with command line arguments and environment variables.
    """

    def get_all_args(self):
        """
        Retrieves all arguments passed to the script from the command line.
        Returns:
            list: A list containing all command line arguments.
        """
        return sys.argv

    def get_all_arg_keys(self):
        """
        Retrieves all environment variable keys from the current environment.
        Returns:
            list: A list containing all environment variable keys.
        """
        return os.environ.keys()

    def get_value_from_key(self, pstr_key):
        """
        Gets the value associated with a specific environment variable key.
        Args:
            pstr_key (str): The key of the environment variable to retrieve the value for.
        Returns:
            str: The value of the environment variable if it exists, otherwise None.
        Raises:
            Exception: If an error occurs while retrieving the environment variable value.
        """
        try:
            if pstr_key in self.get_all_arg_keys():
                return os.environ[pstr_key]
            else:
                return None
        except Exception as e:
            error_message = f"Exception occurred while getting value from key in command line utils --> {e}"
            logger.error(error_message)
            raise Exception(error_message)

