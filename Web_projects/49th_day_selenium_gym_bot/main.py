# User created imports
from login_user import *
from class_logging import log_booking_status, booked_global, waitlisted_global
# Login Info
EMAIL_ACCOUNT = "stan.the.man@gmail.com"
ACCOUNT_PASSWORD = "banana"
GYM_URL = "https://appbrewery.github.io/gym/"

# Enum classes
class GymClassType(Enum):
    YOGA = "yoga"
    HIIT = "hiit"
    SPIN = "spin"

def get_next_weekday_date(weekday_name,time_of_day="1800"):
    # Get the current date
    today = time.localtime()
    current_weekday = today.tm_wday  # Monday is 0 and Sunday is 6

    # Map weekday names to their corresponding index
    weekday_map = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thursday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }

    target_weekday = weekday_map.get(weekday_name.lower())
    if target_weekday is None:
        raise ValueError("Invalid weekday name provided.")

    # Calculate days until the next occurrence of the target weekday
    days_ahead = (target_weekday - current_weekday + 7) % 7
    if days_ahead == 0:  # If today is the target day, we want the next occurrence
        days_ahead += 7

    # Calculate the date of the next occurrence of the target weekday
    next_date = time.localtime(time.mktime(today) + days_ahead * 86400)  # Add days in seconds

    class_date = datetime.datetime.strptime(time.strftime("%Y-%m-%d", next_date) + "-" + time_of_day, "%Y-%m-%d-%H%M")

    return class_date

def check_class_timetable(class_type: GymClassType, class_date):
    
    specific_class_id = f"{class_type.value}-{class_date.strftime('%Y-%m-%d')}-{class_date.strftime('%H%M')}"
    
    try:
        class_to_search = WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located((By.ID, f"class-time-{specific_class_id}"))
    )
    except TimeoutException:
        print("Element did not appear in time")
        return False  # or handle the case where the element is not found

    return class_to_search

    
def book_class_specific(class_type: GymClassType, class_date):
    global booked_global, waitlisted_global

    class_to_search = check_class_timetable(class_type, class_date)

    if not class_to_search:
        print(f"{class_type.value.capitalize()} Class on {class_date.strftime('%a,%b %d')} at {class_date.strftime('%H:%M')} not found.")
        return False  # or handle the case where the class is not found
    else:
        # book a class based on the provided class type and date
        class_date_timetable_format = class_date.strftime("%a,%b %d")
        parent_element = class_to_search.find_element(By.XPATH, "..")  # Get the parent element
        grandparent_element = parent_element.find_element(By.XPATH, "..")  # Get the grandparent element
        # find element
        button_element = grandparent_element.find_element(By.TAG_NAME, "button")
        
        if button_element.text.lower() == "booked":
            print(f"Already booked: {class_type.value.capitalize()} Class on {class_date_timetable_format}")
            return False
        elif button_element.text.lower() == "join waitlist":
            waitlisted_global += 1
            print(f"Joined waitlist: {class_type.value.capitalize()} Class on {class_date_timetable_format}")
        elif button_element.text.lower() == "Waitlisted".lower():
            print(f"Already waitlisted: {class_type.value.capitalize()} Class on {class_date_timetable_format}")
            return False
        elif button_element.text.lower() == "Book Class".lower():
            booked_global += 1
            print(f"Booking {class_type.value} class for {class_date}")
        else:
            print(f"Button text is unexpected: {button_element.text}")
            return False

        button_element.click()

def book_each_tue_and_thu():

    global tuesday_and_thursday_bookings
    tue_date = get_next_weekday_date("tuesday")
    thu_date = get_next_weekday_date("thursday")

    for class_type in GymClassType:
        tue_class = book_class_specific(class_type, tue_date)
        thu_class = book_class_specific(class_type, thu_date)

        if tue_class or thu_class:
            tuesday_and_thursday_bookings += 1


login_user()
class_date = get_next_weekday_date("wednesday","1700")
print(f'Print next wednesday date: {class_date}')
book_class_specific(GymClassType.YOGA, class_date)
book_each_tue_and_thu()
log_booking_status()
time.sleep(10000)