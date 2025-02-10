@echo off
setlocal

:: Define hashcat path (since the bat file is in hashcat directory)
set HASHCAT_PATH=hashcat.exe

:: Define custom charset for ?1 (special characters and numbers)
set CHARSET=-1 0123456789!@#_.*

:: Define hash file and output file
set HASH_FILE=hash.hc22000
set OUTPUT_FILE=cracked.txt

:: Read masks from mask.txt
for /F "tokens=*" %%A in (masks.txt) do (
    echo Running mask: %%A
    %HASHCAT_PATH% %CHARSET% -a 3 -m 22000 %HASH_FILE% %%A -o %OUTPUT_FILE% --potfile-disable
    
    :: Check if password was cracked
    if exist %OUTPUT_FILE% (
        echo Password cracked!
        type %OUTPUT_FILE%
        goto :end
    )
)

:end
echo No passwords cracked.
pause
endlocal