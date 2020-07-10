(function(_eleventy) {
  var eleventy = function() {
    return _eleventy;
  };

  if (typeof module !== "undefined" && module.exports) {
    module.exports = eleventy;
  } else if (typeof define === "function" && define.amd) {
    define(eleventy);
  } else if (window) {
    window.eleventy = eleventy;
  }
})(110);
