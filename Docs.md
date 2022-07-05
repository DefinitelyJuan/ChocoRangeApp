# Como subir un paquete a Chocolatey?
## Crear el ejecutable.
En nuestro caso con Python se puede utilizar py Install para crear el archivo binario .exe que ejecuta la aplicacion.
Esto se puede hacer haciendo uso de pyInstaller --onefile pathtofile.py 
## Crear el paquete Chocolatey (NUPKG)
1. En powershell escriba ```choco new nombreapp```.
2. Entrar a la carpeta nombreapp, luego en tools y en el archivo chocolateyinstall.ps1 y luego escriba el siguiente codigo:
 ```$name = 'nombreapp' $toolsDir = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)" $FileLocation = Join-Path $toolsDir "nombreejecutable.exe" Install-BinFile -name $name -path $FileLocation```.

3. Regrese a la carpeta nombreapp y llene el archivo nombreapp.nuspec.
4. En el powershell apuntando al directorio nombreapp ejecute el comando ```choco pack nombreapp.nuspec```. 
5. Si lo desea installe el paquete haciendo uso de ```choco install nombreapp.version.nupkg```
6. Luego subalo al repositorio publico de Chocolatey: 
```choco apikey --key llaveapi --source https://push.chocolatey.org/```
```choco push nombreapp.version.nupkg --source https://push.chocolatey.org/```. Para mas informacion entre a la pestaña account de Chocolatey, donde podra encontrar su api key.
## Instalar el paquete
choco install nombreapp --version version. Luego de la instalacion simplemente debe ejecutar el comando nombreapp en su consola para correr el programa.
