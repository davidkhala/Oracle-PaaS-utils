
## Limit: Connect agent
- Attempting to include a third agent instance in the same agent group during installation results in an error.
- Minimum compute resource requirement:
  - 8 GB memory with 4 GB of heap size dedicated for JVM
- Up to 1 concurrent instances of given scheduled integration beside the associated
### Planned outage for Connect agent
- When a new version of the on-premises connectivity agent becomes available, your host is automatically upgraded with the latest version. When Oracle Integration is upgraded, the agent is upgraded within a four hour window. There is no separate alert for agent upgrade. There is no downtime or interruption of service for in-process integrations that use the agent. If there is any failure for in-process integrations using the agent, those integrations may require resubmission.
- For cases in which the Oracle Integration instance is decommissioned or if all requests to the instance from the agent fail with an HTTP error code of 401/404 for a continuous period of 24 hours, the agent terminates the poller threads. This halts all message processing. When the conditions leading to the error have been resolved, the agent must be restarted manually.
