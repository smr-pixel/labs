import ast
import os

class StyleChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.report = []
        self.tree = self._parse_file()

    def _parse_file(self):
        with open(self.file_path, 'r') as file:
            return ast.parse(file.read())
        
    def analyze_file(self):
        self.file_structure()
        self.imports()
        self.classes()
        self.functions()
        self.type_annotations()
        self.naming_conventions()
        self.print_report()

    def file_structure(self):
        total_lines = len(open(self.file_path).readlines())
        self.report.append(f"The total number of lines of code is: {total_lines}")

    def imports(self):
        imports = [node.names[0].name for node in ast.walk(self.tree) if isinstance(node, ast.Import)]
        imports += [node.module for node in ast.walk(self.tree) if isinstance(node, ast.ImportFrom)]
        self.report.append(f"Import: {', '.join(imports) if imports else 'No imports found.'}")

    def classes(self):
        classes = [node.name for node in ast.walk(self.tree) if isinstance(node, ast.ClassDef)]
        class_docs = []
        for node in classes:
            class_node = next(n for n in ast.walk(self.tree) if isinstance(n, ast.ClassDef) and n.name == node)
            docstring = ast.get_docstring(class_node) or f"{node}: DocString not found."
            class_docs.append(docstring)
        self.report.append(f"Classes: {', '.join(classes) if classes else 'No classes found.'}\n" + "\n\n".join(class_docs))

    def functions(self):
        functions = [node.name for node in ast.walk(self.tree) if isinstance(node, ast.FunctionDef)]
        func_docs = []
        for node in functions:
            func_node = next(n for n in ast.walk(self.tree) if isinstance(n, ast.FunctionDef) and n.name == node)
            docstring = ast.get_docstring(func_node) or f"{node}: DocString not found."
            func_docs.append(docstring)
        self.report.append(f"Functions: {', '.join(functions) if functions else "No functions found."}\n" + "\n\n".join(func_docs))

    def type_annotations(self):
        no_annotations = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                if node.returns is None:
                    no_annotations.append(node.name)
        if no_annotations:
            self.report.append(f"The functions without any type annotations are: {', '.join(no_annotations)}")
        else:
            self.report.append("All functions have type annotations.")

    def naming_conventions(self):
        class_violations = [node.name for node in ast.walk(self.tree) if isinstance(node, ast.ClassDef) and not node.name[0].isupper()]
        func_violations = [node.name for node in ast.walk(self.tree) if isinstance(node, ast.FunctionDef) and not node.name.islower()]
        if class_violations:
            self.report.append(f"The classes not adhering to naming conventions are: {', '.join(class_violations)}")
        else:
            self.report.append("All classes adhere to naming conventions.")

        if func_violations:
            self.report.append(f"The functions not adhereing to naming conventions are: {', '.join(func_violations)}")
        else:
            self.report.append("All functions adhere to naming conventions.")

    def print_report(self):
        print("\n".join(self.report))

if __name__ == "__main__":
    checker = StyleChecker('custom_style_checker.py')
    checker.analyze_file()