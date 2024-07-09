from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class SocialNetworkRecipe(ConanFile):
    name = "SocialNetwork"
    version = "0.4.1"
    package_type = "application"

    # Optional metadata
    license = "Apache-2.0"
    author = "(various)"
    url = "https://github.com/delimitrou/DeathStarBench"
    description = "Open-source benchmark suite for cloud microservices"
    topics = ("benchmark", "cloud", "microservices")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("amqp-cpp/4.3.26")
        self.requires("boost/1.85.0")
        self.requires("cpp-jwt/1.4")
        self.requires("libmemcached/1.0.18")
        self.requires("mongo-c-driver/1.27.3")
        self.requires("nlohmann_json/3.11.3")
        self.requires("openssl/3.2.2")
        self.requires("opentracing-cpp/1.6.0")
        self.requires("redis-plus-plus/1.3.12")
        self.requires("thrift/0.20.0")
        self.requires("yaml-cpp/0.8.0")
        #
        self.tool_requires("thrift/0.20.0")

    def configure(self):
        self.options["redis-plus-plus"].with_tls = True
        self.options["hiredis"].with_ssl = True
        
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
