(this["webpackJsonpwebsdk-component-demo"] = this["webpackJsonpwebsdk-component-demo"] || []).push([["main"],{

/***/ "./src/index.tsx":
/*!***********************!*\
  !*** ./src/index.tsx ***!
  \***********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* WEBPACK VAR INJECTION */(function(__react_refresh_utils__, __react_refresh_error_overlay__) {/* harmony import */ var _zoomus_websdk_embedded__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @zoomus/websdk/embedded */ "./node_modules/@zoomus/websdk/embedded.js");
/* harmony import */ var _zoomus_websdk_embedded__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_zoomus_websdk_embedded__WEBPACK_IMPORTED_MODULE_0__);
__webpack_require__.$Refresh$.runtime = __webpack_require__(/*! ./node_modules/react-refresh/runtime.js */ "./node_modules/react-refresh/runtime.js");
__webpack_require__.$Refresh$.setup(module.i);


const rootElement = document.getElementById("ZoomEmbeddedApp");
const testTool = window.testTool; // get meeting args from url

const tmpArgs = testTool.parseQuery();
const meetingConfig = {
  sdkKey: tmpArgs.sdkKey,
  meetingNumber: tmpArgs.mn,
  userName: function () {
    if (tmpArgs.name) {
      try {
        return testTool.b64DecodeUnicode(tmpArgs.name);
      } catch (e) {
        return tmpArgs.name;
      }
    }

    return "CDN#" + tmpArgs.version + "#" + testTool.detectOS() + "#" + testTool.getBrowserInfo();
  }(),
  password: tmpArgs.pwd,
  leaveUrl: "/index.html",
  role: parseInt(tmpArgs.role, 10),
  userEmail: function () {
    try {
      return testTool.b64DecodeUnicode(tmpArgs.email);
    } catch (e) {
      return tmpArgs.email;
    }
  }(),
  lang: tmpArgs.lang,
  signature: tmpArgs.signature || "",
  china: tmpArgs.china === "1",
  webEndpoint: "zoom.us"
};

if (!meetingConfig.signature) {
  window.location.href = "./nav.html";
} else {
  const zmClient = _zoomus_websdk_embedded__WEBPACK_IMPORTED_MODULE_0___default.a.createClient();
  const tmpPort = window.location.port === "" ? "" : ":" + window.location.port;
  const avLibUrl = window.location.protocol + "//" + window.location.hostname + tmpPort + "/lib";
  zmClient.init({
    debug: true,
    zoomAppRoot: rootElement,
    assetPath: avLibUrl,
    language: meetingConfig.lang
  }).then(e => {
    console.log("init success", e);
  }).catch(e => {
    console.log("init error", e);
  }); // WebSDK Embedded join

  zmClient.join({
    sdkKey: meetingConfig.sdkKey,
    signature: meetingConfig.signature,
    meetingNumber: meetingConfig.meetingNumber,
    userName: meetingConfig.userName,
    password: meetingConfig.password,
    userEmail: meetingConfig.userEmail
  }).then(e => {
    console.log("join success", e);
  }).catch(e => {
    console.log("join error", e);
  });
}

const currentExports = __react_refresh_utils__.getModuleExports(module.i);
__react_refresh_utils__.registerExportsForReactRefresh(currentExports, module.i);

if (true) {
  const isHotUpdate = !!module.hot.data;
  const prevExports = isHotUpdate ? module.hot.data.prevExports : null;

  if (__react_refresh_utils__.isReactRefreshBoundary(currentExports)) {
    module.hot.dispose(
      /**
       * A callback to performs a full refresh if React has unrecoverable errors,
       * and also caches the to-be-disposed module.
       * @param {*} data A hot module data object from Webpack HMR.
       * @returns {void}
       */
      function hotDisposeCallback(data) {
        // We have to mutate the data object to get data registered and cached
        data.prevExports = currentExports;
      }
    );
    module.hot.accept(
      /**
       * An error handler to allow self-recovering behaviours.
       * @param {Error} error An error occurred during evaluation of a module.
       * @returns {void}
       */
      function hotErrorHandler(error) {
        if (
          typeof __react_refresh_error_overlay__ !== 'undefined' &&
          __react_refresh_error_overlay__
        ) {
          __react_refresh_error_overlay__.handleRuntimeError(error);
        }

        if (typeof __react_refresh_test__ !== 'undefined' && __react_refresh_test__) {
          if (window.onHotAcceptError) {
            window.onHotAcceptError(error.message);
          }
        }

        __webpack_require__.c[module.i].hot.accept(hotErrorHandler);
      }
    );

    if (isHotUpdate) {
      if (
        __react_refresh_utils__.isReactRefreshBoundary(prevExports) &&
        __react_refresh_utils__.shouldInvalidateReactRefreshBoundary(prevExports, currentExports)
      ) {
        module.hot.invalidate();
      } else {
        __react_refresh_utils__.enqueueUpdate(
          /**
           * A function to dismiss the error overlay after performing React refresh.
           * @returns {void}
           */
          function updateCallback() {
            if (
              typeof __react_refresh_error_overlay__ !== 'undefined' &&
              __react_refresh_error_overlay__
            ) {
              __react_refresh_error_overlay__.clearRuntimeErrors();
            }
          }
        );
      }
    }
  } else {
    if (isHotUpdate && __react_refresh_utils__.isReactRefreshBoundary(prevExports)) {
      module.hot.invalidate();
    }
  }
}
/* WEBPACK VAR INJECTION */}.call(this, __webpack_require__(/*! ./node_modules/react-scripts/node_modules/@pmmmwh/react-refresh-webpack-plugin/lib/runtime/RefreshUtils.js */ "./node_modules/react-scripts/node_modules/@pmmmwh/react-refresh-webpack-plugin/lib/runtime/RefreshUtils.js"), __webpack_require__(/*! ./node_modules/react-dev-utils/refreshOverlayInterop.js */ "./node_modules/react-dev-utils/refreshOverlayInterop.js")))

/***/ }),

/***/ 1:
/*!**************************************************************************************************************************************************************************************************************************!*\
  !*** multi (webpack)/hot/dev-server.js ./node_modules/react-scripts/node_modules/@pmmmwh/react-refresh-webpack-plugin/client/ReactRefreshEntry.js ./node_modules/react-dev-utils/webpackHotDevClient.js ./src/index.tsx ***!
  \**************************************************************************************************************************************************************************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

__webpack_require__(/*! /home/robb/ROBB/Web Server/Components/node_modules/webpack/hot/dev-server.js */"./node_modules/webpack/hot/dev-server.js");
__webpack_require__(/*! /home/robb/ROBB/Web Server/Components/node_modules/react-scripts/node_modules/@pmmmwh/react-refresh-webpack-plugin/client/ReactRefreshEntry.js */"./node_modules/react-scripts/node_modules/@pmmmwh/react-refresh-webpack-plugin/client/ReactRefreshEntry.js");
__webpack_require__(/*! /home/robb/ROBB/Web Server/Components/node_modules/react-dev-utils/webpackHotDevClient.js */"./node_modules/react-dev-utils/webpackHotDevClient.js");
module.exports = __webpack_require__(/*! /home/robb/ROBB/Web Server/Components/src/index.tsx */"./src/index.tsx");


/***/ })

},[[1,"runtime-main","vendors~main"]]]);
//# sourceMappingURL=main.chunk.js.map