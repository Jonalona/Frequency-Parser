# Frequency Parser

## Frontend Architecture & Development

When I first built the **Dynamic Date-Range Query Builder**, the UI was intended only as an MVP—and I accelerated prototyping by feeding a clear spec to a large language model (LLM). The LLM generated all the necessary JavaScript, HTML, CSS, and Bootstrap code for:

- **Date-range picker behavior** (single vs. sliding window)  
- **Preset query templates** (“last 30 days,” “year-to-date,” etc.)  
- **Custom filter panels** (tables, dropdowns, free-text inputs)

As the requirements solidified, I discovered that the LLM-generated frontend fully met our needs—so today the **entire front end** remains the original LLM output, polished and styled with Bootstrap for a consistent look and feel.

Behind the scenes, I also:

1. **Mapped user journeys & wireframes**  
   Defined how the RFP/pricing team would select date ranges, filters, and templates, then sketched UI flows to guide the LLM’s component generation.  
2. **Architected the component hierarchy**  
   Designed a clear tree of containers, pickers, and result tables so new features slot in seamlessly without regressions.  
3. **Authored every backend service**  
   Hand-wrote all database models, API endpoints, and query-builder logic in Python/Flask and T-SQL to power each frontend action.

This hybrid approach let me move from concept to prototype in days, then harden both front and back ends into a robust tool the pricing team relies on daily.  
