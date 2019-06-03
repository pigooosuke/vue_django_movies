//
// vue.confg.js
//

module.exports = {
  devServer: {
    proxy: {
      "^/(graphql|admin|dev/graphql|static/admin)": {
        target: "http://localhost:8000",
      }
    }
  },
  configureWebpack: {
    devtool: "source-map"
  },

  outputDir: "dist/",
  assetsDir: "static/",
  indexPath: "index.html"
};
