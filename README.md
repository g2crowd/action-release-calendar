# GitHub Action Release Calendar #

This is a github actions to check whether release allowed or not based on release calendar.


## Inputs ##

* `timezone` (**Required**): Calendar timezone. Ref- [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List)

## Outputs ##

* `release_freeze`: Release allowed or not

## Configuration ##

Configure by creating a `.github/release_calendar.yml` file:

For example:

```yml
working_days:
  - Monday
  - Tuesday
  - Wednesday
  - Thursday
  - Friday
working_time:
  start: 09.00
  end: 18.00
holidays:
  - 2021/05/16
  - 2021/07/01
  - 2021/09/17
```

## Example Usage ##

```yaml
steps:
- name: Check whether release allowed or not
  id: release
  uses: g2crowd/actions-release-calendar@main
  with:
    timezone: Asia/Kolkata
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

- name: Get the output
  shell: bash
  run: |
    echo ${{ steps.release.outputs.release_freeze }}
```
