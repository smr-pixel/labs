import ast

def parse_file(file_path):
    with open(file_path, 'r') as file:
        return ast.parse(file.read())

def file_structure(file_path):
    with open(file_path, 'r') as file:
        total_lines = len(file.readlines())
    return f"The total number of lines of code is: {total_lines}"

def imports(tree):
    imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
    imports += [node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
    return f"Import: {', '.join(imports) if imports else 'No imports found.'}"

def classes(tree):
    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    class_docs = []
    for node in classes:
        class_node = next(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef) and n.name == node)
        docstring = ast.get_docstring(class_node) or f"{node}: DocString not found."
        class_docs.append(docstring)
    return f"Classes: {', '.join(classes) if classes else 'No classes found.'}\n" + "\n\n".join(class_docs)

def functions(tree):
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    func_docs = []
    for node in functions:
        func_node = next(n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == node)
        docstring = ast.get_docstring(func_node) or f"{node}: DocString not found."
        func_docs.append(docstring)
    return f"Functions: {', '.join(functions) if functions else 'No functions found.'}\n" + "\n\n".join(func_docs)

def type_annotations(tree):
    no_annotations = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
            if node.returns is None:
                no_annotations.append(node.name)
    if no_annotations:
        return f"The functions without any type annotations are: {', '.join(no_annotations)}"
    else:
        return"All functions have type annotations."

def naming_conventions(tree):
    class_violations = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef) and not node.name[0].isupper()]
    func_violations = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef) and not node.name.islower()]
    if class_violations:
        class_message = f"The classes not adhering to naming conventions are: {', '.join(class_violations)}"
    else:
        class_message = "All classes adhere to naming conventions."
    
    if func_violations:
        func_message = f"The functions not adhereing to naming conventions are: {', '.join(func_violations)}"
    else:
        func_message = "All functions adhere to naming conventions."
    
    return class_message + '\n' + func_message

def write_report(report, output_path):
    with open(output_path, 'w') as file:
        file.write("\n".join(report))

def analyze_file(file_path, output_path="style_report.txt"):
    tree = parse_file(file_path)
    report = [ file_structure(file_path), imports(tree), classes(tree), functions(tree), type_annotations(tree), naming_conventions(tree) ]
    write_report(report, output_path)

if __name__ == "__main__":
    analyze_file('custom_style_checker.py')

analyze_file('custom_style_checker.py')