from flask import Blueprint, jsonify, request

string_chopper = Blueprint(name='string_chopper', import_name='__name__')

@string_chopper.route('/', methods=['GET'])
def home():
    output = {"msg": "You've reached the test endpoint from string_chopper"}
    return jsonify(output)

@string_chopper.route('/test', methods=['GET', 'POST'])
def test():
    """
    ---
    post:
      description: Returns string which contains every third character from the original string
      requestBody:
        required: true
        content:
            application/json:
                schema: InputSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: OutputSchema
        '400':
          description: call failed
          content:
            application/json:
              schema: ErrorSchema
      tags:
          - string chopper
    """
    # get raw data
    try:
        raw_string = request.json['raw_string']
    except:
        error = 'Request body must be JSON object including key `raw_string` and a string value'
        return jsonify({"message": error}), 400
    if raw_string is not None:
        # string processing
        chopped_string = chop_string(raw_string)
        #return value
        res  = {"chopped_string": chopped_string}
        return jsonify(res), 200
def chop_string(str):
    chars = str[2::3]
    seq = "".join(chars)
    return seq
