package(default_visibility = ["//visibility:public"])

py_library(
        name = "symengine",
        srcs = [
                "__init__.py",
                "printing.py",
                "functions.py",
                "utilities.py",
                "sympy_compat.py",
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
