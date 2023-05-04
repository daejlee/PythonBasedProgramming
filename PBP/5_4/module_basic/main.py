# import test_module as test
# import test_package.__init as i
# from test_package import *
# # radius = test.number_input()
# # print(test.get_circumference(radius))
# # print(test.get_circle_area(radius))

# # print(__name__)

from urllib import request

target = request.urlopen("https://img1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/32E9/image/BA2Qyx3O2oTyEOsXe2ZtE8cRqGk.JPG")
output = target.read()
print(output)

file = open("output.jpg", 'wb')
file.write(output)
file.close
