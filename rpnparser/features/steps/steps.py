from behave import *
from rpnparser import *
 
@given('a single entry of {number}')
def step_impl(context,number):
    context.rpnparser = rpnparser(number)

@when('the parser validates the single entry')
def step_impl(context):
    context.rpnparser.parser()

@then('the parser string is {answer}')
def step_impl(context,answer):
    context.rpnparser.parsedString = context.rpnparser.ParserString()
    assert (context.rpnparser.parsedString == answer)
    
