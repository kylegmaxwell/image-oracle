'use strict';

// Imports the Google Cloud vision library
import Vision from '@google-cloud/vision';
import request from 'request';

// Run Google Cloud Vision label detection on an image file
// @param fileName The name of the image file to process
export default function (fileName) {
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