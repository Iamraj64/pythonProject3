from langchain.llms import OpenAI
import os
os.environ['OPENAI_API_KEY']='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'
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import tiktoken



query = "Can u go for a logic that shows if a bal is wide ball or not in cricket"


API_KEY="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"


def num_tokens_from_string(string, encoding_name):

    encoding = tiktoken.get_encoding(encoding_name)

    num_tokens = len(encoding.encode(string))

    return num_tokens


flowchat_prompt = '''
query:
{query}
convert this query to mermaidjs markup
generate code only. Don't generate any other statements.
Make sure the output is mermaidjs compatible. Don't include extra quotes in the output
'''
tokens = num_tokens_from_string(flowchat_prompt,"p50k_base")
print(tokens)
llm_chain = LLMChain(prompt=PromptTemplate.from_template(flowchat_prompt), llm=OpenAI(model_name="gpt-3.5-turbo",temperature=0.9,openai_api_key=API_KEY), verbose=True)
result=llm_chain.predict(query=query)
print("result_list from ChatGPT:",result)