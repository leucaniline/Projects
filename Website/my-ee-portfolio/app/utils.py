def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def read_latex_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def list_projects(projects_directory):
    import os
    return [f for f in os.listdir(projects_directory) if f.endswith('.md')]

def list_essays(essays_directory):
    import os
    return [f for f in os.listdir(essays_directory) if f.endswith('.txt') or f.endswith('.tex')]