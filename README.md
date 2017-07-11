# Release Checklist

[[Github](https://github.com/HashNuke/release-checklist)] [[@HashNuke](https://twitter.com/HashNuke)]

---

## SQL & indexes
* For new queries in the code, run [`explain`](https://www.postgresql.org/docs/current/static/using-explain.html) and add required indexes ([Postgres Query Plan Visualizer](http://tatiyants.com/pev/))
* For queries used for reporting, run [`explain`](https://www.postgresql.org/docs/current/static/using-explain.html) and add required indexes
* Identify and remove [n+1 queries](https://stackoverflow.com/questions/97197/what-is-n1-select-query-issue)
* Use transactions where necessary

## Caching
* Cache whatever you can
* TTLs for cache keys
* Use cache keys with app version as prefix or suffix

## Code
* Comments for any hacks
* Test cases for all code that isn't quickly comprehensible
* Test any code that depends on randomisation
* Respect third-party API limits
* Request-response times

## Data
* Check affected rows/documents
* Handle old values with fallbacks
* [OR] Migrate/translate any existing data to new format

## Micro-services
* Check database fields that are read/written to by different components
* Check all components that interface with anything related
* Watch for errors across components during testing
* Ensure High Availability for any new components

## Load testing
* Add monitoring limits
* Test all auto-scaling rules
* Disable/block write API calls to third-party APIs (comment code OR use firewall)

## User-facing
* Serve all assets via HTTPS (css, javascript, images, fonts, etc)
* Payload for all XHR calls that might be affected
* Support link is available on every webpage
* Contact form works and contact information is available
* Navigation links
* Anything that depends on SMS (Reset password, 2FA, etc)
* Cross-browser tests
* Lookout for weird characters in views and check if unicode is used properly

## Debugging
* Build reports/pages/scripts to be able to debug quickly

## Metrics and data
* System stats
* Queue message counts at regular intervals
* Response codes from third-party API calls
* Track errors

## Communication
* Inform co-workers about any changes to development setup and provide necessary scripts/commands to migrate
* Update README/docs about changes

---

> I found it useful to maintain a checklist when deploying code. This was compiled over a period of time. Feel free to contribute changes on [GitHub](https://github.com/HashNuke/release-checklist)
> 
> -- [@HashNuke](https://twitter.com/HashNuke)
