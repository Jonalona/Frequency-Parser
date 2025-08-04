# from datetime import datetime
# from dateutil.relativedelta import relativedelta, MO, TU, WE, TH, FR, SA, SU
# import pandas as pd

# #took following two helper functions frm frequency_parser.py
# #Only change was deleting anything not related to start/end date
# def previous_n_quarters(date, n):

#     def previous_quarter(ref):
#         if ref.month < 4:
#             return datetime(ref.year - 1, 12, 31).date()
#         elif ref.month < 7:
#             return datetime(ref.year, 3, 31).date()
#         elif ref.month < 10:
#             return datetime(ref.year, 6, 30).date()

#         return datetime(ref.year, 9, 30).date()

#     # Get previous quarters end date
#     end_quarter_date = previous_quarter(date)

#     # Start quarter date
#     start_quarter_date = pd.date_range(end=end_quarter_date, periods=n, freq="QS")[
#         0
#     ].date()  # end_quarter_date + relativedelta(months=-3 * n, days=1)

#     # Construct dates for return statement
#     start_date = start_quarter_date
#     end_date = end_quarter_date
    

#     return {"start_date":start_date,"end_date":end_date}

# def future_n_quarters(date, n):
#     """
#     Calculates the start and end dates for a period of n future quarters.

#     Args:
#         date (datetime.date): The reference date to start from.
#         n (int): The number of future quarters to span. Must be a positive integer.

#     Returns:
#         dict: A dictionary with "start_date" and "end_date", or None if n is invalid.
#     """
#     # The function requires a positive number of quarters to look forward.
#     if n <= 0:
#         print("Error: n must be a positive integer for future_n_quarters.")
#         return None

#     def get_next_quarter_start(ref):
#         """Helper function to determine the start date of the next calendar quarter."""
#         # If in Q1 (Jan, Feb, Mar), next quarter starts Apr 1.
#         if ref.month < 4:
#             return datetime(ref.year, 4, 1).date()
#         # If in Q2 (Apr, May, Jun), next quarter starts Jul 1.
#         elif ref.month < 7:
#             return datetime(ref.year, 7, 1).date()
#         # If in Q3 (Jul, Sep, Aug), next quarter starts Oct 1.
#         elif ref.month < 10:
#             return datetime(ref.year, 10, 1).date()
#         # If in Q4 (Oct, Nov, Dec), next quarter starts Jan 1 of the next year.
#         return datetime(ref.year + 1, 1, 1).date()

#     # The start date of our range is the beginning of the next quarter.
#     start_date = get_next_quarter_start(date)

#     # The end date is found by generating n quarter-end dates starting from our
#     # calculated start_date and taking the last one.
#     # We use freq='Q' for quarter-end dates.
#     end_date = pd.date_range(start=start_date, periods=n, freq='Q')[n - 1].date()

#     return {"start_date": start_date, "end_date": end_date}




























# def _get_previous_quarter_inteplast(ref_date: date) -> dict:
#     """Calculates the start and end dates of the immediately preceding Inteplast quarter."""
#     if isinstance(ref_date, datetime):
#         ref_date = ref_date.date()

#     month = ref_date.month
#     year = ref_date.year

#     # If date is in Jan (Nov-Jan quarter), previous is Aug-Oct of prior year.
#     if month == 1:
#         start_date = date(year - 1, 8, 1)
#         end_date = date(year - 1, 10, 31)
    
#     # If date is in Feb-Apr (Feb-Apr quarter), previous is Nov-Jan.
#     elif 2 <= month <= 4:
#         start_date = date(year - 1, 11, 1)
#         end_date = date(year, 1, 31)

#     # If date is in May-Jul (May-Jul quarter), previous is Feb-Apr.
#     elif 5 <= month <= 7:
#         start_date = date(year, 2, 1)
#         end_date = date(year, 4, 30)

#     # If date is in Aug-Oct (Aug-Oct quarter), previous is May-Jul.
#     elif 8 <= month <= 10:
#         start_date = date(year, 5, 1)
#         end_date = date(year, 7, 31)
        
#     # If date is in Nov-Dec (Nov-Jan quarter), previous is Aug-Oct.
#     elif 11 <= month <= 12:
#         start_date = date(year, 8, 1)
#         end_date = date(year, 10, 31)

#     return {"start_date": start_date, "end_date": end_date}


# def _get_next_quarter_inteplast(ref_date: date) -> dict:
#     """Calculates the start and end dates of the immediately following Inteplast quarter."""
#     if isinstance(ref_date, datetime):
#         ref_date = ref_date.date()

#     month = ref_date.month
#     year = ref_date.year
    
#     # If date is in Jan (Nov-Jan quarter), next is Feb-Apr.
#     if month == 1:
#         start_date = date(year, 2, 1)
#         end_date = date(year, 4, 30)

