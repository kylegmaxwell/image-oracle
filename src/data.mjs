'use strict';

import fs from 'fs';

export default async function(path) {
  let items = await getItems(path);
  let item = path+items[1];
  console.log("Loading "+item);
  let data = await getImage(item);
  // console.log(data);
  return data;
}

function getImage(itemPath) {
  return new Promise((resolve, reject)=>{
    fs.readFile(itemPath, function(err, data){
      resolve(data.toString('base64'));
    });
  });
};

function getItems(path){
    // console.log("LOAD", path);
    return new Promise((resolve, reject) => {
        fs.readdir(path, (err, items) => {
            if (items.length>0) {
                resolve(items);
            } else {
                reject(null);
            }
        });
    });
}