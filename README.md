# Frequency Parser


## Project Overview
Developed during my internship at Restaurant Depot, a bulk wholesale food provider.  
This project was built for the **Request For Pricing (RFP)** team, which ensures that RD makes correct payments to vendors for their goods. Each payment is determined by a unique contract.  

For example, the RFP team might need to verify that we paid the correct amount for last week’s beef purchase. The payment amount depends on both the contract terms between RD and the vendor, and the current market rate for beef. A contract might specify that RD will pay the vendor the **average market rate over the past calendar month**. However, real-world contract rules can be far more complex.  

The legacy system for defining date ranges was inflexible and cumbersome, with 115 hard-coded contracts. Adding a new contract required the Data Team to write custom date-range logic for RFP—slowing down operations.  

The goal of this project was to replace the legacy system with an intuitive UI that enables the RFP team to define contract date ranges themselves, without developer support. The UI outputs a structured JSON containing all relevant selections. This is paired with a robust, meticulously unit-tested Python backend, which:  
- Parses the JSON  
- Calculates contract start and end dates  
- Generates the list of days over which to average prices  
- Determines the effective date range when pricing takes effect

## Key Features

- **Visual Contract Builder**  
  - Choose from predefined frequency types (e.g., *average rate over last calendar month*, *first business day of quarter*)  
  - Combine multiple rules into a single, complex contract
  - Snap to beginning/end of week, month, or quarter
  - Further specificy date ranges by stopping/starting at the first/second/etc following/preceding Monday/Tuesday.../Sunday
  - Define different contract rules by weekday for especially complex contracts
  - Pattern filtering to select specific days between the Start and End Dates (e.g., exclude holidays, Tuesdays, or every 4th week)

- **Live JSON Preview**  
  - Automatically generates a clean, structured JSON object for all user selections  
  - Ready for copy-paste, version control, or integration with downstream services  

- **Robust Backend Parsing**  
  - Python backend processes the JSON and computes:  
    1. **Start & End Dates** for each rule  
    2. **Full Date Lists** (e.g., the full list of days to average over between start and end dates) 
    3. **Effective Date Ranges** when pricing rules apply  

- **Comprehensive Unit Testing**  
  - 100% test coverage on core parsing logic  
  - Includes edge cases for leap years, business-day adjustments, and overlapping periods  


## Frontend Architecture & Development

When I first built the **Dynamic Date-Range Query Builder**, the UI was intended as an MVP. To accelerate prototyping, I provided a clear spec to a large language model (LLM), which generated all the necessary `JavaScript`, `HTML`, `CSS`, and `Bootstrap` code for the UI.  

As requirements solidified, I found the LLM-generated frontend fully met our needs. Today, the **entire frontend** remains LLM output, polished and styled with Bootstrap for consistency.  


This hybrid approach enabled rapid prototyping and hardening into a robust tool the pricing team relies on daily.

The JSON parsing backend was written in `Python`. In order to provide feedback on what the selected dates are, I setup `Pyscript` in the front end to run the `Python` backend inside the web browser. 

## Backend

The `Python` class `DateRuleParser` is defined in `RFP_JSON_Parser.py`. It imports a few quarter related time functions from `quarter_helper_functions.py`. `DateRuleParser` takes in a JSON string, and outputs a dictionary containing the date information as mentioned in **Robust Backend Parsing**. It makes extensive use of the `datetime` and `dateutil` libraries.

## Testing

For each of the 115 hard coded contracts in the legacy system, I ported them over to the new JSON format using the UI. I defined these JSON ports in `freq_ID_to_JSON_ports.py`. The file `Unittest_DateRuleParse.py` contains a custom unit testing framework. It takes the parsed Start, End, Effective Start, and Effective End Dates from the JSON ports and compares them agains the ground truth dates from the legacy system. For each rule, it runs and compares the results for each day over the past 10 years to ensure consistently correct functionality. Any days that do not match up are then printed in a `diff` like manner.

For proprietary reasons, `Unittest_DateRuleParse.py` can't be run from this repository because that would mean revealing the legacy system's backend code. However, results of what the unit testing output of `Unittest_DateRuleParse.py` might look like are in `unit_test_diffs.out`.

