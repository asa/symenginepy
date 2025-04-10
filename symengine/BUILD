load("@rules_python//python:py_library.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "symengine",
    srcs = [
        "__init__.py",
        "functions.py",
        "printing.py",
        "sympy_compat.py",
        "utilities.py",
    ],
    deps = [
        "//symengine/lib",
    ],
)

py_test(
    name = "test_arit",
    srcs = glob(["tests/test_arit.py"]),
    deps = [
        ":symengine",
    ],
)
