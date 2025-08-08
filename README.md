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

When I first built the **Dynamic Date-Range Query Builder**, the UI was intended as an MVP. To accelerate prototyping, I provided a clear spec to a large language model (LLM), which generated all the necessary JavaScript, HTML, CSS, and Bootstrap code for:  

- **Date-range picker behavior** (single vs. sliding window)  
- **Preset query templates** (“last 30 days,” “year-to-date,” etc.)  
- **Custom filter panels** (tables, dropdowns, free-text inputs)  

As requirements solidified, I found the LLM-generated frontend fully met our needs. Today, the **entire frontend** remains the LLM output, polished and styled with Bootstrap for consistency.  

Behind the scenes, I:  

1. **Mapped user journeys & wireframes**  
   Defined how the RFP/pricing team would select date ranges, filters, and templates, then sketched UI flows to guide the LLM’s component generation.  

2. **Architected the component hierarchy**  
   Designed a clear tree of containers, pickers, and result tables to enable seamless addition of new features without regressions.  

3. **Authored every backend service**  
   Hand-wrote all database models, API endpoints, and query-builder logic in Python/Flask and T-SQL to power each frontend action.  

This hybrid approach enabled rapid prototyping and hardening into a robust tool the pricing team relies on daily.
