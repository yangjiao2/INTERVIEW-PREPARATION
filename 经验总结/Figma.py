
# https://www.1point3acres.com/bbs/thread-856868-1-1.html

# https://www.1point3acres.com/bbs/thread-919909-1-1.html

# apply(Layer(1, {"color": "green"}))
# apply(Layer(2, {"shape": "triangle", "color": "blue"}))
# apply(Layer(1, {"color": "pink"}))
# commit_batch()
# apply(Layer(1, {"color": "blue"}))
# apply(Layer(1, {"color": "white"}))
# commit_batch()

# 运行完这7行就是layer1 color white + layer2 shape triangle和color blue
# 如果redo的话会把5和6全部undo 变成layer1 color pink + layer2 shape triangle和color blue

# support redo和undo
# part 3: redo
# 就是‍‍‌‌‌‍‌‍‍‍‍‌‌‍‍‍‌把上一个undo 给redo了比第二问简单

1: {color: ['green', 'pink', 'pink', 'blue', 'white', 'pink', 'white']}

from collections import defaultdict

class Solution:

    def __init__(self):
        self.command_gc = []
        self.commands = []
        self.states = defaultdict(dict) # current state
        self.status = defaultdict(dict)


    def apply(self, i, actionitems): # dict
        for k, v in actionitems.items():
            if k in self.states[i]:
                self.states[i][k].append(v)
            else:
                self.states[i][k] = [v]
        self.commands.append([("apply", i, actionitems.keys())])

    def undo(self):
        self.command_gc.append(self.commands[-1])
        if self.commands[-1][0] == "apply":
            i, ks = self.commands[-1][1], self.commands[-1][2]
            for k in ks:
                self.states[i][k] = self.states[i][k][:-1]

        self.commands = self.commands[:-1]

    def commit(self):
        for layer, ks in self.states.items():
            for k, v in ks.items()
                self.status[i] = {k, v[-1]}
        self.states = defaultdict(dict)
        self.commands.append([("commit")])


    def redo(self):
        self.commands.append(self.command_gc[-1])






from collections import defaultdict
class Layer:
    def __init__(self, id, properties):
        self.id = id
        self.properties = properties

class Document:
    # Setup the initial document and all necessary data structures.
    def __init__(self, layers):
        # state, commands
        self.state = defaultdict(dict) # {layer: {key: [values] }}
        self.commands = []
        self.layers = {}

        for layer in layers:
            self.layers[layer.id] = layer
            for property, value  in layer.properties.items():
                self.state[layer.id][property] = [value]

    def layer_by_id(self, id):
        return self.layers[id]

    def apply(self, id, property, value):
        # add new value to states property
        self.commands.append(["apply", id, property])
        if property in self.state[id]:
            self.state[id][property].append(value)
        else:
            self.state[id][property] = [value]
        # update states
        temp_property = self.layers[id].properties
        temp_property.update({property: value})

        # update layer
        self.layers[id] = Layer(id, temp_property)


    def undo(self):
        # remove last commands's property
        if self.commands[-1][0] == "apply":
            id, property = self.commands[-1][1], self.commands[-1][2]

            # remove property from state
            self.state[id][property] =  self.state[id][property][:-1]
            prev = self.state[id][property][-1]

            # update property
            temp_property = self.layers[id].properties
            temp_property.update({property: prev})

        # remove commands
        self.commands = self.commands[:-1]

def assert_property_equals(document, layer_id, property, expected):
    actual = document.layer_by_id(layer_id).properties[property]
    assert actual == expected, "Expected layer {}'s {} to be: {}, but received {}.".format(layer_id, property, expected, actual)

def test_apply_and_undo():
    document = Document([
        Layer('a', { 'color': 'red' }),
        Layer('b', { 'shape': 'triangle' }),
    ])

    document.apply('a', 'color', 'green')
    document.apply('b', 'shape', 'square')
    document.apply('a', 'color', 'blue')

    document.undo()
    assert_property_equals(document, 'a', 'color', 'green')
    assert_property_equals(document, 'b', 'shape', 'square')

    document.apply('a', 'color', 'purple')
    assert_property_equals(document, 'a', 'color', 'purple')
    assert_property_equals(document, 'b', 'shape', 'square')

    document.undo()
    assert_property_equals(document, 'a', 'color', 'green')
    assert_property_equals(document, 'b', 'shape', 'square')

    document.undo()
    assert_property_equals(document, 'a', 'color', 'green')
    assert_property_equals(document, 'b', 'shape', 'triangle')

    document.undo()
    assert_property_equals(document, 'a', 'color', 'red')
    assert_property_equals(document, 'b', 'shape', 'triangle')

print("Running the tests..")
test_apply_and_undo()
print("Tests succeeded!")
