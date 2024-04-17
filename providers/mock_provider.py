import json

def call_api(prompt, options, context):
    result = {
        "output": context['vars']['gpt_current_feedback'],
    }
    return result
