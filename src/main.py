import subprocess

from src.ast.ast_processor import AstProcessor
from src.ast.basic_info_listener import BasicInfoListener


if __name__ == '__main__':
    subprocess.run(['ls','-la','/opt/home'])
    target_file_path = 'jmrtd/src/main/java/org/jmrtd/WrappedAPDUEvent.java'

    ast_info = AstProcessor(BasicInfoListener()).execute(target_file_path)
    print(ast_info)