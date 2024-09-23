# This script converts CRLF to LF in all files in the _posts directory and its subdirectories
# Set the relative path to ../_posts
$directory = "$PSScriptRoot\..\_posts"

# Get all files in the directory and subdirectories
$files = Get-ChildItem -Path $directory -Recurse -File

# Loop through each file, replace CRLF with LF
foreach ($file in $files) {
    $content = Get-Content $file.PSPath -Raw
    $content = $content -replace "`r`n", "`n"
    Set-Content -Path $file.PSPath -Value $content -NoNewline
}
