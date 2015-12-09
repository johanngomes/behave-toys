Feature: show the expected page title "Agile development and experience design | ThoughtWorks" on ThoughtWorks page

  Scenario: run a Selenium test
    Given we have Selenium installed
      when we open the TW web page
      then we check if the title is the expected
