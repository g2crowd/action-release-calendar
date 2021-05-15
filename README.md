# GitHub Action Release Calendar #

This is a github actions to check whether release allowed or not based on release calendar.


## Inputs ##

* `timezone` : Calendar timezone
* `calendar_config` : Calendar config file

## Outputs ##

* `release_freeze`: Release allowed or not


## Example Usage ##

```yaml
steps:
- name: Check whether release allowed or not
  id: release
  uses: g2crowd/actions-release-calendar@main
  with:
    timezone: IN

- name: Get the output
  shell: bash
  run: |
    echo ${{ steps.release.outputs.release_freeze }}
```
