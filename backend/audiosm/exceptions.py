from flask import jsonify


def template(data, code=500):
    return {'message': {'errors': {'body': data}}, 'status_code': code}


USER_NOT_FOUND = template(['User not found'], code=404)
USER_ALREADY_REGISTERED = template(['User already registered'], code=422)
UKNOWN_ERROR = template([], code=500)
ARTICLE_NOT_FOUND = template(['Article not found'], code=404)
COMMENT_NOT_OWNED = template(['Not your article'], code=422)
FILE_NOT_FOUND = template(['File not found'], code=404)
STREAM_NOT_FOUND = template(['File not found'], code=404)
JOB_NOT_FOUND = template(['Job not found'], code=404)


class InvalidUsage(Exception):
    status_code = 500

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_json(self):
        rv = self.message
        return jsonify(rv)

    @classmethod
    def user_not_found(cls):
        return cls(**USER_NOT_FOUND)

    @classmethod
    def user_already_registered(cls):
        return cls(**USER_ALREADY_REGISTERED)

    @classmethod
    def unkown_error(cls):
        return cls(**UKNOWN_ERROR)

    @classmethod
    def article_not_found(cls):
        return cls(**ARTICLE_NOT_FOUND)

    @classmethod
    def comment_not_owned(cls):
        return cls(**COMMENT_NOT_OWNED)

    @classmethod
    def job_not_found(cls):
        return cls(**JOB_NOT_FOUND)

    @classmethod
    def file_not_found(cls):
        return cls(**FILE_NOT_FOUND)

    @classmethod
    def stream_not_found(cls):
        return cls(**STREAM_NOT_FOUND)
