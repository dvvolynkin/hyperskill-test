import json
import sys

def mock_prompt_function(context: dict) -> str:
    del context['vars']['gpt_current_feedback']
    
    # Mocked prompt, does not matter what it contains
    return f"Give some feedback for this submission {json.dumps(context['vars'])}"

if __name__ == "__main__":
    # If you don't specify a `function_name` in the provider string, it will run the main
    print(mock_prompt_function(json.loads(sys.argv[1])))
