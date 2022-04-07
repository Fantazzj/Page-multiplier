@ECHO OFF

MKDIR "%USERPROFILE%\Page-multiplier\BACKUP"
COPY %1 "%USERPROFILE%\Page-multiplier\BACKUP\%~nx1"
IF NOT "%ERRORLEVEL%" == "0" PAUSE

python "%USERPROFILE%\Page-multiplier\x10.py" %1 10 "%USERPROFILE%\Page-multiplier\templates\ruled with vertical line.pdf"
IF NOT "%ERRORLEVEL%" == "0" PAUSE

EXIT
