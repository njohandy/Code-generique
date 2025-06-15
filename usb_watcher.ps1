# usb_watcher.ps1
Register-WmiEvent -Class Win32_VolumeChangeEvent -Action {
    Start-Sleep -Seconds 2
    $drive = Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DriveType -eq 2 } | Select-Object -Last 1
    if ($drive) {
        $driveLetter = $drive.DeviceID
        Write-Host "Clé USB détectée : $driveLetter"
        python.exe "C:\Scripts\copy_usb.py" $driveLetter
    }
} | Out-Null

Write-Host "Surveillance des clés USB activée. Appuyez sur [Entrée] pour arrêter."
Read-Host
