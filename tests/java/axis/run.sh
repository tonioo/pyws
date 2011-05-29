#!/bin/bash

BASE_DIR=`dirname $(readlink -f $0)`

source $BASE_DIR/common.sh

java -cp $CP org.junit.runner.JUnitCore \
    testcases.AddSimpleTestCase \
    testcases.AddIntegersTestCase \
    testcases.AddFloatsTestCase \
    testcases.AddStringDictsTestCase \
    testcases.AddIntegerDictsTestCase \
    testcases.AddStringListsTestCase \
    testcases.AddIntegerListsTestCase \
    testcases.SumTreeTestCase \
    testcases.GetTreeTestCase