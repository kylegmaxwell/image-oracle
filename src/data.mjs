'use strict';

import fs from 'fs';

function getImage(itemPath) {
  return new Promise((resolve, reject)=>{
    fs.readFile(itemPath, function(err, data){
      resolve(data.toString('base64'));
    });
  });
};

export async function getImageItems(path) {
  let allItems = await getItems(path);
  let items = [];
  let extensions = ['jpg', 'png'];
  for (let i=0; i<allItems.length; i++) {
    let item = allItems[i];
    let split = item.split('.');
    let extension = split[split.length-1];
    if (extensions.indexOf(extension.toLowerCase())!==-1) {
      const stats = fs.statSync(item);
      const fileSizeMB = stats.size / 1000000.0;
      // Vision api supports up to 4MB
      if (fileSizeMB < 4) {
        items.push(item);
      }
    }
  }
  return items;
}

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

export function writeLabels(imagePath, labels) {
  const split = imagePath.split('.');
  const extension = split[split.length-1];
  const outPath = imagePath.substring(0,imagePath.length-extension.length)+'json';
  fs.writeFileSync(outPath, labels);
}