[Version]
Class=IEXPRESS
SEDVersion=3
[Options]
PackagePurpose=InstallApp
ShowInstallProgramWindow=0
HideExtractAnimation=0
UseLongFileName=0
InsideCompressed=0
CAB_FixedSize=0
CAB_ResvCodeSigning=0
RebootMode=I
InstallPrompt=%InstallPrompt%
DisplayLicense=%DisplayLicense%
FinishMessage=%FinishMessage%
TargetName=%TargetName%
FriendlyName=%FriendlyName%
AppLaunched=%AppLaunched%
PostInstallCmd=%PostInstallCmd%
AdminQuietInstCmd=%AdminQuietInstCmd%
UserQuietInstCmd=%UserQuietInstCmd%
SourceFiles=SourceFiles
[Strings]
InstallPrompt=This will install all necessary files needed.
DisplayLicense=
FinishMessage=Install is complete! Please Create a shortcut on the desktop for the SUITEGEN.py file
TargetName=C:\SUITE_GEN\SUITE_GENERATOR.EXE
FriendlyName=SUITE_GENERATOR
AppLaunched=python-2.7.13.exe
PostInstallCmd=SUITE_GEN.EXE
AdminQuietInstCmd=
UserQuietInstCmd=
FILE0="python-2.7.13.exe"
FILE1="SUITE_GEN.EXE"
[SourceFiles]
SourceFiles0=C:\Users\ahmed.mahmoud\
SourceFiles1=C:\Python27\
[SourceFiles0]
%FILE0%=
[SourceFiles1]
%FILE1%=
