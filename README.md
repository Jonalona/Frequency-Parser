# Frequency Parser
Developed under my internship at Restaurant Depot, a bulk wholesale food provider.<br />
This project is built for the RFP team (Request For Pricing). The RFP team is responsible for ensuring that RD is making the correct payments for vendors for their goods. Each payment depends on a unique contract. For instance, the RFP team might need to make sure that we paid the correct amount for last weeks aquirement of beef. Specifically, the purchase amount depends on the contract specifications between RD and the beef vendor, as well as the going rate of beef. A contract might be defined, for the current week, as RD paying the beef vendor the average going rate of beef over the past calendar month. But contract rules can become much more complex than that. The legacy system used to define date ranges is inflexible and cumbersome. There are 115 hard coded contracts. Adding new contracts requires the Data Team to code new contract date range specifications on behalf of RFP. <br />
This project's initiative was to replace the legacy system with an intuitive UI that allows the RFP to directly define date range contracts without support.<br />
The UI creates a formatted JSON that contains all relevant user selections from the UI. is accompanied by a robust, and meticously unit tested backend written in Python. The backend takes in the JSON, parses it, and calculates the specific date range start dates and end dates, a list of all days in between the start and end date to take the average price over, as well as the effective date range which defines when that pricing takes effect.
## Frontend Architecture & Development

When I first built the **Dynamic Date-Range Query Builder**, the UI was intended only as an MVP—and I accelerated prototyping by feeding a clear spec to a large language model (LLM). The LLM generated all the necessary JavaScript, HTML, CSS, and Bootstrap code for:

- **Date-range picker behavior** (single vs. sliding window)  
- **Preset query templates** (“last 30 days,” “year-to-date,” etc.)  
- **Custom filter panels** (tables, dropdowns, free-text inputs)

As the requirements solidified, I discovered that the LLM-generated frontend fully met our needs—so today the **entire front end** remains the LLM output, polished and styled with Bootstrap for a consistent look and feel.

Behind the scenes, I:

1. **Mapped user journeys & wireframes**  
   Defined how the RFP/pricing team would select date ranges, filters, and templates, then sketched UI flows to guide the LLM’s component generation.  
2. **Architected the component hierarchy**  
   Designed a clear tree of containers, pickers, and result tables so new features slot in seamlessly without regressions.  
3. **Authored every backend service**  
   Hand-wrote all database models, API endpoints, and query-builder logic in Python/Flask and T-SQL to power each frontend action.

This hybrid approach let me move from concept to prototype in days, then harden both front and back ends into a robust tool the pricing team can rely on daily.  
