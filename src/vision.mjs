'use strict';

// Imports the Google Cloud vision library
import Vision from '@google-cloud/vision';
import request from 'request';

// @param fileName The name of the image file to process
export default function (data) {
  return apiVision(data);
}

function restVision(imageData) {
  const key = process.env.VISION_KEY;
  let body = {
    "requests":[{
      "image":{
        //"content":imageData
        "source":{
          "imageUri": "gs://image-oracle/original/Beard%20Model%20The%20Cut%20Buddy%20Shaver%20Razor.jpg"
        }
      },
      "features":[{
        "type":"LABEL_DETECTION",
        "maxResults":1
      }]
    }]
  };
  // console.log(JSON.stringify(body));
  return new Promise((resolve, reject)=>{
    request.post(
      'https://vision.googleapis.com/v1/images:annotate?key='+key,
      { json: body },
      (error, response, body) => {
        console.log('Response status',response.statusCode);
        if (!error) {
          if (response.statusCode == 200) {
            resolve(body);
          } else {
            reject(JSON.stringify(body.error));
          }
        } else {
          reject(error);
        }
      }
    );
  });
}

function apiVision(fileName) {
  const vision = Vision();
  // Prepare the request object
  const request = {
    source: {
      filename: fileName
    }
  };

  // Performs label detection on the image file
  return vision.labelDetection(request);
}