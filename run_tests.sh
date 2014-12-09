#!/bin/bash
#
#

test_results() {
	if [ -n "$1" ]; then
		echo "[ FAIL ]"
		exit 1
	else
		echo '[ PASS ]'
	fi
}

ls -la /home/travis/virtualenv/python2.7.8/lib/python2.7/site-packages

vdfedit="./vdfedit"

rm -rf tests/out/>/dev/null
mkdir tests/out

chmod +x $vdfedit

$vdfedit>/dev/null
$vdfedit -h>/dev/null
$vdfedit -p>/dev/null
$vdfedit -g apple>/dev/null
$vdfedit -s apple=a>/dev/null
$vdfedit "tests/test.vdf">/dev/null
$vdfedit "tests/test.vdf" -g apple -p>/dev/null
$vdfedit "tests/test.vdf" -g apple>/dev/null
$vdfedit "tests/test.vdf" -p>/dev/null



echo "Will now begin a series of tests to test vdfedit"


echo "Read a VDF"
#Will Output All Values in files/localconfig.vdf
$vdfedit tests/localconfig.vdf -p > tests/out/localconfig.vdf.out
output=`diff tests/localconfig.vdf.out.check tests/out/localconfig.vdf.out`
test_results "$output"

#Will Report Error: Incorrectly formed key-value structure: CauseError.NoErrorYet.NoErrorYet.OhhhWeHitAnError
echo "This test will check that minimal error checking works."
echo "Should return an error"
#echo "Something went wrong near here: CauseError.NoErrorYet.NoErrorYet.OhhhWeHitAnError"
$vdfedit tests/causeerror.vdf -c

echo "This test will check that we can edit a vdf"
#Will Create file out/localconfig1.vdf which will have 2 new Values, near the bottom
$vdfedit tests/localconfig.vdf -o tests/out/localconfig1.vdf \
-sUserLocalConfigStore.shortcuts.TestEntry.Var=Test1 \
-sUserLocalConfigStore.shortcuts.TestEntry.Var2=Test2
output=`diff tests/localconfig1.vdf.check tests/out/localconfig1.vdf`
test_results "$output"

echo
echo "This test will check that we can crate a new vdf"
$vdfedit tests/out/created.vdf < tests/create.vdfe
echo
output=`diff tests/created.vdf.check tests/out/created.vdf`
test_results "$output"

echo "Pass"
exit 0

