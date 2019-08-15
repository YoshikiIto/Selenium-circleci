from selenium import webdriver
import pytest
import os, glob

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = get_latest_modified_file_path("test-reports/images/")
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def get_latest_modified_file_path(dirname):
  target = os.path.join(dirname, '*')
  files = [(f, os.path.getmtime(f)) for f in glob(target)]
  latest_modified_file_path = sorted(files, key=lambda files: files[1])[-1]
  return latest_modified_file_path[0]