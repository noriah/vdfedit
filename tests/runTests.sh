#!/bin/bash
#
#

test_results() {
	if [ -n "$1" ]; then
		echo '******Shit, Something went wrong******'
	else
		echo '[ OK ]'
	fi
}


echocmd='echo; echo "[Press Enter to Continue]"; read -s; echo'
if [ -n "$1" ]; then
	waitcmd=""
else
	waitcmd="eval $echocmd"
fi

command -v diff>/dev/null 2>&1 || { echo >&2 \
"I would check the results for you, but you dont have diff\n
So all these results are going to fail.
Just compare the ouputs to the files in the test/files folder."; }

vdfedit="../vdfedit"
out="./out/"

rm -rf $out>/dev/null
mkdir $out

chmod +x $vdfedit

echo
echo "Will now begin a series of tests to test vdfedit"
echo

$waitcmd


echo "This test will check that we are able to parse vdf files correctly."
$waitcmd
#Will Output All Values in files/localconfig.vdf
$vdfedit files/localconfig.vdf >> out/localconfig.vdf.log
output=`diff files/localconfig.vdf.log.check out/localconfig.vdf.log`
test_results $output

echo
echo
#Will Report Error: Incorrectly formed key-value structure: CauseError.NoErrorYet.NoErrorYet.OhhhWeHitAnError
echo "This test will check that minimal error checking works."
echo "Should return:"
echo "Something went wrong near here: CauseError.NoErrorYet.NoErrorYet.OhhhWeHitAnError"
$waitcmd
$vdfedit files/causeerror.vdf
echo "Did It?"
$waitcmd

echo
echo
echo "This test will check that we can edit a vdf"
$waitcmd
#Will Create file out/localconfig1.vdf which will have 2 new Values, near the bottom
$vdfedit files/localconfig.vdf,out/localconfig1.vdf \
UserLocalConfigStore.shortcuts.TestEntry.Var=Test1,\
UserLocalConfigStore.shortcuts.TestEntry.Var2=Test2
output=`diff files/localconfig1.vdf.check out/localconfig1.vdf`
test_results $output

echo
echo "This test will check that we can crate a new vdf"
$waitcmd
$vdfedit out/created.vdf \
TestSet.Test5.Test4.Test3.Test2.Test1.Test=Test,\
TestSet.Test4.Test3.Test2.Test1.Test=Test,\
TestSet.Test3.Test2.Test1.Test=Test,\
TestSet.Test2.Test1.Test=Test,\
TestSet.Test1.Test=Test,\
TestSet.Test5.Test4.Test3.Test2.Test=Test,\
TestSet.Test4.Test3.Test2.Test=Test,\
TestSet.Test3.Test2.Test=Test,\
TestSet.Test2.Test=Test,\
TestSet.Test5.Test4.Test3.Test=Test,\
TestSet.Test4.Test3.Test=Test,\
TestSet.Test3.Test=Test,\
TestSet.Test5.Test4.Test2.Test1.Test=Test,\
TestSet.Test4.Test2.Test1.Test=Test,\
TestSet.Test5.Test4.Test2.Test=Test,\
TestSet.Test4.Test2.Test=Test,\
TestSet.Test5.Test4.Test1.Test=Test,\
TestSet.Test4.Test1.Test=Test,\
TestSet.Test5.Test4.Test=Test,\
TestSet.Test4.Test=Test,\
TestSet.Test5.Test3.Test2.Test1.Test=Test,\
TestSet.Test5.Test3.Test2.Test=Test,\
TestSet.Test5.Test3.Test1.Test=Test,\
TestSet.Test5.Test3.Test=Test,\
TestSet.Test5.Test2.Test1.Test=Test,\
TestSet.Test5.Test2.Test=Test,\
TestSet.Test5.Test1.Test=Test,\
TestSet.Test5.Test=Test
echo
output=`diff files/created.vdf.check out/created.vdf`
test_results $output

echo "Tests Complete"
exit 0
