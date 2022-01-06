# ucaller

# Установка

pip install ucaller

# Использование

from ucaller_package.ucaller import UCaller

SERVICE_ID = ''
KEY = ''
uc = UCaller(service_id=SERVICE_ID, key=KEY)

# Первый звонок
init_call = uc.init_call(phone_number=79999999999)

# Повторный бесплатный звонок
repeat_free_call = uc.init_repeat(uid=init_call.get('ucaller_id'))

# Баланс
balance = uc.get_balance()

# Информация о звонке
info = uc.get_info(uid=init_call.get('ucaller_id')



