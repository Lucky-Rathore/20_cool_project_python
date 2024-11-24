
import markdown

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def convert_markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html

def write_html_file(html, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(html)

def main(input_file, output_file):
    markdown_content = read_markdown_file(input_file)
    html_content = convert_markdown_to_html(markdown_content)
    write_html_file(html_content, output_file)
    print(f"Conversion complete! HTML output written to {output_file}.")

if __name__ == "__main__":
    input_markdown_file = 'Introduction.md'  # Replace with your file path
    output_html_file = 'example.html'  # Desired output file path
    main(input_markdown_file, output_html_file)