#     # If date is in Feb-Apr (Feb-Apr quarter), next is May-Jul.
#     elif 2 <= month <= 4:
#         start_date = date(year, 5, 1)
#         end_date = date(year, 7, 31)

#     # If date is in May-Jul (May-Jul quarter), next is Aug-Oct.
#     elif 5 <= month <= 7:
#         start_date = date(year, 8, 1)
#         end_date = date(year, 10, 31)

#     # If date is in Aug-Oct (Aug-Oct quarter), next is Nov-Jan (crossing year).
#     elif 8 <= month <= 10:
#         start_date = date(year, 11, 1)
#         end_date = date(year + 1, 1, 31)

#     # If date is in Nov-Dec (Nov-Jan quarter), next is Feb-Apr of next year.
#     elif 11 <= month <= 12:
#         start_date = date(year + 1, 2, 1)
#         end_date = date(year + 1, 4, 30)

#     return {"start_date": start_date, "end_date": end_date}


# # --- Public Functions (N Quarters Step) ---

# def get_previous_n_inteplast_quarters(ref_date: date, n: int) -> dict:
#     """
#     Calculates the start and end dates of the Inteplast quarter 'n' periods in the past.

#     Args:
#         ref_date (date): The reference date to calculate from.
#         n (int): The number of quarters to go back. Must be 1 or greater.

#     Returns:
#         dict: A dictionary containing the 'start_date' and 'end_date'
#               of the nth previous fiscal quarter.
#     """
#     if n < 1:
#         raise ValueError("Number of quarters 'n' must be 1 or greater.")
    
#     current_date = ref_date
#     quarter_dates = {}
    
#     for _ in range(n):
#         quarter_dates = _get_previous_quarter_inteplast(current_date)
#         # Use the start date of the found quarter as the reference for the next iteration
#         current_date = quarter_dates['start_date']
        
#     return quarter_dates


# def get_future_n_inteplast_quarters(ref_date: date, n: int) -> dict:
#     """
#     Calculates the start and end dates of the Inteplast quarter 'n' periods in the future.

#     Args:
#         ref_date (date): The reference date to calculate from.
#         n (int): The number of quarters to go forward. Must be 1 or greater.

#     Returns:
#         dict: A dictionary containing the 'start_date' and 'end_date'
#               of the nth future fiscal quarter.
#     """
#     if n < 1:
#         raise ValueError("Number of quarters 'n' must be 1 or greater.")

#     current_date = ref_date
#     quarter_dates = {}

#     for _ in range(n):
#         quarter_dates = _get_next_quarter_inteplast(current_date)
#         # Use the start date of the found quarter as the reference for the next iteration
#         current_date = quarter_dates['start_date']

#     return quarter_dates








# def previous_n_quarters_inteplast(anchor_date, n):
#     if n > 0:
#         return get_previous_n_inteplast_quarters(anchor_date, n)
#     elif n < 0:
#         return get_future_n_inteplast_quarters(anchor_date, n)
#     elif n == 0:
#         next_quarter_start_date = get_future_n_inteplast_quarters(anchor_date,1)["start_date"]
#         return get_previous_n_inteplast_quarters(next_quarter_start_date,1)
# def previous_n_quarters_default(anchor_date, n):
#     if n > 0:
#         return previous_n_quarters(anchor_date, n)
#     elif n < 0:
#         return future_n_quarters(anchor_date, n)
#     elif n == 0:
#         next_quarter_start_date = future_n_quarters(anchor_date,1)["start_date"]
#         return previous_n_quarters(next_quarter_start_date,1)

# previous_n_quarter_func_dict = {"default":previous_n_quarters_default, "inteplast":previous_n_quarters_inteplast}





from datetime import date, datetime
from dateutil.relativedelta import relativedelta

# ===================================================================
# NEW HELPER FUNCTION FOR INPUT VALIDATION
# ===================================================================

def _parse_date_input(input_date) -> date:
    """
    Parses various input types (date, datetime, string) into a date object.
    Raises TypeError or ValueError for invalid inputs.
    """
    if isinstance(input_date, datetime):
        return input_date.date()
    if isinstance(input_date, date):
        return input_date
    if isinstance(input_date, str):
        try:
            # Handles ISO format 'YYYY-MM-DD' and also 'YYYY-MM-DDTHH:MM:SS...'
            return datetime.fromisoformat(input_date).date()
        except ValueError:
            raise ValueError(f"Date string '{input_date}' is not in a valid ISO format (e.g., 'YYYY-MM-DD').")
    
    # If it's none of the above, it's an unsupported type
    raise TypeError(f"Unsupported type for date input: {type(input_date)}. Expected date, datetime, or string.")


# ===================================================================
# UNIFIED HELPER FUNCTIONS (for a single quarter step)
# (No changes needed here, as the input will now be clean)
# ===================================================================

