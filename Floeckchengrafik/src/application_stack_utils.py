class StatementNode:
    class GenericNode:
        pass

    class MathNode(GenericNode):

        def __init__(self, _type, var1, var2):
            self.type = _type
            self.var1 = var1
            self.var2 = var2

    class EqualNode(GenericNode):

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class NotEqualNode(GenericNode):

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class GreaterThanNode(GenericNode):

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class GreaterOrEqualsThanNode(GenericNode):

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class SmallerThanNode(GenericNode):

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class SmallerOrEqualsThanNode(GenericNode):

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var2

    class VarAssignNode(GenericNode):

        def __init__(self, name, value):
            self.var_name = name
            self.var_value = value

    class VarNode(GenericNode):

        def __init__(self, name):
            self.var_name = name

    class LiterallyNode(GenericNode):

        def __init__(self, var, walk_function=None):
            self.var = var
            self.walk_function = walk_function

    class StoredProcedureNode(GenericNode):

        def __init__(self, content, description=None):
            self.content = content
            self.description = description

    class ExecuteStoredProcedureNode(GenericNode):

        def __init__(self, _exec, description=None):
            self.exec = _exec
            self.description = description

    class FunctionDefinitionNode(GenericNode):

        def __init__(self, content, args):
            self.content = content
            self.args = args

    class FunctionCallNode(GenericNode):

        def __init__(self, func_name, args):
            self.func_name = func_name
            self.args = args

    class ForLoopExecutorNode(GenericNode):

        def __init__(self, varname, tgetfrm, execute):
            self.varname = varname
            self.tgetfrm = tgetfrm
            self.execute = execute

    class FunctionDescriptionNode(GenericNode):

        def __init__(self, attrs):
            self.attributes = attrs