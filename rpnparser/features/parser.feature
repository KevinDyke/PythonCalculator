Feature: Reverse Polish parser

  In Order to help with reverse polish notatiom
  As a command line user
  I use a reverse notation parser.
  
  Scenario Outline: simple number
    Given a single entry of <number>
    When the parser validates the single entry
    Then the parser string is <answer>
    
    Examples: Single_Numbers
    | number | answer          |
    | 1      | 1               |
    | 0.1    | 0.1             |
    | 999    | 999             |
    | 0xA    | 0xA             |
    | 0144   | 0144            |
    | Z      | Unknown Number  | 
	
	