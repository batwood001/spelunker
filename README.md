# spelunker
A Sublime Text 3 plugin that digs through deep JSON objects so you don't have to!

## Description
Given a value in an arbitarily nested JSON object, Spelunker will return the path to that value as a lodash chain.

## Usage
1. Have a properly formatted JSON object in a ST3 tab. 

2. Highlight the value you want to retrieve the path to (for now, the path must be a string--if it's an int or bool, just throw "'s around it). Do not highlight the " " marks. Use the keyboard shortcut **cmd+shift+s** or right-click on the value and select "spelunker" from the menu. 

3. The lodash-formatted path is now in your clipboard.

## Installation
Clone this repo into /Users/{username}/Library/Application Support/Sublime Text 3/Packages/

Eventually this will be a proper ST3 package.

## Bugs
- If your object contains multiple instances of the same value, Spelunker will not necessarily find the path to the instance of the value you are looking for. This will be fixed in future versions, but for now you can simply add some extra text to your value to make it unique.
- If spelunker needs to iterate through an array that contains multiple objects with the same property, and spelunker is finding the value based on one of those properties, it will not know how to distinguish among these objects. e.g.: https://www.youtube.com/watch?v=sI8w2xnrcqQ&feature=youtu.be
