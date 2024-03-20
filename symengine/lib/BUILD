package(default_visibility = ["//visibility:public"])

load("@cython//Tools:rules.bzl", "pyx_library")
load("@rules_symforce//symengine_tools:config.bzl", "symenginepy_config")
load("@rules_symforce//symengine_tools:python.bzl", "cython_add_module_pyx")
#load("@rules_symforce//symengine_tools:python.bzl", "add_python_library")

symenginepy_config(
     name="config",
     template = "config.pxi.in",
     output = "config.pxi",
)
cython_flags = [ "--cplus", 
                     "--fast-fail", 
                  #   "--lenient", 
                     "-3"]
#pyx_library(
#    name = "symengine_wrapper_test",
#    srcs = [
#        "symengine_wrapper.pyx",
#        "config.pxi",
#        "symengine_wrapper.pxd",
#        "symengine.pxd",
#    ],
##    cython_directives = cython_flags,
#)

cython_add_module_pyx(
# Cythonizes the .pyx files into .cpp file (but doesn't compile it)
    # produces symengine_wrapper.cpp
    name = "symengine_wrapper",
    pyx = "symengine_wrapper.pyx",
    srcs = [
            "symengine_wrapper.pxd",
            "symengine.pxd",
            "config.pxi",
    ],
    cython_flags = [ "--cplus", 
                     "--fast-fail", 
                  #   "--lenient", 
                     "-3"],
    output = "symengine_wrapper.cpp",
)


cc_library(
        name = "pywrapper",
        hdrs = [
                "pywrapper.h",
                "py_callable_wrapper.h",
        ],        
        srcs = [
                "pywrapper.cpp",
        ],
        copts = [   
             "-fno-strict-aliasing", 
             "-Wno-unused-function",
        ],        
        includes = [
            "."
        ],
        deps = [
            "@symengine_repo//:symengine",
            "@python",
        ],
)

cc_binary(
        name = "symengine_wrapper.so",
        srcs = [
                "symengine_wrapper.cpp",
        ],
        linkshared = 1,
        deps = [
                ":pywrapper",
        ],
    copts = [   
             "-fno-strict-aliasing", 
             "-Wno-unused-function",
             "-Wno-deprecated-volatile",
    ],
)

py_library(
        name = "lib",
        srcs = [
                "__init__.py",
        ],
        deps = [
        ],
        data = [
            ":symengine_wrapper.so",
            "symengine_wrapper.pxd",
            "symengine_wrapper.pyx",
            "symengine.pxd",
            "config.pxi",
        ],
)
