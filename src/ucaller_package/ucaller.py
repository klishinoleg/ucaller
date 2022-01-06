import requests


class UCaller:
    BASE_URL = 'https://api.ucaller.ru/v1.0/'
    INIT_CALL_METHOD = 'initCall'
    INIT_REPEAT_METHOD = 'initRepeat'
    GET_INFO_METHOD = 'getInfo'
    GET_BALANCE_METHOD = 'getBalance'
    GET_SERVICE_METHOD = 'getService'
    with_data_response = True
    KEY = ''
    SERVICE_ID = ''

    def __init__(self, service_id, key, with_data_response=True):
        """
        set with_data_response False if you want to take boolean status and keep True for data response from init methods
        """
        self.KEY = key
        self.SERVICE_ID = service_id
        self.with_data_response = with_data_response

    def _get_url(self, method):
        return f'{self.BASE_URL}{method}'

    def _get_params(self, **kwargs):
        params = {
            'service_id': self.SERVICE_ID,
            'key': self.KEY
        }
        params.update(kwargs)
        return params

    def _request(self, method, **kwargs):
        response = requests.get(self._get_url(method),
                                params=self._get_params(**kwargs))
        response_data = response.json()
        if self.with_data_response:
            return response_data
        return response_data.get('status')

    def init_call(self, phone_number, code=None, client=None, unique=None):
        """
        https://ucaller.ru/doc#api31
        Init call to phone_number with code in 4 end numbers
        if code is None then code will be generated automatically, code must be 4 numbers
        unique - unique identifier 64 symbols maximum
        client - user's ID or other 64 symbols maximum
        """
        return self._request(self.INIT_CALL_METHOD, phone=phone_number, code=code, client=client, unique=unique)

    def init_repeat(self, uid):
        """
        https://ucaller.ru/doc#api32
        Free repeat call by ucaller_id from init_call response data
        """
        return self._request(self.INIT_REPEAT_METHOD, uid=uid)

    def get_info(self, uid):
        """
        https://ucaller.ru/doc#api33
        Get info by ucaller_id
        """
        return self._request(self.GET_INFO_METHOD, uid=uid)

    def get_balance(self):
        """
        https://ucaller.ru/doc#api34
        Get balance info
        """
        return self._request(self.GET_BALANCE_METHOD)

    def get_service(self):
        """
        https://ucaller.ru/doc#api35
        Get service info
        """
        return self._request(self.GET_SERVICE_METHOD)
