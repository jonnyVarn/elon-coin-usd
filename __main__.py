from convert.converter import Converter

converter=Converter()


user_input_str=input('Elon coin amount')
user_input_int=int(user_input_str)

result = converter.to_usd(user_input_int)

print('USD: {}'.format(result))
