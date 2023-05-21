secret_key = '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'
prompt = 'give me a english idiom'

import openai
openai.api_key = secret_key

output = openai.Completion.create(
    model = 'text-davinci-003',
    prompt = prompt,
    max_tokens = 100,
    temperature=0
)
output_text = output['choices'][0]['text']
print(output_text)