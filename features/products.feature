Feature: Product Catalog

  Scenario: List all products
    When I visit the "Home Page"
    And I press the "List All" button
    Then I should see "Camera"

  Scenario: Search product by name
    When I enter "Camera" in the name field
    And I press the "Search by Name" button
    Then I should see "Camera"

  Scenario: Search by category
    When I select "Electronics" in the category field
    And I press the "Search by Category" button
    Then I should see "TV"

  Scenario: Search by availability
    When I select "Available" in the availability filter
    And I press the "Search by Availability" button
    Then I should see "Laptop"
