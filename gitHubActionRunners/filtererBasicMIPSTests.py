from tests.generateInstructionTests import filtererBasicMIPSTest as test

test.test_filterValidRTypeInstructions()
test.test_filterInvalidRTypeInstructions()
test.test_filterValidITypeInstructions()
test.test_filterInvalidITypeInstructions()
test.test_filterAnyJTypeInstructions()
