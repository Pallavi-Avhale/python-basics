# from selenium import webdriver
#
# driver=webdriver.Chrome()
#
# driver.get("https://www.youtube.com/")
#
# driver.close()
import time

print("------------------------------------------")


# from selenium import webdriver
#
# c_options = webdriver.ChromeOptions()
# c_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=c_options)
# driver.get("https://www.youtube.com/")

# print("------------------------------------------")

# from selenium import webdriver

# c_options = webdriver.ChromeOptions()
# c_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=c_options)
# driver.get("https://www.facebook.com")
# driver.get("https://www.youtube.com")


# time.sleep(2)
# driver.maximize_window()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# time.sleep(2)
# driver.close()


'''
ctrl + shift + i to check the url_page or web page code 

insted of using this use right click and select inspect it eill directly open code page

'''



print("------------------------------------------")

# from selenium import webdriver

# c_options = webdriver.ChromeOptions()
# c_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=c_options)
# driver.get("https://demowebshop.tricentis.com/")

# driver.find_element("id","small_search-terms").send_keys("Cricket")         # id=attribute , value = small_searchterms

# driver.maximize_window()

# time.sleep(2)
# driver.close()


from selenium import webdriver

c_options = webdriver.ChromeOptions()
c_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=c_options)
driver.get("https://demowebshop.tricentis.com/")
driver.find_element("id","small-searchterms").send_keys("cricket")