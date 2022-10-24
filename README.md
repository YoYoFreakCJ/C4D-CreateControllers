# Introduction
This script creates some controller nulls for the selected objects.

# Usage
1. Select objects.
2. Execute script.

For each selected object this creates a new Null at the root level. Each selected object receives a constraint tag set to Transform. Each Null shape is set to Sphere, the display and icon colors are set to white.

# Installation
Create a new script in the Script Manager in Cinema 4D. Paste the contents of CreateControllers.py into the script and save it. Then use it as you see fit (like making it a clickable icon on your layout).

# Customization
You can customize the script to your likings:

|Purpose|How|
|-|-|
|Change the controller name suffix|Find the line which says `controllerNameSuffix = '...'` and change the suffix to your liking.|
|Change the Null shape|Find the line which says `controllerNullType = controllerNullType = c4d.NULLOBJECT_DISPLAY_SPHERE` and change the value to your liking. See [documentation](https://developers.maxon.net/docs/Cinema4DPythonSDK/html/classic_resource/object/onull.html?highlight=onull#parameters) for other values.|
|Change the icon and display color|Find the line which says `controllerColor = c4d.Vector(1)` and change the value to your liking.|
|Disable the `Maintain Original` checkmark in the Offset section|Find the line which says `tag[c4d.ID_CA_CONSTRAINT_TAG_PSR_MAINTAIN]` and remove it.|

If you'd like to assist me in making a GUI for these settings please contact me.
