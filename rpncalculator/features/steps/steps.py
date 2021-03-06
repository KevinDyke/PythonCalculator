from behave import *
from rpncalculator import *

@given('a sum of {two_numbers}')
def step_impl(context,two_numbers):
    context.rpncalculator = rpncalculator()
    context.rpncalculator.numbers = two_numbers.split(',')
    context.rpncalculator.number1 = float(context.rpncalculator.numbers[0])
    context.rpncalculator.number2 = float(context.rpncalculator.numbers[1])
    context.rpncalculator.enterValue(context.rpncalculator.number1)
    context.rpncalculator.enterValue(context.rpncalculator.number2)
    
@when('the calculator sums the numbers')
def step_impl(context):
    context.rpncalculator.sum()
    
@then('the result is {sum}')
def step_impl(context,sum):
    context.sumresult = context.rpncalculator.getResult()
    assert (context.sumresult == str(sum))
 
@given('a subtraction')
def step_impl(context):
    context.rpncalculator = rpncalculator()
    
@when('I enter the minuend as {value}')
def step_impl(context,value):
    context.rpncalculator.enterValue(value)

@when('I enter the subtrahend as {value}')
def step_impl(context,value):
    context.rpncalculator.enterValue(value) 

@then('the difference is {result}')
def step_impl(context,result):
    context.rpncalculator.difference()
    context.differenceResult = context.rpncalculator.getResult()
    assert (context.differenceResult == result)

@given('a multiplication')
def step_impl(context):
    context.rpncalculator = rpncalculator()

@when('I enter the multiplicand as {value}')
def step_impl(context,value):
    context.rpncalculator.enterValue(value)
    
@when('I enter the multiplier as {value}')
def step_impl(context,value):
    context.rpncalculator.enterValue(value)
    
@then('the product is {result}')
def step_impl(context,result):
    context.rpncalculator.multiply()
    context.productResult = context.rpncalculator.getResult()
    assert (context.productResult == result) 
    
@given('a pair of {pair_of_numbers}')
def step_impl(context,pair_of_numbers):
    context.rpncalculator = rpncalculator()
    context.rpncalculator.numbers = pair_of_numbers.split(',')
    context.rpncalculator.number1 = float(context.rpncalculator.numbers[0])
    context.rpncalculator.number2 = float(context.rpncalculator.numbers[1])
    context.rpncalculator.enterValue(context.rpncalculator.number1)
    context.rpncalculator.enterValue(context.rpncalculator.number2)
    
@when('the calculator divides the numbers')
def step_impl(context):
    context.rpncalculator.divide()
    
@then('the quotient is {quotient}')
def step_impl(context,quotient):
    context.sumresult = context.rpncalculator.getResult()
    assert (context.sumresult == str(quotient))
    