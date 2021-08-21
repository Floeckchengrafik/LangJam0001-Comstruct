from application_stack_utils import StatementNode


def out(args):
    for i in args:
        print(i, end=" ")

    print()


# This method is called "when" because it can´t be called if
def when(args):
    condition = args[0]
    if condition:
        return StatementNode.ExecuteStoredProcedureNode(args[1])


def _for(args):
    loop_limit = args[0]
    return StatementNode.ForLoopExecutorNode(args[1], loop_limit)


internals = {
    "function": lambda args: StatementNode.FunctionDefinitionNode(args[0], args[1:len(args)]),
    "out": out,
    "readline": lambda args: input(args[0] if len(args) == 1 else ""),
    "length": lambda args: len(args[0]),
    "if": when,
    "exit": lambda args: exit(args[0] if len(args) == 1 else 0),
    "for": _for,
    "list_add": lambda args: args[0].append(args[1]),
    "list_clear": lambda args: args[0].clear(),
    "list_extend": lambda args: args[0].extend(args[1]),
    "list_pop": lambda args: args[0].pop() if len(args) == 1 else args[0].pop(args[1]),
    "list_reverse": lambda args: args[0].reverse(),
    "list_sort": lambda args: args[0].sort(),
}

env = {
    "function": StatementNode.FunctionDefinitionNode("internal", []),
    "out": StatementNode.FunctionDefinitionNode("internal", []),
    "readline": StatementNode.FunctionDefinitionNode("internal", []),
    "length": StatementNode.FunctionDefinitionNode("internal", []),
    "if": StatementNode.FunctionDefinitionNode("internal", []),
    "exit": StatementNode.FunctionDefinitionNode("internal", []),
    "for": StatementNode.FunctionDefinitionNode("internal", []),
    "list_add": StatementNode.FunctionDefinitionNode("internal", []),
    "list_clear": StatementNode.FunctionDefinitionNode("internal", []),
    "list_extend": StatementNode.FunctionDefinitionNode("internal", []),
    "list_pop": StatementNode.FunctionDefinitionNode("internal", []),
    "list_reverse": StatementNode.FunctionDefinitionNode("internal", []),
    "list_sort": StatementNode.FunctionDefinitionNode("internal", []),
}
