import subprocess
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.storage import default_storage

# Constants for framework and language combinations
TESTNG_JAVA = ('TestNG', 'Java')
SELENIUM_PYTHON = ('Selenium', 'Python')

def execute_script(test_script):
    """Executes the test script based on the framework and language."""
    try:
        # Use a dictionary for clearer mapping
        execution_commands = {
            TESTNG_JAVA: ['mvn', 'test'],
            SELENIUM_PYTHON: ['python', 'test_script.py'],
            # Add more commands for other frameworks and languages here
        }

        command = execution_commands.get((test_script.framework, test_script.language))
        if command:
            subprocess.run(command, capture_output=True, check=True)
            return True
        else:
            raise ValueError(f"Unsupported framework/language combination: {test_script.framework}/{test_script.language}")

    except subprocess.CalledProcessError as e:
        return False
    except ValueError as e:
        return False  # Indicate unsupported combination

def save_screenshot(screenshot_path):
    """Saves a screenshot to the media directory."""
    with open(screenshot_path, 'rb') as f:
        file_name = screenshot_path.split('/')[-1]
        file_content = f.read()
        uploaded_file = SimpleUploadedFile(file_name, file_content, content_type='image/png')
        return default_storage.save('screenshots/' + file_name, uploaded_file)