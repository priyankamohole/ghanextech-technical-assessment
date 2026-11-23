
import ast
import math
import operator

from langchain.tools import tool
from pydantic import BaseModel, Field


class CalculatorInput(BaseModel):
    expression: str = Field(
        description=(
            "Mathematical expression to calculate. "
            "Use Python arithmetic syntax, such as 25 * 4, "
            "sqrt(144), or 2 ** 5."
        )
    )


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

FUNCTIONS = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "factorial": math.factorial,
    "ceil": math.ceil,
    "floor": math.floor,
    "abs": abs,
    "round": round,
}


def safe_evaluate(node):
    if isinstance(node, ast.Constant):
        if type(node.value) not in (int, float):
            raise ValueError("Only numeric constants are allowed.")

        return node.value

    if isinstance(node, ast.BinOp):
        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported mathematical operator.")

        left = safe_evaluate(node.left)
        right = safe_evaluate(node.right)

        if isinstance(node.op, ast.Pow) and abs(right) > 100:
            raise ValueError("Exponent is too large.")

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        value = safe_evaluate(node.operand)

        if isinstance(node.op, ast.USub):
            return -value

        if isinstance(node.op, ast.UAdd):
            return value

        raise ValueError("Unsupported unary operator.")

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Invalid function call.")

        function = FUNCTIONS.get(node.func.id)

        if function is None:
            raise ValueError("Function is not allowed.")

        if node.keywords:
            raise ValueError("Keyword arguments are not allowed.")

        args = [safe_evaluate(arg) for arg in node.args]

        return function(*args)

    raise ValueError("Invalid mathematical expression.")


@tool(args_schema=CalculatorInput)
def calculator(expression: str) -> str:
    """
    Performs mathematical calculations safely.

    Use this tool whenever the user requests arithmetic,
    percentages, powers, square roots, or other supported
    mathematical calculations.
    """

    try:
        if len(expression) > 200:
            return "Error: Expression is too long."

        tree = ast.parse(expression, mode="eval")

        result = safe_evaluate(tree.body)

        if isinstance(result, complex):
            return "Error: Complex results are not supported."

        if not math.isfinite(float(result)):
            return "Error: Result is not finite."

        return f"Calculation: {expression} = {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except (ValueError, TypeError, OverflowError):
        return "Error: Invalid or unsupported mathematical expression."

    except Exception:
        return "Error: Unable to perform this calculation."
