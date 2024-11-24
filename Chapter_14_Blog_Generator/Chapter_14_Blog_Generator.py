# Chapter_14_Blog_Generator
import os
from jinja2 import Environment, FileSystemLoader
import markdown

def read_markdown_files(directory):
    markdown_files = {}
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            with open(os.path.join(directory, filename), 'r') as file:
                markdown_files[filename] = file.read()
    return markdown_files

def convert_markdown_to_html(markdown_content):
    return markdown.markdown(markdown_content)

def generate_blog(markdown_directory, output_directory, template_name):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template_name)
    
    markdown_files = read_markdown_files(markdown_directory)
    
    for filename, content in markdown_files.items():
        html_content = convert_markdown_to_html(content)
        output_filename = os.path.splitext(filename)[0] + '.html'
        
        with open(os.path.join(output_directory, output_filename), 'w') as output_file:
            output_file.write(template.render(content=html_content, title=filename))
    
if __name__ == '__main__':
    markdown_directory = 'markdown_files'
    output_directory = 'blog_html'
    template_name = 'helloWorld.jinja' #helloWorld.jinja
    
    generate_blog(markdown_directory, output_directory, template_name)