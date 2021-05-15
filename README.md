# GitHub Action Release Calendar #

This is a github actions to check whether release allowed or not based on release calendar and pr labels.


## Inputs ##

* `timezone` (**Required**): Calendar timezone. Ref- [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List)


## Outputs ##

* `release_freeze`: Release allowed or not


## Environment Variables ##

* `GITHUB_TOKEN` (**Required**): Github token

* `PR_NUMBER` (**Required**): Pull request number

* `GITHUB_PR_SHA` (**Required**): Latest commit sha in pull request

* `STATUS_CONTEXT` (**Required**): Context for status check


## Configuration ##

Configure by creating a `.github/release_calendar.yml` file in `default branch`.

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
pr_labels:
  - block-release
```


## Example Usage ##

```yaml
on:
  pull_request:
    types:
      - opened
      - synchronize
      - labeled
      - reopened

  jobs:
    release_calendar:
      runs-on: ubuntu-18.04
      steps:
      - name: Check whether release allowed or not
        id: release
        uses: g2crowd/actions-release-calendar@main
        with:
          timezone: Asia/Kolkata
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PR_NUMBER: ${{ github.event.number }}
          GITHUB_PR_SHA: ${{ github.event.pull_request.head.sha }}
          STATUS_CONTEXT: 'Production Deploy Approved'

      - name: Get the output
        shell: bash
        run: |
          echo ${{ steps.release.outputs.release_freeze }}
```
