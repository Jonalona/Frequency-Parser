import json
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import holidays
from dateutil.rrule import rrule, DAILY, WEEKLY, MONTHLY, MO, TU, WE, TH, FR, SA, SU
import pandas as pd
from quarter_helper_functions import get_nth_quarter_func_dict


us_holidays = holidays.US()
# Open and read the JSON file
with open('test.json', 'r') as file:
    data = json.load(file)





class DateRuleParser:
    us_holidays = holidays.US()

    def __init__(self, rule_dict):
        """
        Initializes the DateRuleParser with a dictionary containing the date rule.
        """
        if not isinstance(rule_dict, dict):
            raise TypeError("rule_dict must be a dictionary.")
        
        self.rule_dict = rule_dict
        self.global_anchor = self.parse_global_relative_anchor() #today unless explicitly otherwise

        self._assign_day_specific_ruleDict() #will updates self.rule_dict if day specific ruling is enabled

        self.start_date = None
        self.end_date = None
        self.valid_intra_start_end_dates = None
        self.effective_start_date = None
        self.effective_end_date = None
        self.generate_dates()   

    def _assign_day_specific_ruleDict(self):
        rule_dict = self.rule_dict
        #if there is no group-1 then day specific rules are not enabled
        if rule_dict.get("group-1") is None:
            return
    
        day_dict = {"Monday":0,"Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4,"Saturday":5,"Sunday":6}
        weekday = self.global_anchor.weekday()

        for i in range(7):
            group_i_rule = rule_dict.get(f"group-{i+1}")
            if group_i_rule is not None:
                rule_specific_days = group_i_rule.get("rule_specific_days")
    
                if rule_specific_days is None:
                    raise KeyError(f"Day specific rules are enabled yet group-{i+1} doesn't have rule_specific_days key")

                for day in rule_specific_days:
                    #if self.global_anchor's weekday is in group-i's rule_specific_days then we use that specific rule for the rest of the program
                    if day_dict[day] == weekday:
                        self.rule_dict = group_i_rule
                        return
            #this break isn't neccessary for control flow, but should save a couple zeptoseconds!
            else:
                break
        raise AssertionError("Day specific rules are enabled yet the global_anchor day is not in any")
        

    def parse_global_relative_anchor(self):
        glob_rel_from_td = self.rule_dict.get("global-relative-from-today")
        if glob_rel_from_td is not None:
            if glob_rel_from_td == "today":
                return date.today()
            else:
                return DateRuleParser._absolute_to_dateObject(glob_rel_from_td)
        else:
            return date.today()
        
    def generate_dates(self):
        self._calc_start_date()
        self._calc_end_date()
        self._calc_valid_intra_start_end_dates()

        if self.start_date is None:
            raise ValueError("start_date was calculated to be None")
        if self.end_date is None:
            raise ValueError("end_date was calculated to be None")

        
        #effective doesn't exist for older verions of this class
        #going forward, all JSONs should have an effective field
        if self.rule_dict.get("effective") is not None:
            self._calc_effective_start_date()
            self._calc_effective_end_date()

    def __str__(self):
        # Check if dates have been calculated; provide a default message if not.
        if self.start_date is None or self.end_date is None:
            return "DateRuleParser (dates have not been generated yet)"

        # Use f-strings for cleaner formatting. No .date() call is needed.
        message = f"Start Date: {self.start_date}\n"
        message += f"End Date: {self.end_date}\n"

        # Safely check if filtered_dates has been populated before trying to print it.
        if self.valid_intra_start_end_dates is not None:
            message += f"\nValid Dates between Start and End ({len(self.valid_intra_start_end_dates)}):"
            # Join the first few dates for a clean preview
            #date_preview = "\n  ".join(map(str, self.valid_intra_start_end_dates[:20]))
            date_preview = "\n  ".join(map(str, self.valid_intra_start_end_dates[:]))
            message += f"\n  {date_preview}"
            # if len(self.valid_intra_start_end_dates) > 20:
            #     message += "\n  ..."
        
        message += "\n\n"
        message += f"Effective Start Date: {self.effective_start_date}\n"
        message += f"Effective End Date: {self.effective_end_date}\n"
        return message

    def get_results_dict(self):
        return {"start_date":self.start_date, "end_date": self.end_date, "valid days inbetween start and end":self.valid_intra_start_end_dates,
                "effective_start_date":self.effective_start_date, "effective_end_date":self.effective_end_date}

    def _calc_start_date(self):
        start_date_rule = self.rule_dict["start_date"]
        #anchor_date = date.today() if start_date_rule.get("start_date") == "today" else DateRuleParser._absolute_to_dateObject(start_date_rule["start_date"])
        anchor_date = self.global_anchor #used to be date.today
        self.start_date = self._calc_date(start_date_rule, anchor_date=anchor_date)
        return self.start_date
    
    def _calc_end_date(self):
        end_date_rule = self.rule_dict["end_date"]
        anchor_date = None
    
        if end_date_rule["type"] == "relative_to_start":
            anchor_date = self.start_date
        else:
            anchor_date = self.global_anchor

        self.end_date = self._calc_date(end_date_rule, anchor_date=anchor_date)
        return self.end_date
    
    def _calc_effective_start_date(self):
        effective_start_date_rule = self.rule_dict["effective"]["start_date"]
        anchor_date = self.global_anchor #used to be date.today()
        if effective_start_date_rule.get("relative-minor") is not None:
            directions_from_end_date = ["after-end-date","before-end-date"]
            directions_from_GRD = ["before-global-relative-date","after-global-relative-date"]
            direction = effective_start_date_rule.get("relative-minor").get("direction")
            
            if direction is None:
                raise ValueError("Effective Start Date is missing 'direction' field")
            
            #set anchor_date depending on what the direction is relative to
            if direction in directions_from_end_date:
                anchor_date = self.end_date
            elif direction in directions_from_GRD:
                anchor_date = self.global_anchor
            if anchor_date is None:
                raise ValueError("effective_start_date's anchor_date is none when it shoudln't be")
            
        else:
            # anchor_date = self.end_date if effective_start_date_rule.get("start_date") == "end_date" else DateRuleParser._absolute_to_dateObject(effective_start_date_rule["start_date"])
            pass
        if anchor_date is None:
            raise ValueError("anchor_date within _calc_effective_start_date must not be None")
        self.effective_start_date = self._calc_date(effective_start_date_rule, anchor_date=anchor_date)
        return self.effective_start_date
    
    def _calc_effective_end_date(self):
        effective_end_date_rule = self.rule_dict["effective"]["end_date"]
        # anchor_date = self.end_date if effective_end_date_rule.get("start_date") =="end_date" else DateRuleParser._absolute_to_dateObject(effective_end_date_rule["start_date"])
        # #effective end date has special direction option "After Effective Start Date"
        # if effective_end_date_rule["relative-minor"].get("direction") == "after-effective-start-date":
        #     anchor_date = self.effective_start_date
        anchor_date = None
        if effective_end_date_rule.get("relative-minor") is not None:
            directions_from_end_date = ["after-end-date","before-end-date"]
            directions_from_GRD = ["before-global-relative-date","after-global-relative-date"]
            direction = effective_end_date_rule.get("relative-minor").get("direction")
            
            if direction is None:
                raise ValueError("Effective End Date is missing 'direction' field")
            
            #set anchor_date depending on what the direction is relative to
            if direction == "after-effective-start-date":
                anchor_date = self.effective_start_date
            elif direction in directions_from_end_date:
                anchor_date = self.end_date
            elif direction in directions_from_GRD:
                anchor_date = self.global_anchor
        self.effective_end_date = self._calc_date(effective_end_date_rule, anchor_date=anchor_date)


        #once effective_end_date has been initially calculated we extend to following day if neccessary
        extend_from = effective_end_date_rule.get("extend_from") 
        extend_to = effective_end_date_rule.get("extend_to") 
        if extend_from is not None and extend_to is not None:
            day_dict = {"Monday":0,"Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4,"Saturday":5,"Sunday":6}
            #check the current effective_end_date is the same day of the week as extend_from
            #if it is, we extend effective_end_date to the next day of teh week as specificied by extend_to
            if self.effective_end_date.weekday() == day_dict[extend_from]:
                days_ahead = (day_dict[extend_to] - self.effective_end_date.weekday() + 7) % 7
                days_ahead = days_ahead or 7 #if days_ahead==0 then set to 7 to skip 1 whole week
                self.effective_end_date += timedelta(days=days_ahead)
        return self.effective_end_date

    def _calc_valid_intra_start_end_dates(self):
        #calculate start/end dates if they haven't already been
        if self.start_date is None:
            self._calc_start_date()
        if self.end_date is None:
            self._calc_end_date()

        start_date = self.start_date
        end_date = self.end_date
        pattern_filter_dict = self.rule_dict.get("pattern_filter") #pattern_filter may not be a key
        day_filter_arrDict = self.rule_dict["day_filter"] #day_filter will be a key

        self.valid_intra_start_end_dates = self._calc_valid_dates_list(start_date, end_date, pattern_filter_dict, day_filter_arrDict)
        
        return self.valid_intra_start_end_dates

    #TODO: calc_valid_effective_intra_start_end_dates using above as reference
        
    @staticmethod
    def _calc_valid_dates_list(start_date, end_date, pattern_filter_dict, day_filter_arrDict):
        if start_date > end_date:
            raise ValueError("start_date must be less than or equal to end_date")

        intra_start_end_dates = None
        #"pattern filter" field only exists if it's not Null 
        if pattern_filter_dict is not None:
            intra_start_end_dates = DateRuleParser._pattern_filtering(pattern_filter_dict, start_date, end_date)
        else:
            #inclusive
            #ensure rrule, which yields datetimes, is converted to date objects
            intra_start_end_dates = [dt.date() for dt in rrule(DAILY, dtstart=start_date, until=end_date)]
        
        for item in day_filter_arrDict:
            if item["type"] == "inclusive_days_of_week":
                intra_start_end_dates = DateRuleParser._weekday_filtering(item["days"], intra_start_end_dates)
            if item["type"] == "exclude_holidays":
                intra_start_end_dates = [d for d in intra_start_end_dates if d not in DateRuleParser.us_holidays]
            if item["type"] == "days_between":
                #inclusive
                lower_bound = int(item["lower_bound"])
                upper_bound = int(item["upper_bound"])
                intra_start_end_dates = [d for d in intra_start_end_dates if (d.day >= lower_bound and d.day <= upper_bound)]

            #TODO: Exclude Holidays and Days Between
        
        return intra_start_end_dates
        

    
    @staticmethod
    def _calc_date(dateRule_dict, anchor_date):
        if not isinstance(dateRule_dict, dict):
            raise TypeError("dateRule_dict must be a dictionary.") 
        if anchor_date is None:
            raise TypeError("anchor_date must not be None type in _calc_date") 
        
        if dateRule_dict["type"] == "anchored":
            return DateRuleParser._anchored_to_dateObject(dateRule_dict["anchored"], anchor_date=anchor_date)
        elif dateRule_dict["type"] == "relative":
            return DateRuleParser._relative_to_dateObject(dateRule_dict, anchor_date=anchor_date)
        elif dateRule_dict["type"] == "absolute":
            return DateRuleParser._absolute_to_dateObject(dateRule_dict["value"])
        elif dateRule_dict["type"] == "fiscal":
            pass #TODO: add fiscal
        elif dateRule_dict["type"] == "relative_to_start":
            return DateRuleParser._relativeToStartDate_to_dateObject(relativeToStartDate_dict=dateRule_dict,start_date=anchor_date)
        else:
            raise Exception("dateRule_dict didn't have a valid " \
            "date type (anchored, relative, absolute, or fiscal)")
        
    #string_date should be in YYYY-MM-DD format
    @staticmethod
    def _absolute_to_dateObject(string_date):
        format_string = "%Y-%m-%d"
        # Convert the string to a datetime, then date object
        dateObject = datetime.strptime(string_date, format_string).date()
        return dateObject


    
    #returns a date object offset from anchor_date (defaults to today's date) with parameters from relative_dict
    @staticmethod
    def _relativeMinor_to_dateObject(relative_dict, anchor_date):
        if relative_dict.get("unit") is None:
            raise ValueError("relative_dict in _relativeMinor_to_dateObject has no 'unit' key")
        if relative_dict.get("value") is None:
            raise ValueError("relative_dict in _relativeMinor_to_dateObject has no 'value' key")
        if relative_dict.get("direction") is None:
            raise ValueError("relative_dict in _relativeMinor_to_dateObject has no 'direction' key")
        if anchor_date is None:
            raise ValueError("anchor_date in _relativeMinor_to_dateObject can not be None")
        
        
        relative_d_params = {relative_dict["unit"].lower() : relative_dict["value"]}

        #quarter isn't a standard time unit defined in python's date library
        #plus, we automatically snap to start or end of quarter
        quarter_value = relative_d_params.get("quarter") or relative_d_params.get("quarters")
        if quarter_value is not None:
            quarter_snap = relative_dict.get("snap_to")
            if quarter_snap is None:
                raise ValueError("Date unit is 'quarter' yet does not have required 'snap-to' attribute")
            #specifically for inteplast which has special quarter definition
            #as of right now, quarter_modifier must be inserted manually into JSON; not UI option
            quarter_modifier = relative_dict.get("quarter_modifier") or "default" #quarter_modifier key-value may not exist
            
            return DateRuleParser._quarter_relativeMinor_helper(quarter_value, quarter_snap, anchor_date, relative_dict["direction"], quarter_modifier=quarter_modifier)

        relative_delta = relativedelta(**relative_d_params)
        relative_date = None
        #spent last 2 hours chasing bug becuase forgot to decapitalize 2 letters
        backward_direction = ["AGO","Before End Date", "before-end-date", "before-global-relative-date"]
        forward_direction = ["FROM NOW","After End Date","after-end-date", "after-effective-start-date", "after-global-relative-date"]
        #If DAYS then need to check for skip weekend option. No other unit has skip_weekends option
        if relative_dict["unit"] == "DAYS" and relative_dict.get("skip_weekends") is True:
                current_date = anchor_date
                nonweekend_days_skipped = 0
                direction = -1 if relative_dict["direction"] in backward_direction else 1
                while nonweekend_days_skipped < relative_dict["value"]:
                    current_date += timedelta(days=direction)
                    if current_date.weekday() < 5:  # Monday=0, Sunday=6
                        nonweekend_days_skipped += 1
                relative_date = current_date
        else:
            if relative_dict["direction"] in backward_direction:
                relative_date = anchor_date - relative_delta
            elif relative_dict["direction"] in forward_direction:
                relative_date = anchor_date + relative_delta
        if relative_date is None:
            raise ValueError("relative_date in _relativeMinor_to_dateObject should not still be None")
        #optional snap to button will snap to the start or end of what ever time unit relative_date is in up to this point
        #ex) if, up to this point, relative_date is Thursday, July 3rd 2025 and unit="WEEK" then snap_to=="beginning" will alter
        #relative_date to the start of that week (ie set relative_date to Monday, June 30th 2025)
        snap_to = relative_dict.get("snap_to")
        if snap_to is not None:
            if relative_dict["unit"] == "MONTHS":
                #if snap_to == "beginning" then just move to first day of the month
                relative_date = relative_date.replace(day=1)
                if snap_to == "end":
                    #if snapping to end, it's the first of the next month minus 1 day
                    relative_date = relative_date + relativedelta(months=1, days=-1)

            if relative_dict["unit"] == "WEEKS":
                days_from_monday = relative_date.weekday()
                if snap_to == "beginning":
                    relative_date = relative_date - timedelta(days=days_from_monday)
                elif snap_to == "end":
                    days_until_sunday = 6 - days_from_monday
                    relative_date = relative_date + timedelta(days=days_until_sunday)

        return relative_date

    #extra
    @staticmethod
    def _quarter_relativeMinor_helper(quarter_value, quarter_snap, anchor_date, direction, quarter_modifier="default"):
        if direction in ["FROM NOW","After End Date","after-end-date", "after-effective-start-date", "after-global-relative-date"]:
            quarter_value *= -1
        """
        Gets the start/end of the Nth calendar quarter relative to an anchor date.
        n > 0: Nth quarter in the past.
        n < 0: Nth quarter in the future.
        n = 0: The current quarter.
        """
        previous_n_quarter_func = get_nth_quarter_func_dict.get(quarter_modifier)
        if previous_n_quarter_func is None:
            raise ValueError(f"The value of the quarter_modifier field is '{quarter_modifier}' which is not valid. Try 'standard' (default) or 'inteplast'")
        
        q_start_end_dict = previous_n_quarter_func(anchor_date, quarter_value)

        
        if quarter_snap == "beginning":
            return q_start_end_dict["start_date"]
        elif quarter_snap == "end":
            return q_start_end_dict["end_date"]
        else:
            raise ValueError(f"quarter_snap value is {quarter_snap}. Must be 'beginning' or 'end'")

    #the final anchored_date will always be on or anchor_date
        #For instance, anchored_dict = {"Position":"SECOND","day":"Friday","in":{"type":"relative","value":3,"unit":"MONTHS","direction":"FROM NOW"}}
        #anchored_date will be the second Friday AFTER 3 months from now. If 3 months from now was a Friday, the final anchored_date would be the following
        #Friday because that first day 3 months from now would be count as the first Friday.
    @staticmethod
    def _refine_by_weekday(refine_by_weekday_dict, anchor_date):
        day_dict = {"Monday":0,"Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4,"Saturday":5,"Sunday":6}

        anchored_date = None

        ordinal_dict = {"FIRST" : 0, "SECOND" : 1, "THIRD" : 2, "FOURTH" : 3, "FIFTH" : 4, "SIXTH" : 5}
        if refine_by_weekday_dict["position"] in ordinal_dict:
            desired_day = day_dict[refine_by_weekday_dict["weekday"]]
            relative_anchor_date_DOW = anchor_date.weekday()
            
            days_to_add = None
            if refine_by_weekday_dict["direction"] == "FOLLOWING": 
                days_to_add = ((desired_day - relative_anchor_date_DOW) % 7) + 7 * ordinal_dict[refine_by_weekday_dict["position"]]
            elif refine_by_weekday_dict["direction"] == "PRECEDING": 
                days_to_add = -((relative_anchor_date_DOW - desired_day) % 7) - 7 * ordinal_dict[refine_by_weekday_dict["position"]]
            anchored_date = anchor_date + timedelta(days=days_to_add)

        return anchored_date
    
    @staticmethod
    def _refine_by_days(refine_by_days_dict, anchor_date):
        days_to_add = None
        if refine_by_days_dict["direction"] == "PRECEDING":
            days_to_add = -1 * refine_by_days_dict["value"]
        elif refine_by_days_dict["direction"] == "FOLLOWING":
            days_to_add = refine_by_days_dict["value"]
        return anchor_date + timedelta(days=days_to_add)
    
    @staticmethod
    def _relative_to_dateObject(relative_dict, anchor_date):
        if anchor_date is None: 
            raise ValueError("anchor_date must not be None in _relative_to_dateObject")
        if relative_dict.get("relative-minor") is None:
            raise ValueError("effective_end_date is missing relative-minor key when it should have one")
        relative_offset_date = DateRuleParser._relativeMinor_to_dateObject(relative_dict=relative_dict["relative-minor"], anchor_date=anchor_date)
        if(relative_offset_date is None):
            raise ValueError("relative_offset_date must not be None in _relative_to_dateObject()")
        
        final_date = relative_offset_date
        if relative_dict.get("refine-by-weekday") is not None:
            final_date = DateRuleParser._refine_by_weekday(relative_dict["refine-by-weekday"], anchor_date=relative_offset_date)
        if relative_dict.get("refine-by-days") is not None:
            final_date = DateRuleParser._refine_by_days(relative_dict["refine-by-days"], anchor_date=relative_offset_date)
        
        return final_date 

    
    @staticmethod
    def _relativeToStartDate_to_dateObject(relativeToStartDate_dict, start_date):
        relativeToStartDate_dict["direction"] = "FROM NOW"
        unrefined_date = DateRuleParser._relativeMinor_to_dateObject(relativeToStartDate_dict, anchor_date=start_date)
        if relativeToStartDate_dict.get("refine-by-weekday") is not None:
            refined_date = DateRuleParser._refine_by_weekday(relativeToStartDate_dict["refine-by-weekday"], anchor_date=unrefined_date)
            return refined_date
        if relativeToStartDate_dict.get("refine-by-days") is not None:
            refined_date = DateRuleParser._refine_by_days(relativeToStartDate_dict["refine-by-days"], anchor_date=unrefined_date)
            return refined_date
        
        return unrefined_date 




    #any weekdays that are not in inclusive_dayname_list are removed from the set of all_days_list
    @staticmethod
    def _weekday_filtering(inclusive_dayname_list, all_days_list):
        #faster if it's a set
        inclusive_dayname_set = set(inclusive_dayname_list)
        filtered_by_dayname = [d for d in all_days_list if d.strftime('%A') in inclusive_dayname_set]
        return filtered_by_dayname
    
    @staticmethod
    def _pattern_filtering(pattern_filter_dict, start_date, end_date):
        freq_dict = {"DAY" : DAILY, "WEEK" : WEEKLY, "MONTH" : MONTHLY}
        patternUnit_start_dates = list(rrule(
            freq=freq_dict[pattern_filter_dict["unit"]],
            interval=pattern_filter_dict["interval"],
            dtstart=start_date,
            until=end_date
        ))

        # patternUnit_start_dates contains the first day of each pattern unit (e.g., week, month)
        # If you want all days in each pattern unit, expand each period into its days
        all_dates = []
        for period_start in patternUnit_start_dates:
            if pattern_filter_dict["unit"] == "WEEK":
                for i in range(7):
                    day = period_start + timedelta(days=i)
                    if day.date() <= end_date:
                        all_dates.append(day)
            elif pattern_filter_dict["unit"] == "MONTH":
                # Get all days in the month
                next_month = (period_start + relativedelta(months=1))
                day = period_start
                while day < next_month and day.date() <= end_date:
                    all_dates.append(day)
                    day += timedelta(days=1)
            #this is overkill and doesn't actually accomplish anything. Good for safety I guess
            elif pattern_filter_dict["unit"] == "DAY": 
                if period_start.date() <= end_date:
                    all_dates.append(period_start)

        all_dates = [d.date() for d in all_dates] 
        return all_dates
    




# parser = DateRuleParser(test_dict)
# print(parser)