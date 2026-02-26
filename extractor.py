from schema import SCHEMA

OPERATORS = {
    "greater": ">",
    "less": "<",
    "equal": "=",
    "above": ">",
    "below": "<"
}

AGGREGATIONS = {
    "count": "COUNT",
    "average": "AVG",
    "avg": "AVG",
    "sum": "SUM"
}

def extract_table(tokens):
    for table in SCHEMA.keys():
        if table in tokens or table[:-1] in tokens:
            return table
    return None


def extract_columns(tokens, table):
    columns = []
    for col in SCHEMA[table]:
        if col in tokens:
            columns.append(col)

    if not columns:
        return ["*"]

    return columns


def extract_aggregation(tokens, columns):
    for word in tokens:
        if word in AGGREGATIONS:
            return AGGREGATIONS[word]
    return None


def extract_conditions(tokens, table):
    conditions = []
    tokens_len = len(tokens)

    for i in range(tokens_len):
        if tokens[i] in SCHEMA[table]:
            column = tokens[i]

            if i+2 < tokens_len:
                op_word = tokens[i+1]
                value = tokens[i+2]

                if op_word in OPERATORS:
                    operator = OPERATORS[op_word]

                    if value.isdigit():
                        conditions.append(f"{column} {operator} {value}")
                    else:
                        conditions.append(f"{column} {operator} '{value}'")

    return conditions
