import login_user as user_info

booked_global = 0
waitlisted_global = 0
already_booked_global = 0
tuesday_and_thursday_bookings = 0

def log_booking_detailed():
    log_booking_detailed()

def log_booking_status():
    global booked_global, waitlisted_global, already_booked_global, tuesday_and_thursday_bookings

    schedule_page = user_info.driver.find_elements(
        user_info.By.XPATH,
        "//div[starts-with(@id, 'day-group-')]"
    )

    for day_group in schedule_page:
        class_elements = day_group.find_elements(
            user_info.By.XPATH,
            ".//div[starts-with(@id, 'class-card-')]"
        )
        class_element_id = day_group.get_property("id")
        tue_or_thu_flag = False
        if class_element_id.find("tue") != -1 or class_element_id.find("thu")!= -1:
            tue_or_thu_flag = True


        for class_element in class_elements:
            button_element = class_element.find_element(user_info.By.TAG_NAME, "button")
            button_text = button_element.text.lower()

            if tue_or_thu_flag and (button_text == "booked" or button_text == "Waitlisted".lower()):
                tuesday_and_thursday_bookings+=1

            if button_text == "booked" or button_text == "Waitlisted".lower():
                already_booked_global += 1
            else:
                pass

    print("---------------------------------------------")
    print(f"Total Booked Classes this session: {booked_global}")
    print(f"Total Waitlisted Classes this session: {waitlisted_global}")
    print(f"Total Already Booked/Waitlisted Classes: {already_booked_global}")
    print(f"Total Tuesday & Thursday 6pm classes: {tuesday_and_thursday_bookings}")

            
        