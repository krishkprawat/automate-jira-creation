class chromedriver:
        def launch(self):
                print("chrome launched")

class firefox:
        def launch(self):
                print("ff launched")

def testbrowser(driver):
        driver.launch()
        

fire=firefox()

chrome=chromedriver()
testbrowser(fire)
testbrowser(chrome)

