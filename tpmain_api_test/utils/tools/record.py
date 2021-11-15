import allure


def record(body, title: str = ""):
    allure.attach(str(body), str(title), allure.attachment_type.TEXT)
