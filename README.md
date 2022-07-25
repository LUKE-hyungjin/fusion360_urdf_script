# fusion360 urdf Addin  
Inspired by [syuntoku14/fusion2urdf](https://github.com/syuntoku14/fusion2urdf) and [dheena2k2/fusion2urdf-ros2](https://github.com/dheena2k2/fusion2urdf-ros2), this repertoire is ADDIN, who converts it into a pure Urdf file. Check out [syuntoku14/fusion2urdf](https://github.com/syuntoku14/fusion2urdf) for converting fusion360 model to robot description package of ROS1.
## Difference
* Pure urdf file
* Color reflection  
![image](https://user-images.githubusercontent.com/68213792/180804341-0097e49f-3c57-46f2-ace4-095952cc445c.png)
  
It can be used in unity, omniverse  
### Unity  
![image](https://user-images.githubusercontent.com/68213792/180796529-3d922af0-85a8-4711-830b-10f04173fbff.png)
### Omniverse  
![image](https://user-images.githubusercontent.com/68213792/180797344-9ac42ea7-5696-4fdb-ab7e-a6e3844d0081.png)


## Installation

Run the following command in your shell.

##### Windows (In PowerShell)

```powershell
cd <path to fusion2urdf-ros2cpp>
Copy-Item ".\URDF\" -Destination "${env:APPDATA}\Autodesk\Autodesk Fusion 360\API\Scripts\" -Recurse
```

##### macOS (In bash or zsh)

```bash
cd <path to fusion2urdf-ros2cpp>
cp -r ./URDF "$HOME/Library/Application Support/Autodesk/Autodesk Fusion 360/API/Scripts/"
```
## What is this script?
This is a fusion 360 script to export urdf from fusion 360 directly.

This exports:
* .urdf file of your model
* .stl files of your model


**Enjoy your Fusion 360 and Robotic life!**
