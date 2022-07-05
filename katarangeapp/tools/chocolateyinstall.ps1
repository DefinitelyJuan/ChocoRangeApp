$name = 'katarangeapp'
$toolsDir = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
$FileLocation = Join-Path $toolsDir "rangeconsoleapp.exe"

Install-BinFile -name $name -path $FileLocation