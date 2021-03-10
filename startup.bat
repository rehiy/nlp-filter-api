@ECHO OFF

CD /d %~dp0

::加载Python环境

IF EXIST D:\RunTime\python3\runtime.bat (
    CALL D:\RunTime\python3\runtime set "%~n0"
)

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::编译项目

CD /d %~dp0

pip3 install -q -r nlp-serve\requirements.txt

python -m nlp-serve

IF "%1" == "" CMD /k
