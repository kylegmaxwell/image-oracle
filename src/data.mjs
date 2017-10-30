'use strict';

import fs from 'fs';

// get a list of image paths in a directory
// skip images that already have json
export async function getImageItemsOrJson(path) {
  let allItems = await getItems(path);
  let items = [];
  let extensions = ['jpg', 'jpeg', 'png'];
  for (let i=0; i<allItems.length; i++) {
    let item = allItems[i];
    if (extensions.indexOf(extension(item)) !== -1) {
      const stats = fs.statSync(item);
      const fileSizeMB = stats.size / 1000000.0;

      const itemJson = changeExtension(item);
      const hasJson = exists(itemJson);

      if (hasJson) {
        items.push(itemJson);
      } else if (fileSizeMB < 4) {
        // Vision api supports up to 4MB
        items.push(item);
      }
    }
  }
  return items;
}

// Get the file extension from a path string
export function extension(path) {
  let split = path.split('.');
  let extension = split[split.length-1];
  return extension.toLowerCase();
}

// Check if a file path exists on disk
function exists(path) {
  try{
      fs.accessSync(path)
  }
  catch (e) {
    return false;
  }
  return true;
}

// Get a list of all file paths for files in a directory
function getItems(path){
  return new Promise((resolve, reject) => {
    fs.readdir(path, (err, items) => {
      if (items.length>0) {
        resolve(items.map(item=>path+item));
      } else {
        reject(null);
      }
    });
  });
}

// Get a string with json extension instead of it's original
function changeExtension(path) {
  const split = path.split('.');
  const extension = split[split.length-1];
  return path.substring(0,path.length-extension.length)+'json';
}

// Write the labels as a JSON file
export function writeLabels(imagePath, labels) {
  const outPath = changeExtension(imagePath);
  fs.writeFileSync(outPath, labels);
  return outPath
}

// Read the labels from a json file
export function readLabel(path) {
  const annotations = JSON.parse(fs.readFileSync(path, 'utf8'))[0].labelAnnotations;
  return annotations.map(o=>o.description);
}