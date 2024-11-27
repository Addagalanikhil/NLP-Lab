import re

# Function to parse FOPC expressions
def parse_fopc(expression):
    pattern = r'(\w+)\(([\w,]+)\)'  # Pattern for predicates with arguments
    match = re.match(pattern, expression)
    if match:
        predicate = match.group(1)
        arguments = match.group(2).split(",")
        return {"predicate": predicate, "arguments": arguments}
    else:
        return "Invalid FOPC expression"

# Input expression
expression = "likes(John,Mary)"
parsed = parse_fopc(expression)
print("Parsed FOPC Expression:", parsed)
