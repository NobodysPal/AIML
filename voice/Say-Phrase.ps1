<#
.SYNOPSIS
  Speaks phrase from python

.DESCRIPTION
  Speaks phrase from python

.TODO
  
.NOTES
  Version:        1.0
  Author:         Jeff Pierdomenico
  Creation Date:  31 Dec 2016
  Purpose/Change: Initial script development

#>

#---------------------------------------------------------[Initialisations]--------------------------------------------------------

#Set Default Error Action
$ErrorActionPreference = 'Stop'

#Import PSLogging Module
#Import-Module PSLogging

#----------------------------------------------------------[Declarations]----------------------------------------------------------

#Script Version
$sScriptVersion = '1.0'

#Log File Info
#$sLogPath = 'C:\Windows\Temp'
#$sLogName = '<script_name>.log'
#$sLogFile = Join-Path -Path $sLogPath -ChildPath $sLogName

#-----------------------------------------------------------[Functions]------------------------------------------------------------

Function Say-Phrase {
    param(
          [string]$phrase
         )
    Try {
        
        # Loading all the voice sysnthesis
        Add-Type -AssemblyName System.speech -ErrorAction SilentlyContinue
        $speak=new-object System.Speech.Synthesis.SpeechSynthesizer
        $speak.Speak($phrase)
    }
    Catch {
        Write-Host "Error: Could not load the Voice Synethesizer." -ForegroundColor Red
    }
    Finally {
        $speak.Dispose()
    }
}