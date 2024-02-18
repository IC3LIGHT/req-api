class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate_response(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)

        else:
            schema.model_validate(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, "Ошибка в коде ответа"

        else:
            assert self.response_status == status_code, "Ошибка в коде ответа"

    def assert_user_data(self, expected_data):
        for key, value in expected_data.items():
            assert self.response_json[
                       key] == value, f"Ошибка в данных пользователя: {key} не соответствует ожидаемому значению {value}"
