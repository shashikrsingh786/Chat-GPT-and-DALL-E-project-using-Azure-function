import logging
import openai
import azure.functions as func

{
    "prompt" : "give me a nice picture dog",
    "n" : 1,
       "size" : "1024x1024"
    }

secret_key  = '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'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # give openai our secret key to authenticate
    openai.api_key = secret_key
    # get variable from http request body
    req_body = req.get_json()
    logging.info(type(req_body))
    # call the openai api
    output = openai.Image.create(
        prompt = req_body['prompt'],
       n = req_body['n'],
       size = req_body['size']
    ) 
    # format the response
    output_text = output['data'][0]['url']
    # provide the response


    return func.HttpResponse(output_text, status_code=200)