'use strict';

import * as data from "./data.mjs";
import vision from "./vision.mjs";
import dotenv from "dotenv";

async function main() {
  // Load env vars if they are missing
  if (!process.env.NODE_ENV) {
    dotenv.load();
    // console.log(process.env.VISION_KEY);
  }

  let path = "./data/original/"
  let items = await data.getImageItems(path);
  let itemLabels=[];
  try {
    // Process items
    for (let i=0;i<items.length;i++) {
      const item = items[i];
      let labels;
      //console.log(item);
      if (data.extension(item)!='json') {
        const response = await vision(item);
        labels = JSON.stringify(response, null, 1);
        items = data.writeLabels(item, labels);
        items[i] = item;
      }
      itemLabels.push(data.readLabel(item));
    }

    // Count labels
    let counter = {};
    for (let i=0; i<itemLabels.length; i++) {
      let labels = itemLabels[i];
      for (let j=0;j<labels.length;j++) {
        let label = labels[j];
        let count = counter[label];
        if (count != null) {
          counter[label]=count+1;
        } else {
          counter[label]=1;
        }
      }
    }
    //console.log(counter);
    let sortable = [];
    for (let k in counter) {
      sortable.push({label:k,count:counter[k]})
    }
    sortable.sort(function (a, b) {
      return a.count - b.count;
    });
    console.log(sortable);

  } catch (e) {
    console.log(e);
  }

}

main();