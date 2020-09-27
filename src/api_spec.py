"""OpenAPI v3 Specification"""

# apispec via OpenApi
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

# Create an APISpec
spec = APISpec(
    title="String Chopper",
    version="1.0.0",
    openapi_version="3.0.3",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Define schemas
class InputSchema(Schema):
    raw_string = fields.String(description="A string to be processed", required=True)

class OutputSchema(Schema):
    chopped_string = fields.String(description="A string containing every third letter from the raw_string parameter")

class ErrorSchema(Schema):
    message = fields.String(description="An error message")

# register schemas with spec
spec.components.schema("Input", schema=InputSchema)
spec.components.schema("Output", schema=OutputSchema)

# add swagger tags that are used for endpoint annotation
tags = [
            {"name": "string chopper",
             "description": "Funtion for processing a string"
            },
       ]

for tag in tags:
    print(f"Adding tag: {tag['name']}")
    spec.tag(tag)