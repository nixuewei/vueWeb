from selenium import webdriver
chromeOptions = webdriver.ChromeOptions()

# 设置代理
chromeOptions.add_argument("--proxy-server=http://192.168.124.18:8080")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
browser = webdriver.Chrome(chrome_options = chromeOptions)
# 查看本机ip，查看代理是否起作用
browser.get("https://vhsupply.staging.viewchain.net")
