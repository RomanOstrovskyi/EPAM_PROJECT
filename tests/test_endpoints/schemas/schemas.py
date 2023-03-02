valid_schema = {
    "type": "object",
    "properties": {
        "Message": {"type": "string"},
    },
}

invalid_schema = {
    "type": "object",
    "properties": {
            "error": {"type": "string"},
        },
}
