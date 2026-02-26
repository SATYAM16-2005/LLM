def build_query(intent, table, columns, aggregation, conditions):

    if aggregation:
        column_str = f"{aggregation}({columns[0]})"
    else:
        column_str = ", ".join(columns)

    query = f"{intent} {column_str} FROM {table}"

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += ";"

    return query
