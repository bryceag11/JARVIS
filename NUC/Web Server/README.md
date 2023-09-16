# Zoom Meeting SDK Sample App - Web

Use of this sample app is subject to our [Terms of Use](https://zoom.us/docs/en-us/zoom_api_license_and_tou.html).

The [Zoom Meeting SDK](https://marketplace.zoom.us/docs/sdk/native-sdks/web) embeds the Zoom Meeting and Webinar experience in a website through a highly optimized WebAssembly module.

![Zoom Meeting SDK Client View](https://marketplace.zoom.us/docs/images/sdk/msdk-web-client-view.gif)

## Installation

To get started, clone the repo:

`$ git clone https://github.com/zoom/sample-app-web.git`

## Setup

1. Once cloned, navigate to the `sample-app-web/CDN` directory for the Client View CDN sample, or `sample-app-web/Local` for the Client View NPM sample, or `sample-app-web/Components` for the Component View NPM sample:

   `$ cd sample-app-web/CDN` or `$ cd sample-app-web/Local` or `$ cd sample-app-web/Components`

1. Then install the dependencies:

   `$ npm install`

1. Open the directory in your code editor.

1. Open the `sample-app-web/CDN/js/index.js` or `sample-app-web/Local/js/index.js` or `sample-app-web/Components/tools/nav.js` file respectively, and enter required values for the variables:

   | Key                   | Value Description |
   | -----------------------|-------------|
   | `SDK_KEY`     | Your SDK Key. Required. |
   | `SDK_SECRET`  | Your SDK Secret. Required. |

   Example:

   ```js
   var SDK_KEY = "YOUR_SDK_KEY"
   var SDK_SECRET = "YOUR_SDK_SECRET"
   ```

   > Reminder to not publish this sample app as is. Replace the frontend signature generator with a [backend signature generator](https://marketplace.zoom.us/docs/sdk/native-sdks/auth#generate-the-sdk-jwt) to keep your SDK Secret safe.

1. Save `index.js` or `nav.js` respectively.

1. Run the app:

   `$ npm start`

## Usage

1. Navigate to http://localhost:9999 for the `CDN` or
`Local` sample, or http://localhost:3000 for the `Components` sample. Then, enter in a Meeting or Webinar number and passcode, choose host or attendee (participant), and, click "join".

