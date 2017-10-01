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
  try {
    for (let i=0;i<items.length;i++) {
      const item = items[i];
      console.log(item);
      const response = await vision(item);
      const labels = JSON.stringify(response, null, 1);
      data.writeLabels(item, labels);
    }

  } catch (e) {
    console.log(e);
  }

}

main();