instructions = """
You are given a Advanced level Physics or Mathematics problem.
Your task is to:
1. Carefully understand the entire problem.
2. Rewrite it into a shorter, cleaner version while preserving ALL mathematical information, assumptions, constraints, symbols, equations, units, and conditions. Do NOT change the meaning or difficulty of the problem.
3. Write Python code that models or solves the simplified problem whenever appropriate. Use libraries such as:
   - numpy
   - scipy
   - sympy
   - pandas (only if useful)
   - matplotlib (for visualizations)
   - jax (only if automatic differentiation or numerical optimization is beneficial)
4. The code should:
   - Be logically structured.
   - Contain concise, informative comments.
   - Use meaningful variable names.
   - Show intermediate computations when they help explain the solution.
   - Produce the required numerical or symbolic result.
5. Do NOT explain the mathematics in natural language. The Python code and comments should provide enough information for another LLM to generate the complete solution and explanation.
6. Preserve exact notation, constants, units, and mathematical expressions whenever possible.
7. If the problem cannot reasonably be solved using code alone, generate code that models the mathematical expressions, performs relevant computations, verifies important identities, or visualizes the situation to aid the final explanation.

The output should contain only:
1. The simplified problem.
2. The Python code.
"""

