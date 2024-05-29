import time
from selenium import webdriver
from selenium.webdriver.common.by import By

tracking_id = "17654016023"
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://eskycargo.emirates.com/app/offerandorder/#/home/find-offer")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH, '//input[@placeholder="Doc. No. e.g.: 17602268011"]').send_keys(tracking_id)
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='mcf__btn -state-secondary ng-star-inserted']").click()
driver.find_element(By.XPATH, "//button[@class='mcf__btn -state-secondary ng-star-inserted']").click()
time.sleep(1)
driver.find_element(By.XPATH, '//span[normalize-space()="Show Details"]').click()
time.sleep(1)
places = driver.find_elements(By.XPATH, "//span[@class='simple-journey-airport']")
data1 = {"doc_no": tracking_id,
         "cargo_type": driver.find_element(By.XPATH, '//span[@class="cargo-type"]').text,
         "jrn_no": driver.find_element(By.XPATH, "//span[@class='order-id']/b").text,
         "going from": places[0].text,
         "going to": places[1].text}
time.sleep(1)
data2 = {
    driver.find_element(By.XPATH, "//div[@class='col-xs-2 col-md-2 col-lg-2']/span[1]").text:  # pieces
        driver.find_element(By.XPATH, "//div[@class='col-xs-2 col-md-2 col-lg-2']/span[2]").text,  # 4
    driver.find_element(By.XPATH, "//span[normalize-space()='Gross Weight']").text:  # gross weight
        driver.find_element(By.XPATH, "//div[@class='col-xs-4 col-sm-3 col-md-3 col-lg-3'][1]/span[2]").text,  # 1217 k
    driver.find_element(By.XPATH, "//div[@class='col-xs-4 col-sm-3 col-md-3 col-lg-3'][2]/span[1]").text:
        driver.find_element(By.XPATH, "//div[@class='col-xs-4 col-sm-3 col-md-3 col-lg-3'][2]/span[2]").text,
    driver.find_element(By.XPATH, "//div[@class='col-xs-5 col-sm-3 col-md-3 col-lg-3 ng-star-inserted']/span[1]").text:
        driver.find_element(By.XPATH,
                            "//div[@class='col-xs-5 col-sm-3 col-md-3 col-lg-3 ng-star-inserted']/span[2]").text,
}
data3 = {
    driver.find_element(By.XPATH, "//div[@class='col-xs-5 col-sm-6 col-md-4 col-lg-3 ng-star-inserted']/span[1]").text:
        driver.find_element(By.XPATH,
                            "//div[@class='col-xs-5 col-sm-6 col-md-4 col-lg-3 ng-star-inserted']/span[2]").text,
    driver.find_element(By.XPATH, "//div[@class='col-xs-5 col-sm-6 col-md-4 col-lg-4']/span[1]").text:
        driver.find_element(By.XPATH, "//div[@class='col-xs-5 col-sm-6 col-md-4 col-lg-4']/span[2]").text,
    driver.find_element(By.XPATH, "//b[normalize-space()='SHCs']").text:
        driver.find_element(By.XPATH, "//i[@class='black-text']").text
}
driver.find_element(By.XPATH, '//*[@id="trackingDetailsundefined"]').click()
time.sleep(2)
no_stops = driver.find_element(By.XPATH, "//span[@class='stops ng-star-inserted']").text[1]
driver.find_element(By.XPATH, "(//ng-select[@role='listbox'])[1]").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Least Recent']").click()
time.sleep(3)
milestones = driver.find_elements(By.XPATH, "//ul[@class='milestone']/li")
data4 = []


def separate(x):  # returns split values of string containing value of status location and time
    location = x.split(",")[0]
    Time = x.split(",")[1]
    return location, Time


for i in range(0, len(milestones)):  # loop1
    x = len(driver.find_elements(By.XPATH, "//ul[@class='milestone']/li[" + str(
        i + 1) + "]//div"))  # checking number of div tags in each card
    if x == 7:
        status = \
            driver.find_elements(By.XPATH, "(//div[@class='row-container'])[2]//p[@class='milestone-description']")[
                i].text
        status_location_time = driver.find_element(By.XPATH,
                                                   "//ul[@class='milestone']/li[" + str(i + 1) + "]//div[2]/p[1]").text
        status_date = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(i + 1) + "]//div[2]/p[2]").text
        pieces = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(i + 1) + "]//div[5]/p[1]").text
        grossWeight = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(i + 1) + "]//div[5]/p[2]").text
        location, time = separate(status_location_time)
        data = {"status": status,
                "status date": status_date,
                'pieces': pieces,
                "gross weight": grossWeight,
                "status location": location,
                "status time": time}
        data4.append(data)
    elif x == 10:  # for the cards with 10 div elements
        status = \
            driver.find_elements(By.XPATH, "(//div[@class='row-container'])[2]//p[@class='milestone-description']")[
                i].text
        status_location_time = driver.find_element(By.XPATH,
                                                   "//ul[@class='milestone']/li[" + str(i + 1) + "]//div[2]/p[1]").text
        status_date = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(i + 1) + "]//div[2]/p[2]").text
        pieces = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(i + 1) + "]//div[5]/p[1]").text
        grossWeight = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(i + 1) + "]//div[5]/p[2]").text
        source = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(
            i + 1) + "]//span[@class='col-xs-2 col-lg-2']/b").text
        destination = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(
            i + 1) + "]//span[@class='col-xs-5 col-lg-2 ']/b").text
        plannedTimeAtSource = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(
            i + 1) + "]//div[@class='journey-steps row journey-dates ng-star-inserted']//span[@class='col-xs-7 col-lg-7']").text
        plannedTimeAtDestination = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(
            i + 1) + "]//div[@class='journey-steps row journey-dates ng-star-inserted']//span[@class='col-xs-5 col-lg-5 ']").text
        plannedDateAtSource = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(
            i + 1) + "]//div[@class='journey-steps journey-dates row ng-star-inserted']//span[@class='col-xs-7 col-lg-7']").text
        plannedDateAtDestination = driver.find_element(By.XPATH, "//ul[@class='milestone']/li[" + str(
            i + 1) + "]//div[@class='journey-steps journey-dates row ng-star-inserted']//span[@class='col-xs-5 col-lg-5 ']").text
        location, time = separate(status_location_time)
        data = {"status": status,
                "status date": status_date,
                "source": source,
                "destination": destination,
                "planned time at source": plannedTimeAtSource,
                "planned time at destination": plannedTimeAtDestination,
                "planned date at source": plannedDateAtSource,
                "planned date at destination": plannedDateAtDestination,
                'pieces': pieces,
                "gross weight": grossWeight,
                "status location": location,
                "status time": time}
        data4.append(data)
print(data1)
print()
print()
print(data2)
print()
print()
print(data3)
print()
print()
print(" No of stops= ", no_stops)
print()
print()
print("----------MILESTONES-----------")
for i in data4:
    print(i)
    print()
