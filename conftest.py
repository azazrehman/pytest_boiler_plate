import os, sys, shutil

sys.path.append(os.getcwd())

import pytest
from src.utils.bot_handlers.bots.bot_playwright import BotPlaywright
from src.utils.bot_handlers.bots.bot_selenium import BotSelenium
from src.utils.config_handler import ConfigHandler
from src.utils.path_handler import PathHandler
from src.utils.logger import logger

config_properties = ConfigHandler()
screen_shot_folder = PathHandler().get_screenshot_folder()


class BaseCase:
    def common_config(self):
        logger.info('Conftest Comon config')
        pytest.web_bot = None
        pytest.mobile_bot = None
        pytest.current_test_name = None

    @pytest.fixture(scope='session', autouse=True)
    def before_all(self):
        logger.info('Before All')
        # TODO - Update it to use from config
        frame_work = config_properties.get_automation_tool()
        browser = config_properties.get_browser_name()

        if frame_work.lower() == 'selenium':
            driver_path = config_properties.get_browser_driver_path()
            pytest.web_bot = BotSelenium(browser_on_tests_execute=browser, driver_path=driver_path)
        elif frame_work.lower() == 'playwright':
            pytest.web_bot = BotPlaywright(browser_on_tests_execute=browser)
        if os.path.exists(f"{screen_shot_folder}"):
            shutil.rmtree(screen_shot_folder)
            os.mkdir(screen_shot_folder)

    def setup_method(self, method):
        try:
            pytest.current_test_name = method.__name__
            if not os.path.exists(f"{screen_shot_folder}/{pytest.current_test_name}"):
                os.mkdir(f"{screen_shot_folder}/{pytest.current_test_name}")
            pytest.web_bot.launch_browser()
        except Exception as e:
            error_message = f"Error in before Scenario {e}"
            logger.error(error_message)
            raise Exception(error_message)

    def setup_class(cls):
        try:
            # print("FINDING DEVICE TYPE")
            print('a')
            # print("DEVICE TYPE IS ", device_type)

        except Exception as e:
            error_message = f"Error in Setup Before Class/Test File {str(e)}"
            logger.error(error_message)
            raise Exception(error_message)

    def teardown_method(self):
        try:
            logger.debug(f"Inside After Each method of the test {pytest.current_test_name}")
            pytest.web_bot.quit_browser()
            self.generate_gifs(pytest.current_test_name)
        except Exception as e:
            error_message = f"Error in After Each Method for Test {pytest.current_test_name} {str(e)}"
            logger.error(error_message)

    def teardown_class(self):
        try:
            logger.debug(f"Inside After Each Class/File of the test")
        except Exception as e:
            print(str(e))

    def generate_gifs(self, test_case_name):
        try:
            import os
            from PIL import Image

            screenshot_folder = f"{screen_shot_folder}/{test_case_name}"
            # Get a list of all PNG files in the directory
            png_files = [os.path.join(screenshot_folder, file) for file in os.listdir(screenshot_folder) if
                         file.lower().endswith('.png')]

            # Sort the PNG files based on modification time
            png_files.sort(key=lambda x: os.path.getmtime(x))

            # Open the first image to get its size
            with Image.open(png_files[0]) as img:
                # Create a list to store the frames
                frames = []

                # Iterate through each PNG image and append to the frames list
                for png_file in png_files:
                    frames.append(Image.open(png_file))

                # Save the frames as a GIF
                frames[0].save(f"{screen_shot_folder}/{test_case_name}.gif", save_all=True, append_images=frames[1:],
                               duration=700, loop=0)
            shutil.rmtree(screenshot_folder)
        except Exception as e:
            error_message = f"Error in Creating gifs Scenario {str(e)}"
            logger.warning(error_message)
