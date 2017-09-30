'use strict';

import data from "./data.mjs";
import vision from "./vision.mjs";
import dotenv from "dotenv";

async function main() {
  // Load env vars if they are missing
  if (!process.env.NODE_ENV) {
    dotenv.load();
    // console.log(process.env.VISION_KEY);
  }

  let path = "./data/original/"
  let imageData = data(path);

  try {
    let response = await vision(imageData);
    console.log(response);
  } catch (e) {
    console.log(e);
  }

}

main();