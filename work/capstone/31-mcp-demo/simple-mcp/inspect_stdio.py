# inspect_stdio.py

from fastmcp.client import PythonStdioTransport
import inspect

print(inspect.signature(PythonStdioTransport))