from datetime import datetime

input_string = '20180105120130'
date_format = '%Y%m%d%H%M%S'

date_object = datetime.strptime(input_string, date_format)
print(date_object)

output_string = date_object.strftime(date_format)
print(output_string)
