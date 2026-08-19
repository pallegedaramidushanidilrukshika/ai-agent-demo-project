# AI Agent Demo Project

An AI-powered Python code analysis and testing workflow using Gemini.

## Overview

This project demonstrates an agentic workflow that can analyze source code, generate tests, execute the tests, identify failures, generate fixes, apply the fixes, and verify the result.

## Workflow

1. Retrieve the project repository
2. Read the source code
3. Analyze the code using Gemini
4. Generate pytest test cases using Gemini
5. Save the generated tests
6. Execute the tests
7. Detect test failures
8. Send failure information to Gemini
9. Generate a code fix
10. Back up the original source code
11. Apply the generated fix
12. Run the tests again
13. Verify the final result

## Technologies

- Python
- Gemini API
- Google GenAI SDK
- Pytest
- GitHub

## Example

The demo project contains a simple calculator with:

- `add()`
- `divide()`

The agent intentionally detects test failures, generates a fix, applies the fix, and re-runs the tests.

## Result

The final workflow successfully demonstrates:

**Code Analysis → Test Generation → Test Execution → Failure Analysis → Fix Generation → Fix Application → Re-testing**
