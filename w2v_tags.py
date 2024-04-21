from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI, AzureChatOpenAI


base_url = "http://mistral.vkcloud.eazify.net:8000/v1"

chat = ChatOpenAI(api_key="<key>",
                model = "tgi",
                openai_api_base = base_url,
                temperature=0.1)

parser = JsonOutputParser()

instruct = """
На основе предоставленного текста извлеки ключевые слова которые наилучшим образом отображают его содержание. 
Оформи ответ в формате JSON: {{
            "keywords": ["ключевое слово1", "ключевое слово2", ...]
            }}

Предоставленный текст: ```{text}```
"""

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", f"Ты сторого следуешь задаче: твоя задача извлекать из текста ключевые слова"),
        ("human", instruct),
    ]
)


def get_tags(text) -> dict:

    '''
    Get JSON response by category.

    INPUT: category [STRING], text [STRING]
    OUTPUT: JSON response [DICT]
    '''
    try:
        res = parser.invoke(chat.invoke(chat_template.format_messages(text=text)))
        return res
    except:
        return {'keywords': []}
                
