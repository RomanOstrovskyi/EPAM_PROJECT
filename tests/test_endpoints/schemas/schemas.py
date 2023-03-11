"""Schemas fro testing"""
valid_schema = {
    "type": "object",
    "properties": {
        "Message": {"type": "string"},
    },
}

valid_get_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "lastname": {"type": "string"},
            "email": {"type": "string", "format": "email"}
        },
        "required": ["id", "name", "lastname", "date_of_birth", "email"],
    }
}

valid_get_by_email_date_of_birth_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "lastname": {"type": "string"},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["id", "name", "lastname", "date_of_birth", "email"],
}

invalid_schema = {
    "type": "object",
    "properties": {
            "error": {"type": "string"},
        },
}
