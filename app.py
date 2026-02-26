# app.py

from tokenizer import tokenize
from intent import detect_intent
from extractor import extract_table, extract_columns, extract_aggregation, extract_conditions
from sql_builder import build_query
from database import execute_query


def text_to_sql(text):

    tokens = tokenize(text)

    intent = detect_intent(tokens)
    if not intent:
        return None, "Could not detect query type."

    table = extract_table(tokens)
    if not table:
        return None, "Table not found."

    columns = extract_columns(tokens, table)
    aggregation = extract_aggregation(tokens, columns)
    conditions = extract_conditions(tokens, table)

    sql_query = build_query(intent, table, columns, aggregation, conditions)

    return sql_query, None


if __name__ == "__main__":

    while True:
        user_input = input("\nEnter Query (type exit to quit): ")

        if user_input.lower() == "exit":
            break

        sql_query, error = text_to_sql(user_input)

        if error:
            print(error)
            continue

        print("\nGenerated SQL:")
        print(sql_query)

        result = execute_query(sql_query)

        print("\nResults:")
        print(result)
