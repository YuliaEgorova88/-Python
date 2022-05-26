from Calculations.input_data import init_data
from Calculations.prog import mathOperation
from Calculations.out_data import view


def start():
    init_data.init()
    result = mathOperation.do(init_data.userInput)
    view.printResult(init_data.userInput, result)
