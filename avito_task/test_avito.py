import os


os.makedirs("output", exist_ok=True)


def test_1_x_1(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="0.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "1.1.1.png")
    screenshot_path_2 = os.path.join("output", "1.2.1.png")
    screenshot_path_3 = os.path.join("output", "1.3.1.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)


def test_1_x_2(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="999.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "1.1.2.png")
    screenshot_path_2 = os.path.join("output", "1.2.2.png")
    screenshot_path_3 = os.path.join("output", "1.3.2.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)


def test_2_x_1(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="1000.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "2.1.1.png")
    screenshot_path_2 = os.path.join("output", "2.2.1.png")
    screenshot_path_3 = os.path.join("output", "2.3.1.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)


def test_2_x_2(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="999999.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "2.1.2.png")
    screenshot_path_2 = os.path.join("output", "2.2.2.png")
    screenshot_path_3 = os.path.join("output", "2.3.2.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)


def test_3_x_1(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="1000000.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "3.1.1.png")
    screenshot_path_2 = os.path.join("output", "3.2.1.png")
    screenshot_path_3 = os.path.join("output", "3.3.1.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)


def test_3_x_2(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="999999999.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "3.1.2.png")
    screenshot_path_2 = os.path.join("output", "3.2.2.png")
    screenshot_path_3 = os.path.join("output", "3.3.2.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)


def test_4_x_1(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="1000000000.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "4.1.1.png")
    screenshot_path_2 = os.path.join("output", "4.2.1.png")
    screenshot_path_3 = os.path.join("output", "4.3.1.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)


def test_4_x_2(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="999999999999.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "4.1.2.png")
    screenshot_path_2 = os.path.join("output", "4.2.2.png")
    screenshot_path_3 = os.path.join("output", "4.3.2.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)


def test_5_x_1(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="1000000000000.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "5.1.1.png")
    screenshot_path_2 = os.path.join("output", "5.2.1.png")
    screenshot_path_3 = os.path.join("output", "5.3.1.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)


def test_5_x_2(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="999999999999999.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "5.1.2.png")
    screenshot_path_2 = os.path.join("output", "5.2.2.png")
    screenshot_path_3 = os.path.join("output", "5.3.2.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)


def test_6_x(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="1000000000000000.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "6.1.png")
    screenshot_path_2 = os.path.join("output", "6.2.png")
    screenshot_path_3 = os.path.join("output", "6.3.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)


def test_7_x(page):
    page.route(
        "**/web/1/charity/ecoImpact/init",
        lambda route: route.fulfill(path="fractional.json"),
    )
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    counter_1 = page.locator(".desktop-impact-item-eeQO3").nth(1)
    counter_2 = page.locator(".desktop-impact-item-eeQO3").nth(3)
    counter_3 = page.locator(".desktop-impact-item-eeQO3").nth(5)

    screenshot_path_1 = os.path.join("output", "7.1.png")
    screenshot_path_2 = os.path.join("output", "7.2.png")
    screenshot_path_3 = os.path.join("output", "7.3.png")

    counter_1.screenshot(path=screenshot_path_1)
    counter_2.screenshot(path=screenshot_path_2)
    counter_3.screenshot(path=screenshot_path_3)
