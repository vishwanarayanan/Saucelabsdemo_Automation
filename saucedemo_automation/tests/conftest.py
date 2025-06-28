import tempfile
import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#Used Auto Driver Management


def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')
@pytest.fixture(scope="function")
def setup():
    # 1. Clear Cookies Instead of Creating Temp Profile (optional)
    #Creating a temp profile every test is good for isolation, but it’s slightly heavy.
    temp_profile=tempfile.mkdtemp()
    # disabling the google pop up for password management
    options = Options()
    prefs={
        "credentials_enable_service" : False ,
        "profile.password_manager_enabled" : False,
        "profile.default_content_setting_values.notifications": 2,
    }
    options.add_experimental_option("prefs", prefs)

    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--remote-allow-origins=*")
    #options.add_argument("--incognito")
    options.add_argument(f"--user-data-dir={temp_profile}")

    driver = webdriver.Chrome(options=options)
    #driver.delete_all_cookies()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

# This will hook into pytest's reporting
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    # Only add screenshot on test failure
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")  # 'setup' is your fixture name
        if driver is not None:
            # Create screenshot path
            screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            # Take screenshot
            driver.save_screenshot(file_path)

            # Attach to HTML report
            if file_path:
                html = f'<div><img src="{file_path}" alt="screenshot" style="width:500px;height:auto;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
    setattr(report, 'extra', extra)