# --- Default Calendar Quarters ---
def _get_previous_quarter_default(ref_date: date) -> dict:
    """Calculates the start and end dates of the immediately preceding standard calendar quarter."""
    
    # 1. Find the first day of the quarter that ref_date is in.
    #    For 2015-07-22, this is 2015-07-01.
    first_day_of_current_quarter = date(ref_date.year, 3 * ((ref_date.month - 1) // 3) + 1, 1)
    
    # 2. The end date of the previous quarter is one day before that.
    #    For 2015-07-01, this is 2015-06-30.
    end_date = first_day_of_current_quarter - relativedelta(days=1)
    
    # 3. The start date of the previous quarter is the first day of its starting month.
    #    We can find this by taking the end_date, going to the first day of its month,
    #    and then subtracting two months.
    #    - end_date = 2015-06-30
    #    - First day of its month = 2015-06-01
    #    - Subtract 2 months = 2015-04-01
    start_date = end_date.replace(day=1) - relativedelta(months=2)
    
    return {"start_date": start_date, "end_date": end_date}

def _get_next_quarter_default(ref_date: date) -> dict:
    first_day_of_current_quarter = date(ref_date.year, 3 * ((ref_date.month - 1) // 3) + 1, 1)
    start_date = first_day_of_current_quarter + relativedelta(months=3)
    end_date = start_date + relativedelta(months=3, days=-1)
    return {"start_date": start_date, "end_date": end_date}

# --- Inteplast Fiscal Quarters ---
def _get_previous_quarter_inteplast(ref_date: date) -> dict:
    month, year = ref_date.month, ref_date.year # This will now work
    if month == 1: return {"start_date": date(year - 1, 8, 1), "end_date": date(year - 1, 10, 31)}
    elif 2 <= month <= 4: return {"start_date": date(year - 1, 11, 1), "end_date": date(year, 1, 31)}
    elif 5 <= month <= 7: return {"start_date": date(year, 2, 1), "end_date": date(year, 4, 30)}
    elif 8 <= month <= 10: return {"start_date": date(year, 5, 1), "end_date": date(year, 7, 31)}
    elif 11 <= month <= 12: return {"start_date": date(year, 8, 1), "end_date": date(year, 10, 31)}

def _get_next_quarter_inteplast(ref_date: date) -> dict:
    month, year = ref_date.month, ref_date.year # This will now work
    if month == 1: return {"start_date": date(year, 2, 1), "end_date": date(year, 4, 30)}
    elif 2 <= month <= 4: return {"start_date": date(year, 5, 1), "end_date": date(year, 7, 31)}
    elif 5 <= month <= 7: return {"start_date": date(year, 8, 1), "end_date": date(year, 10, 31)}
    elif 8 <= month <= 10: return {"start_date": date(year, 11, 1), "end_date": date(year + 1, 1, 31)}
    elif 11 <= month <= 12: return {"start_date": date(year + 1, 2, 1), "end_date": date(year + 1, 4, 30)}

# ===================================================================
# UNIFIED N-QUARTER FUNCTIONS
# ===================================================================

def _get_nth_quarter_generic(ref_date: date, n: int, step_func: callable) -> dict:
    if n < 1: raise ValueError("Number of quarters 'n' must be 1 or greater for stepping.")
    current_date = ref_date
    quarter_dates = {}
    for _ in range(n):
        quarter_dates = step_func(current_date)
        current_date = quarter_dates['start_date']
    return quarter_dates

# ===================================================================
# DISPATCHER FUNCTIONS (The public interface with validation)
# ===================================================================

def get_nth_quarter_default(anchor_date, n: int) -> dict:
    """
    Gets the start/end of the Nth calendar quarter relative to an anchor date.
    """
    # *** ADDED VALIDATION STEP ***
    processed_date = _parse_date_input(anchor_date)

    if n > 0:
        return _get_nth_quarter_generic(processed_date, n, _get_previous_quarter_default)
    elif n < 0:
        return _get_nth_quarter_generic(processed_date, abs(n), _get_next_quarter_default)
    elif n == 0:
        next_q = _get_next_quarter_default(processed_date)
        return _get_previous_quarter_default(next_q['start_date'])

def get_nth_quarter_inteplast(anchor_date, n: int) -> dict:
    """
    Gets the start/end of the Nth Inteplast fiscal quarter relative to an anchor date.
    """
    # *** ADDED VALIDATION STEP ***
    processed_date = _parse_date_input(anchor_date)
    
    if n > 0:
        return _get_nth_quarter_generic(processed_date, n, _get_previous_quarter_inteplast)
    elif n < 0:
        return _get_nth_quarter_generic(processed_date, abs(n), _get_next_quarter_inteplast)
    elif n == 0:
        next_q = _get_next_quarter_inteplast(processed_date)
        return _get_previous_quarter_inteplast(next_q['start_date'])

# ===================================================================
# FINAL EXPORT DICTIONARY
# ===================================================================

get_nth_quarter_func_dict = {
    "default": get_nth_quarter_default, 
    "inteplast": get_nth_quarter_inteplast
}