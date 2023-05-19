@echo off
for /r "." %%a in (*.md) do (
    echo %%~na
    type %%a >> %%~na-merged.md
    for /f "delims=" %%I in (%%~na-merged.md) do findstr /X /C:"%%I"   %%~na.md >NUL ||(echo;%%I)>>%%~na.md
    del %%~na-merged.md
)