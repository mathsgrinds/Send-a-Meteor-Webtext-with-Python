#!/usr/bin/env python

def meteor(message="", yournumber="", username="", password="", theirnumber="", headless=True):
    import time
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.common.keys import Keys
    try:
        from pyvirtualdisplay import Display
    except:
        pass
    number = yournumber[1:]
    if theirnumber == "":
        theirnumber = yournumber
    theirnumber = theirnumber[1:]
    try:
        if headless:
            try:
                display=Display(visible=0,size=(1024,768))
                display.start()
            except:
                pass
            try:
                binary = FirefoxBinary('/usr/bin/firefox')
            except:
                pass
            profile = webdriver.FirefoxProfile()
            profile.native_events_enabled = False
            profile.set_preference('permissions.default.stylesheet', 2)
            profile.set_preference('permissions.default.image', 2)
            profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
            profile.set_preference("network.http.pipelining", True)
            profile.set_preference("network.http.proxy.pipelining", True)
            profile.set_preference("network.http.pipelining.maxrequests", 8)
            profile.set_preference("content.notify.interval", 500000)
            profile.set_preference("content.notify.ontimer", True)
            profile.set_preference("content.switch.threshold", 250000)
            profile.set_preference("browser.cache.memory.capacity", 65536)
            profile.set_preference("browser.startup.homepage", "about:blank")
            profile.set_preference("reader.parse-on-load.enabled", False)
            profile.set_preference("browser.pocket.enabled", False)
            profile.set_preference("loop.enabled", False)
            profile.set_preference("browser.chrome.toolbar_style", 1)
            profile.set_preference("browser.display.show_image_placeholders", False)
            profile.set_preference("browser.display.use_document_colors", False)
            profile.set_preference("browser.display.use_document_fonts", 0)
            profile.set_preference("browser.display.use_system_colors", True)
            profile.set_preference("browser.formfill.enable", False)
            profile.set_preference("browser.helperApps.deleteTempFileOnExit", True)
            profile.set_preference("browser.shell.checkDefaultBrowser", False)
            profile.set_preference("browser.startup.homepage", "about:blank")
            profile.set_preference("browser.startup.page", 0)
            profile.set_preference("browser.tabs.forceHide", True)
            profile.set_preference("browser.urlbar.autoFill", False)
            profile.set_preference("browser.urlbar.autocomplete.enabled", False)
            profile.set_preference("browser.urlbar.showPopup", False)
            profile.set_preference("browser.urlbar.showSearch", False)
            profile.set_preference("extensions.checkCompatibility", False)
            profile.set_preference("extensions.checkUpdateSecurity", False)
            profile.set_preference("extensions.update.autoUpdateEnabled", False)
            profile.set_preference("extensions.update.enabled", False)
            profile.set_preference("general.startup.browser", False)
            profile.set_preference("plugin.default_plugin_disabled", False)
            profile.set_preference("permissions.default.image", 2)
            try:
                browser = webdriver.Firefox(firefox_profile=profile,firefox_binary=binary)
            except:
                try:
                    browser = webdriver.Firefox(firefox_profile=profile)
                except:
                    browser = webdriver.Firefox() 
            browser.set_window_size(1024, 768)
            browser.maximize_window()
        else:
            browser = webdriver.Firefox()
            browser.maximize_window()
        ###--------------------- START ---------------------###
        browser.get('https://my.meteor.ie/meteor/transactional/login')
        time.sleep(1)
        for usernamefield in browser.find_elements_by_id("username"):
            try:
                usernamefield.send_keys(username+"\t")
                time.sleep(1)
            except:
                pass
        time.sleep(1)
        for usernamefield in browser.find_elements_by_id("password"):
            try:
                usernamefield.send_keys(password+"\t")
                time.sleep(1)
            except:
                pass
        time.sleep(1)
        for submit in browser.find_elements_by_id("submit"):
            try:
                submit.click()
                time.sleep(1)
            except:
                pass
        time.sleep(1)
        browser.get("https://my.meteor.ie/webtext/page/main?msisdn=+353"+number+"#send:")
        time.sleep(10)
        browser.find_element_by_xpath("//body").send_keys(str("\t\t\t\t\t\t\t"+str(message)+"\t"+"0"+theirnumber))
        time.sleep(1)
        browser.find_element_by_link_text("Send").click()
        time.sleep(1)
        ###---------------------- END ----------------------###
        time.sleep(1)
        browser.close()
        time.sleep(1)
        try:
            display.stop()
        except:
            pass
        return True
    except:
        try:
            display.stop()
        except:
            pass        
        return False
