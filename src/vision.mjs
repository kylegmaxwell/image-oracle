'use strict';

// Imports the Google Cloud vision library
// import Vision from '@google-cloud/vision';
import request from 'request';

// @param fileName The name of the image file to process
export default function (imageData) {
  const key = process.env.VISION_KEY;
  let body = {
    "requests":[{
      "image":{
        "content":imageData
      },
      "features":[{
        "type":"LABEL_DETECTION",
        "maxResults":1
      }]
    }]
  };

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

  // const vision = Vision();

  // // Prepare the request object
  // const request = {
  //   source: {
  //     filename: fileName
  //   }
  // };

  // // Performs label detection on the image file
  // vision.labelDetection(request)
  //   .then((results) => {
  //     const labels = results[0].labelAnnotations;

  //     console.log('Labels:');
  //     labels.forEach((label) => console.log(label.description));
  //   })
  //   .catch((err) => {
  //     console.error('ERROR:', err);
  //   });
}