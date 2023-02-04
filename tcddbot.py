
from selenium import webdriver
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager

import time
try:
    while True:
        wd = webdriver.Chrome(ChromeDriverManager().install())
        wd.implicitly_wait(5)
        wd.get("https://ebilet.tcddtasimacilik.gov.tr/view/eybis/tnmGenel/tcddWebContent.jsf")


        nereden_input = wd.find_element_by_id('nereden') # Ankara Gar
        nereye_input = wd.find_element_by_id('nereye') # İstanbul(Pendik)

        date_input = wd.find_element_by_id('trCalGid_input') # 13.07.2022

        ara_button = wd.find_element_by_id('btnSeferSorgula') # Ara

        nereden_input.send_keys('İstanbul(Pendik)')

        nereye_input.send_keys('Ankara Gar')

        date_input.clear()
        date_input.send_keys('04.02.2023')
        date_input_close = wd.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div[2]/button[2]')
        date_input_close.click()

        ara_button.click()
        wd.implicitly_wait(2)

        tren_parent = wd.find_elements_by_xpath('//*[@id="mainTabView:gidisSeferTablosu_data"]//tr')
        # num_trains = len(tren_parent.find_elements_by_xpath(".//tr"))
        # print(f'toplam {len(tren_parent)-1} tren var')
        for i in range(len(tren_parent)-1):
            try:
                # print(wd.find_elements_by_xpath(f'//*[starts-with(@id, "mainTabView:gidisSeferTablosu:{i}") and contains(@id, "somVagonTipiGidis1_panel")]/div/ul/li'))
                ekonomi = wd.find_elements_by_xpath(f'//*[starts-with(@id, "mainTabView:gidisSeferTablosu:{i}") and contains(@id, "somVagonTipiGidis1_panel")]/div/ul/li')[0].get_attribute('data-label')
                business = wd.find_elements_by_xpath(f'//*[starts-with(@id, "mainTabView:gidisSeferTablosu:{i}") and contains(@id, "somVagonTipiGidis1_panel")]/div/ul/li')[1].get_attribute('data-label')
                
                ekonomi_koltuk = int(ekonomi.split('(')[-1][:-1])
                business_koltuk = int(business.split('(')[-1][:-1])
                if ekonomi_koltuk > 2 or business_koltuk > 0:
                    print(f'{i}. trende ekonomi koltuk sayısı: {ekonomi_koltuk}, business koltuk sayısı: {business_koltuk}')
                # print(ekonomi_koltuk)
                # print(business_koltuk)
            except:
                print(f'toplam {i-1} tren var')
                break

        wd.quit()
        time.sleep(60*1)
except KeyboardInterrupt:
    quit()