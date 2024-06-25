load("@cython_repo//Tools:rules.bzl", "pyx_library")
load("@rules_symforce//symengine_tools:config.bzl", "symenginepy_config")
load("@rules_symforce//symengine_tools:python.bzl", "cython_add_module_pyx")

package(default_visibility = ["//visibility:public"])

symenginepy_config(
    name = "config",
    output = "config.pxi",
    template = "config.pxi.in",
)

cython_flags = [
    "--cplus",
    "--fast-fail",
    #   "--lenient",
    "-3",
]

cython_add_module_pyx(
    # Cythonizes the .pyx files into .cpp file (but doesn't compile it)
    # produces symengine_wrapper.cpp
    name = "symengine_wrapper",
    srcs = [
        "config.pxi",
        "symengine.pxd",
        "symengine_wrapper.pxd",
    ],
    cython_flags = [
        "--cplus",
        "--fast-fail",
        #   "--lenient",
        "-3",
    ],
    output = "symengine_wrapper.cpp",
    pyx = "symengine_wrapper.pyx",
)

cc_library(
    name = "pywrapper",
    srcs = [
        "pywrapper.cpp",
    ],
    hdrs = [
        "py_callable_wrapper.h",
        "pywrapper.h",
    ],
    copts = [
        "-fno-strict-aliasing",
        "-Wno-unused-function",
    ],
    includes = [
        ".",
    ],
    deps = [
        "@python",
        "@symengine_repo//:symengine",
    ],
)

# TODO make this support linux and osx
cc_binary(
    name = "symengine_wrapper.so",
    srcs = [
        "symengine_wrapper.cpp",
    ],
    copts = [
        "-fno-strict-aliasing",
        "-Wno-unused-function",
        "-Wno-deprecated-volatile",
    ],
    linkshared = 1,
    deps = [
        ":pywrapper",
    ],
)

py_library(
    name = "lib",
    srcs = [
        "__init__.py",
    ],
    data = [
        "config.pxi",
        "symengine.pxd",
        "symengine_wrapper.pxd",
        "symengine_wrapper.pyx",
        ":symengine_wrapper.so",
    ],
)
