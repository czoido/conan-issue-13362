
from conan import ConanFile
from conan.tools.files import copy
import os

class Base(ConanFile):
    version = "0.1"

    def export(self):
        copy(self, '*', src=os.path.dirname(__file__), dst=self.export_folder)
        print("Base export ----------->>>", os.path.join(self.export_folder, os.path.basename(__file__)))
        assert os.path.isfile( os.path.join(self.export_folder, os.path.basename(__file__)) )

    def build(self):
        self.output.info(f"build of {self.name}")

    def package_info(self):
        self.output.info(f"package_info of {self.name}")
        self.output.info(f"using conanfile_base {__file__}")
