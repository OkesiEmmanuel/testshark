import requests
import os
import logging
from ratelimit import limits, sleep_and_retry
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(filename='gemini_api.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
load_dotenv()
GEMINI_API_URL = os.environ.get('GEMINI_API_URL', 'https://api.gemini.com/v1/generate_script')
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
GENERATE_SCRIPT_RATE_LIMIT = int(os.environ.get('GENERATE_SCRIPT_RATE_LIMIT', 10))
SUGGEST_TEST_CASES_RATE_LIMIT = int(os.environ.get('SUGGEST_TEST_CASES_RATE_LIMIT', 5))

# Rate limits
GENERATE_SCRIPT_RATE_LIMIT = limits(calls=GENERATE_SCRIPT_RATE_LIMIT, period=60)
SUGGEST_TEST_CASES_RATE_LIMIT = limits(calls=SUGGEST_TEST_CASES_RATE_LIMIT, period=60)

# Helper function for making Gemini API requests
@sleep_and_retry
def _make_gemini_api_request(endpoint, data, rate_limit):
    """Helper function to make requests to the Gemini API."""
    headers = {'Authorization': f'Bearer {GEMINI_API_KEY}'}
    logging.info(f"Making API request to: {endpoint} with data: {data}")
    try:
        response = requests.post(endpoint, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        logging.info(f"API Response: {response.json()}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error calling Gemini API: {e}")
        return None

# Generate Script
@GENERATE_SCRIPT_RATE_LIMIT
def generate_script(framework, language, test_case, element_identifiers):
    """Sends a request to the Gemini API to generate a test script."""
    data = {
        'framework': framework,
        'language': language,
        'test_case': test_case.steps,
        'element_identifiers': element_identifiers,
    }
    return _make_gemini_api_request(GEMINI_API_URL, data, GENERATE_SCRIPT_RATE_LIMIT)

# Suggest Test Cases
@SUGGEST_TEST_CASES_RATE_LIMIT
def suggest_test_cases(code_analysis_data):
    """Sends a request to the Gemini API to suggest test cases."""
    data = {
        'code_analysis_data': code_analysis_data,
    }
    return _make_gemini_api_request(GEMINI_API_URL, data, SUGGEST_TEST_CASES_RATE_LIMIT)