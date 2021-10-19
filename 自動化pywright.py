from playwright.sync_api import sync_playwright


# 網頁截圖
with sync_playwright() as p:
    #brower = p.chromium.launch()
    brower = p.chromium.launch(headless=False)
    
    #訂製畫面大小
    # context = brower.new_context(
        # viewport={"width":750, "height":1334}
    # )
    
    
    page = brower.new_page()
    page.goto("https://www.google.com")
    #page.screenshot(path="pyout1.png")
    brower.close()


