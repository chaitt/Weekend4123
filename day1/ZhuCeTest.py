from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("cjy")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_name("userpassword2").send_keys("123456")
driver.find_element_by_name("mobile_phone").send_keys("15890096748")
driver.find_element_by_name("email").send_keys("741211359@qq.com")
driver.find_element_by_class_name("reg_btn").click()