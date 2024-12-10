def parse_rules(rules_text):
    rules = {}
    for rule in rules_text.split('\n'):
        before, after = map(int, rule.split('|'))
        rules.setdefault(before, set()).add(after)
    return rules

def is_order_valid(update, rules):
    # Convert update to a list if it isn't already
    update = list(update)
    
    # Check each rule that involves pages in this update
    for i, page in enumerate(update):
        for j, next_page in enumerate(update[i+1:], start=i+1):
            # If there's a rule saying 'page' must come before 'next_page'
            if page in rules and next_page in rules[page]:
                # If 'page' appears after 'next_page', order is invalid
                if update.index(page) > update.index(next_page):
                    return False
    return True

def solve_page_order(input_text):
    # Split input into rules and updates
    rules_text, updates_text = input_text.strip().split('\n\n')
    
    # Parse rules
    rules = parse_rules(rules_text)
    
    # Process updates
    updates = [list(map(int, update.split(','))) for update in updates_text.split('\n')]
    
    # Find valid updates and their middle pages
    valid_middle_pages = []
    
    for update in updates:
        if is_order_valid(update, rules):
            # Find middle page of the correctly ordered update
            middle_index = len(update) // 2
            valid_middle_pages.append(update[middle_index])
    
    # Return sum of middle pages
    return sum(valid_middle_pages)

# Read input from file
with open('input.txt', 'r') as file:
    input_text = file.read()

result = solve_page_order(input_text)
print(result)