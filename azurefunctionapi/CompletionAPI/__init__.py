import logging
import openai
import azure.functions as func

# {"model" : "text-davinci-003",
#     "prompt" : "give me a nice name for my dog",
#     "max_tokens" : 100,
#     "temperature":0}

secret_key  = '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'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give openai our secret key to authenticate
    openai.api_key = secret_key
    # get variable from http request body
    req_body = req.get_json()
    logging.info(type(req_body))
    # call the openai api
    output = openai.Completion.create(
        model = req_body['model'],
        prompt = req_body['prompt'],
        max_tokens = req_body['max_tokens'],
        temperature = req_body['temperature']
    ) 
    # format the response
    output_text = output['choices'][0]['text']
    # provide the response


    return func.HttpResponse(output_text, status_code=200)
    
