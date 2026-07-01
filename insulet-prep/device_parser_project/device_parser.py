#Device Parser Class
#the purpose of this class is to parse and validate device readings
#The data being read in consist of 
# 1. BG (blood glucose) level (never negative)
# 2. Status - ULOW, LOW, OK, HIGH, UHIGH (U for urgent) 
# 3. Dose - Insulin dosage (never negative)
# 4. Time - Time of the administration 
#

class DeviceParser:
    #constructor
    def __init__(self):
       pass     #no initialization

    def parse_line(self, line):
        #rules for parsed values to be added to the dictionary
        VALIDATION_RULES = {
            "BG" : (int, 0, 400),
            "Status" : (str, ["ULOW", "LOW", "OK", "HIGH", "UHIGH", "ERROR"]),
            "Dose" : (float, 0.0, 20.0),
            "Hour" : (int, 0, 23),
            "Minute" : (int, 0, 59)
        }

       #clean the spaces up
        spaces_removed = line.replace(" ", "")

        #split the line into pairs by comma (eg. 'BG:123' , 'Dose: 123', etc)
        pairs = spaces_removed.split(',')

        #spliting each into a dictionary
        parsed_dict = {}

        for item in pairs:
            try:
                if ':' in item:
                    key, value = item.split(':', 1)

                if key in VALIDATION_RULES:
                    rule = VALIDATION_RULES[key]

                    converted_val = rule[0](value)

                    if rule[0] in (int, float):
                        min_val, max_val = rule[1], rule[2]
                        if not (min_val <= converted_val <= max_val):
                            print(f"ERROR: The value {converted_val} is out of range for {key}")
                            continue

                    elif rule[0] is str:
                        valid_strings = rule[1]
                        if not converted_val in rule[1]:
                            print(f"{converted_val} is not a valid {key}")
                            continue

                    #if everything passes, then add it to the dictionary
                    parsed_dict[key] = converted_val

                else:
                    print(f"{key} is not a valid key name")

            except ValueError:
                print( f"Data formatted incorrectly Value: '{value}'. Skipping line... ")

        
        bg_value = parsed_dict.get("BG", "NOT_FOUND")
        status_value = parsed_dict.get("Status", "NOT_FOUND")
        dose_value = parsed_dict.get("Dose", "NOT_FOUND")
        hour_value = parsed_dict.get("Hour", "NOT_FOUND")
        min_value = parsed_dict.get("Minute", "NOT_FOUND")

        print(f"BG: {bg_value}, Status: {status_value}, Dose: {dose_value}, Time, {hour_value}:{min_value}")
        
                
test = DeviceParser()
test_line = "BG: 101, Status: OK, Dose: 1.1, Hour: 12, Minute: 45"
test_line2 = "BG: , Status: OK, Dose: hello, Hour: 6, Minute: 0"

test.parse_line(test_line)
test.parse_line(test_line2)