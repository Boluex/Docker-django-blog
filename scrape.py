# import requests
# from bs4 import BeautifulSoup
# import lxml
# import os


# def generate_files():
#     html_dir=os.makedirs('/home/deji/Desktop/deji/PycharmProjects/blog_proj/html_dir',exist_ok=True)
#     new_file=os.path.join('/home/deji/Desktop/deji/PycharmProjects/blog_proj/html_dir/file.html')
#     js_file=os.path.join('/home/deji/Desktop/deji/PycharmProjects/blog_proj/html_dir/file.js')
#     css_file=os.path.join('/home/deji/Desktop/deji/PycharmProjects/blog_proj/html_dir/file.css')
#     source=requests.get('http://127.0.0.1:8000/').content

#     soup=BeautifulSoup(source,'lxml')

#     with open('file.html','w') as f:
#         data=soup.prettify()
#         f.write(data)
#         f.close()


#     find_script_tag=soup.find_all('script')
#     change_tag=str(find_script_tag)
#     with open('file.js','w') as f:
#         f.write(change_tag)
#         f.close()

        
#     find_css_tag=soup.find_all('link')
#     css_style=find_css_tag[1]

#     css_style_link='http://127.0.0.1:8000/' + css_style['href']


#     new_request=requests.get(css_style_link).content
#     soup=BeautifulSoup(new_request,'lxml')
#     css_style=soup.prettify()
#     with open('file.css','w') as f:
#         f.write(css_style)
#         f.close()
        
#     print('Done....')



from llama_cpp import Llama
import json

model_path = '/home/deji/Desktop/deji/models/mistral-7b-instruct-v0.1.Q3_K_L.gguf'
load_model = Llama(model_path)

model_output = load_model('Question: what is architecture? Answer:',
                          max_tokens=100,
                          stop=['\n', 'Question:', 'Q:'],
                          echo=True)

print(json.dumps(model_output, indent=4))