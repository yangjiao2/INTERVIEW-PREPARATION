import json
import random
# from collections import Counter

# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>> 
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>> 
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]

class TreeNode:
    def __init__(self, name, node_type, children=None):
        self.name = name
        self.type = node_type
        self.children = children or []

def delete_random_node(node):
    if not node.children:
        return None  # Cannot delete nodes with no children

    index = random.randint(0, len(node.children) - 1)
    deleted_node = node.children.pop(index)
    return deleted_node

def refine_tree(input_json):
    try:
        root_node = parse_json_to_tree(input_json)
        max_depth = find_max_depth(root_node)
        
        if max_depth <= 1:
            raise ValueError("Tree has insufficient depth for deletion.")

        layer = random.randint(1, max_depth)  # Choose a random layer between 1 and 5
        deleted_node = delete_random_node_at_layer(root_node, layer)
        output_json = json.dumps(root_node, default=lambda o: o.__dict__, indent=2)
        return {"output": output_json, "error_message": f"Deleted node: {deleted_node.name if deleted_node else None}"}
    except Exception as e:
        return {"output": None, "error_message": f"Error: {e}"}


def find_max_depth(node):
    if not node.children:
        return 1
    else:
        # Recursively find the maximum depth of the children
        child_depths = [find_max_depth(child) for child in node.children]
        return 1 + max(child_depths)


def delete_random_node_at_layer(node, layer):
    if layer == 1:
        return delete_random_node(node)
    else:
        # Traverse the tree to the specified layer
        current_layer = node
        for _ in range(layer - 1):
            if current_layer.children:
                current_layer = random.choice(current_layer.children)
            else:
                return None  # Cannot delete nodes beyond the available layers

        # Delete a random node from the specified layer
        return delete_random_node(current_layer)

def parse_json_to_tree(json_str):
    try:
        data = json.loads(json_str)
        if isinstance(data, dict):
            name = data.get("name", "")
            node_type = data.get("type", "")
            children = [parse_dict_to_tree(child) for child in data.get("children", [])]
            return TreeNode(name, node_type, children)
        raise ValueError(f"Input is not a dictionary: {data}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON: {e}")

# Example usage:
input_json1 = '{"name": "root", "type": "Root", "children": [{"name": "node1", "type": "TypeA", "children": [{"name": "child1", "type": "TypeB"}, {"name": "child2", "type": "TypeC"}]}, {"name": "node2", "type": "TypeA", "children": [{"name": "child3", "type": "TypeB"}, {"name": "child4", "type": "TypeC"}]}]}'
input_json2 = '{"name": "root", "type": "Root", "children": [{"name": "node3", "type": "TypeA", "children": [{"name": "child5", "type": "TypeB"}, {"name": "child6", "type": "TypeC"}]}, {"name": "node4", "type": "TypeA", "children": [{"name": "child7", "type": "TypeB"}, {"name": "child8", "type": "TypeC"}]}]}'

result1 = refine_tree(input_json1)
result2 = refine_tree(input_json2)

print("Tree 1:")
print(result1["output"])
print(result1["error_message"])

print("\nTree 2:")
print(result2["output"])
print(result2["error_message"])


