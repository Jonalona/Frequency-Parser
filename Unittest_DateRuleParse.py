from frequency_parser import get_query_parameters
from RFP_JSON_Parser import DateRuleParser
from datetime import date, datetime, timedelta
from freq_ID_to_JSON_ports import *
import tracemalloc


def do_dates_match(DRP_dict, legacy_dict, date_checking_on, id):
    day_dict = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"]

    if DRP_dict is None:
        raise ValueError("DRP_dict is None")
    if legacy_dict is None:
        raise ValueError("legacy_dict is None")
    failure_log = ""
    passed_flag = True
    if str(DRP_dict["start_date"]) != str(legacy_dict["start_date"]):
        failure_log += "\t\t\t\tStart date:    " + str(DRP_dict["start_date"]) + "(" + day_dict[DRP_dict["start_date"].weekday()] + ")" + " : " + str(legacy_dict["start_date"]) + "(" + day_dict[DateRuleParser._absolute_to_dateObject(legacy_dict["start_date"]).weekday()] + ")" + "\n"
        passed_flag = False
    if str(DRP_dict["end_date"]) != str(legacy_dict["end_date"]):
        failure_log += ("\t\t\t\tEnd date:    " + str(DRP_dict["end_date"]) + "(" + day_dict[DRP_dict["end_date"].weekday()] + ")" + " : " + str(legacy_dict["end_date"]) + "(" + day_dict[DateRuleParser._absolute_to_dateObject(legacy_dict["end_date"]).weekday()] + ")" + "\n")
        passed_flag = False
    if str(DRP_dict["effective_start_date"]) != str(legacy_dict["effective_start_date"]):
        failure_log += ("\t\t\t\tEffective Start date:    " + str(DRP_dict["effective_start_date"]) + "(" + day_dict[DRP_dict["effective_start_date"].weekday()] + ")" + " : " + str(legacy_dict["effective_start_date"])) + "(" + day_dict[DateRuleParser._absolute_to_dateObject(legacy_dict["effective_start_date"]).weekday()] + ")" + "\n"
        passed_flag = False
    if str(DRP_dict["effective_end_date"]) != str(legacy_dict["effective_end_date"]):
        failure_log += ("\t\t\t\tEffective end date:    " + str(DRP_dict["effective_end_date"]) + "(" + day_dict[DRP_dict["effective_end_date"].weekday()] + ")" + " : " + str(legacy_dict["effective_end_date"])) +  "(" + day_dict[DateRuleParser._absolute_to_dateObject(legacy_dict["effective_end_date"]).weekday()] + ")" + "\n"
        passed_flag = False
    if failure_log != "":
        print("\t\t" + str(date_checking_on) + "(" + day_dict[date_checking_on.weekday()] + ")")
        print(failure_log)
    return passed_flag

def side_by_side(DRP_dict, legacy_dict, date_checking_on):
    if DRP_dict is None:
        raise ValueError("DRP_dict is None")
    if legacy_dict is None:
        raise ValueError("legacy_dict is None")
    
    failure_log = "\t\t" +date_checking_on + "\n"
    
    failure_log += "\t\t\t\tStart date:    " + str(DRP_dict["start_date"]) + " : " + str(legacy_dict["start_date"]) + "\n"    
    failure_log += ("\t\t\t\tEnd date:    " + str(DRP_dict["end_date"]) + " : " + str(legacy_dict["end_date"]) + "\n")    
    failure_log += ("\t\t\t\tEffective Start date:    " + str(DRP_dict["effective_start_date"]) + " : " + str(legacy_dict["effective_start_date"])) + "\n"    
    failure_log += ("\t\t\t\tEffective end date:    " + str(DRP_dict["effective_end_date"]) + " : " + str(legacy_dict["effective_end_date"])) +  "\n"   

    print(failure_log)

# date_str = "2023-07-23"
# date_to_check = datetime.strptime(date_str, "%Y-%m-%d").date()
# date_to_check_str = date_to_check.strftime("%Y-%m-%d")
# #augment the JSON so that it's checking relative to $date_to_check
# ported_IDs[1][0]["global-relative-from-today"] = date_to_check_str
# id_Parser = DateRuleParser(ported_IDs[1][0])
# legacy_results = get_query_parameters(str(date_to_check), 1)
# side_by_side(id_Parser.get_results_dict(), legacy_results, date_str)


# date_str = "2023-07-22"
# date_to_check = datetime.strptime(date_str, "%Y-%m-%d").date()
# date_to_check_str = date_to_check.strftime("%Y-%m-%d")
# #augment the JSON so that it's checking relative to $date_to_check
# ported_IDs[1][0]["global-relative-from-today"] = date_to_check_str
# id_Parser = DateRuleParser(ported_IDs[1][0])
# legacy_results = get_query_parameters(str(date_to_check), 1)
# side_by_side(id_Parser.get_results_dict(), legacy_results, date_str)


# date_str = "2023-07-21"
# date_to_check = datetime.strptime(date_str, "%Y-%m-%d").date()
# date_to_check_str = date_to_check.strftime("%Y-%m-%d")
# #augment the JSON so that it's checking relative to $date_to_check
# ported_IDs[1][0]["global-relative-from-today"] = date_to_check_str
# id_Parser = DateRuleParser(ported_IDs[1][0])
# legacy_results = get_query_parameters(str(date_to_check), 1)
# side_by_side(id_Parser.get_results_dict(), legacy_results, date_str)

#tracemalloc.start()
def unit_test_id(id):
    ported_ID = ported_IDs[id]
    perfect_run = True
    id = ported_ID[1]
    print("ID" + str(id))
    for i in range(num_years * 365):
        date_to_check = date.today() - timedelta(days=i)
        date_to_check_str = date_to_check.strftime("%Y-%m-%d")
        #augment the JSON so that it's checking relative to $date_to_check
        ported_ID[0]["global-relative-from-today"] = date_to_check_str

        id_Parser = DateRuleParser(ported_ID[0])
        legacy_results = get_query_parameters(str(date_to_check), id)
        
        if not do_dates_match(id_Parser.get_results_dict(), legacy_results, date_to_check, id):
            perfect_run = False
       
    if perfect_run:
        print(f"\t\tPerfect across the past {num_years} years!!!")

def print_compare_id(id):
    ported_ID = ported_IDs[id]
    perfect_run = True
    id = ported_ID[1]
    print("ID" + str(id))
    for i in range(num_years * 365):
        date_to_check = date.today() - timedelta(days=i)
        date_to_check_str = date_to_check.strftime("%Y-%m-%d")
        #augment the JSON so that it's checking relative to $date_to_check
        ported_ID[0]["global-relative-from-today"] = date_to_check_str

        id_Parser = DateRuleParser(ported_ID[0])
        legacy_results = get_query_parameters(str(date_to_check), id)
        
        side_by_side(id_Parser.get_results_dict(), legacy_results, date_to_check_str)
           
       



       
    
num_years = 10
for id in range(len(ported_IDs)):
    #print_compare_id(id) #prints all 4 dates for both legacy and new implementation
    unit_test_id(id) #only prints when diff fails