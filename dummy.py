query=str("' OR '1'='1""")

query_tokens = {}
if query:
    for param in query.split('&'):
        key_value = param.split('=')
        if len(key_value) == 2:
            query_tokens[key_value[0]] = key_value[1]

