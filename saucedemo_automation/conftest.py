import tempfile
import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

#  Hook to capture HTML plugin
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

#  Add CLI option for browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests on: chrome, firefox, edge")

#  Main fixture with cross-browser support
@pytest.fixture(scope="function")
def setup(request):
    browser = request.config.getoption("--browser")
    temp_profile = tempfile.mkdtemp()

    if browser == "chrome":
        options = ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-extensions")
        options.add_argument("--remote-allow-origins=*")
        options.add_argument(f"--user-data-dir={temp_profile}")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.set_preference("dom.webnotifications.enabled", False)
        options.set_preference("signon.rememberSignons", False)
        options.set_preference("network.cookie.cookieBehavior", 2)
        driver = webdriver.Firefox(options=options)

    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(options=options)

    else:
        raise Exception(f"Browser '{browser}' is not supported.")

    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

#  Hook to attach screenshot to HTML report on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")
        if driver:
            screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            driver.save_screenshot(file_path)

            html = (
                f'<div><img src="{file_path}" alt="screenshot" style="width:500px;height:auto;" '
                f'onclick="window.open(this.src)" align="right"/></div>'
            )
            extra.append(pytest_html.extras.html(html))
    report.extra = extra
