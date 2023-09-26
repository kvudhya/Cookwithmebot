import os
import openai
from PIL import Image
from model import *

#prediction = predictions("istockphoto-1094166778-612x612.jpg")

#openai.organization = "org-bSI6wsPa9iLKnICno111wZfw"
openai.api_key =


#def chat_with_chatgpt( model=):
def recipe_bot(image):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        #max_tokens=2000,
        messages = [{'role' : "system",  'content': 'your are a cook who give detail recipe when given the recipe'},
                    { 'role': "user", 'content':'Provide a brief recipe give these ingredients' + str(predictions(image))},   
                    
                    ] ,
    )
    #print(response)
    message = response.choices[0].message.content

    return message

