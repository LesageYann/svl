import behave
import nose.tools
from calculateur import *

@given('values height in cm')
def step_impl(context):
    context.caculator= CalculateurPoids()

@then('with 100 height I obtain a weight of 12.5 weight')
def step_impl(context):
    nose.tools.assert_equal(context.caculator.calculPoids(100), 12.5)

@then('with 150 height I obtain a weight of 50 weight')
def step_impl(context):
    nose.tools.assert_equal(context.caculator.calculPoids(150), 50)

@then('with 200 height I obtain a weight of 87.5 weight')
def step_impl(context):
    nose.tools.assert_equal(context.caculator.calculPoids(200), 87.5)
