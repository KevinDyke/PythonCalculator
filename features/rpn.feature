Feature: Reverse Polish notation calculator

  In Order to help with basic mathematics
  As a command line user
  I use a calculator.

  Scenario Outline: binary addition
    Given a sum of <two_numbers>
    When the calculator sums the numbers
    Then the result is <sum>
    
    Examples: Numbers_to_sum
    | two_numbers | sum    |
    | 1,0         | 1.0    |
    | 0,1         | 1.0    |
    | 1,2         | 3.0    |
    | 2,1         | 3.0    |
    | 100,300     | 400.0  |
    | 0.01,0.1    | 0.11   | 

 Scenario: binary subtraction
    Given a subtraction
    When I enter the minuend as 3
    And I enter the subtrahend as 2
    Then the difference is 1.0
    
  Scenario: binary multiplication
    Given a multiplication
    When I enter 3
    And I also enter 2
    Then the product is 6.0
 