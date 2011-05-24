from pyws.functions import NativeFunctionAdapter
from pyws.functions.args import String, Integer, Float, DictOf, Field, ListOf

def add_simple(a, b):
    return a + b

def add_dicts(p, q):
    return {
        'a': p['a'] + q['a'],
        'b': p['b'] + q['b'],
    }

def add_string_lists(p, q):
    if len(p) < len(q):
        p.extend([''] * (len(q) - len(p)))
    if len(q) < len(p):
        q.extend([''] * (len(p) - len(q)))
    return list(p[i] + q[i] for i in xrange(len(p)))

def add_integer_lists(p, q):
    if len(p) < len(q):
        p.extend([0] * (len(q) - len(p)))
    if len(q) < len(p):
        q.extend([0] * (len(p) - len(q)))
    return list(p[i] + q[i] for i in xrange(len(p)))

def sum_tree(p):
    return p and (p['value'] + \
        (p['left'] and sum_tree(p['left']) or 0) + \
        (p['right'] and sum_tree(p['right']) or 0)) or 0

def get_tree(p):
    if p == 0:
        return None
    if p == 1:
        return {'value': 1}
    if p == 2:
        return {'value': 2, 'left': None, 'right': None}
    return {
        'value': 3,
        'left': {'value': 4, 'left': None, 'right': None},
        'right': {'value': 5, 'left': None, 'right': None},
    }

add_integers_adapter = NativeFunctionAdapter(
    add_simple,
    name='add_integers',
    return_type=Integer,
    args=(
        (Integer, 0),
        (Integer, 0),
    ),
)

add_floats_adapter = NativeFunctionAdapter(
    add_simple,
    name='add_floats',
    return_type=Float,
    args=(
        (Float, 0),
        (Float, 0),
    ),
)

ABStringDict = DictOf('ABStringDict',
    ('a', String),
    ('b', String),
)

add_string_dicts_adapter = NativeFunctionAdapter(
    add_dicts,
    name='add_string_dicts',
    return_type=ABStringDict,
    args=(
        (ABStringDict, {'a': '', 'b': ''}),
        (ABStringDict, {'a': '', 'b': ''}),
    ),
)

ABIntegerDict = DictOf('ABIntegerDict',
    ('a', Integer, 0),
    ('b', Integer, 0),
)

add_integer_dicts_adapter = NativeFunctionAdapter(
    add_dicts,
    name='add_integer_dicts',
    return_type=ABIntegerDict,
    args=(
        (ABIntegerDict, {'a': 0, 'b': 0}),
        (ABIntegerDict, {'a': 0, 'b': 0}),
    ),
)

StringList = ListOf(String)

add_string_lists_adapter = NativeFunctionAdapter(
    add_string_lists,
    name='add_string_lists',
    return_type=StringList,
    args=(StringList, StringList),
)

IntegerList = ListOf(Integer, 0)

add_integer_lists_adapter = NativeFunctionAdapter(
    add_integer_lists,
    name='add_integer_lists',
    return_type=IntegerList,
    args=(IntegerList, IntegerList),
)

Tree = DictOf('Tree', ('value', Integer, 0))
Tree.add_fields(
    ('left', Tree),
    ('right', Tree),
)

sum_tree_adapter = NativeFunctionAdapter(
    sum_tree,
    return_type=Integer,
    args=(Tree, ),
)

get_tree_adapter = NativeFunctionAdapter(
    get_tree,
    return_type=Tree,
    args=(Integer, ),
)
