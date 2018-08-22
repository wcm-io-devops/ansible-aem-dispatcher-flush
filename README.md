# wcm_io_devops.aem_dispatcher_flush

This role flushes one or multiple AEM dispatcher caches by using `curl`.

## Requirements

This role requires Ansible 2.0 or higher and was tested with AEM dispatcher 4.2+

## Role Variables

Available variables are listed below, along with their default values:

        aem_dispatcher_flush_targets: []

List of targets to be flushed.

        aem_dispatcher_flush_noproxy: false

Controls if the `--noproxy` `curl` will be added for the flush targets.

        aem_dispatcher_flush_cq_action: Delete

The CQ-Action to use.

        aem_dispatcher_flush_cq_handle: /

The CQ-Handle to use.

        # aem_dispatcher_flush_resolve_ip: 127.0.0.1

Overrides the dns resolving by using the `--resolve` curl argument for flush operations.

        aem_dispatcher_flush_location: /dispatcher/invalidate.cache

The location of dispatcher invalidate cache.

        aem_dispatcher_flush_insecure: false

Allows insecure HTTPS connections.

    aem_dispatcher_flush_connect_timeout: 10

Maximum time allowed for the connection to the dispatcher in seconds.

    aem_dispatcher_flush_timeout: 60

Maximum time allowed for the dispatcher flush operation in seconds.

## Dependencies

This role has no dependencies.

## Example Playbook (defaults)

Flushes the dispatcher running on https://aem-author with default values.

```yaml
- hosts: aem-author
  vars:
    aem_dispatcher_flush_targets:
      - "https://aem-author"
  roles:
    - aem-dispatcher-flush 
```

This playbook will result in the following curl command:

        curl -X POST -H \"CQ-Action: Delete\" -H \"CQ-Handle: /\" --write-out %{http_code} --output /dev/null --silent --head --fail https://aem-author/dispatcher/invalidate.cache

## Example Playbook (custom)

Flushes the dispatcher running on https://aem-author with custom values:
* No proxy for https://aem-author
* Allow insecure connection
* resolve aem-author to 127.0.0.1 (localhost)

```yaml
- hosts: aem-author
  vars:
    aem_dispatcher_flush_targets:
      - "https://aem-author"
    aem_dispatcher_flush_noproxy: true
    aem_dispatcher_flush_insecure: true
    aem_dispatcher_flush_resolve: true
    aem_dispatcher_flush_resolve_ip: 127.0.0.1
  roles:
    - wcm_io_devops.aem_dispatcher_flush
```

This playbook will result in the following curl command:

        curl --resolve \"aem-author:443:127.0.0.1\" --noproxy aem-author -k -X POST -H \"CQ-Action: Delete\" -H \"CQ-Handle: /\" --write-out %{http_code} --output /dev/null --silent --head --fail https://aem-author/dispatcher/invalidate.cache

## License

Apache 2.0
