
import conanfile_base

class Pkg(conanfile_base.Base):
    name = "app"
    exports = "conanfile_base.py"

    def requirements(self):
        self.requires("pkg1/0.1")
        self.requires("pkg2/0.1")
        self.output.info(f"using conanfile_base {conanfile_base.__file__}")
